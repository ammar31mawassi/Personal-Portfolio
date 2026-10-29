import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build


def repository(name, **changes):
    return {"name": name, "private": False, "owner": {"login": build.USERNAME},
            "description": "Description from GitHub", "fork": False, "archived": False,
            "pushed_at": "2026-10-29T12:00:00Z", **changes}


class GitHubBuildTests(unittest.TestCase):
    def test_pagination_and_public_owner_filter(self):
        first = [repository(str(i)) for i in range(98)]
        first += [repository("private", private=True), repository("foreign", owner={"login": "other"})]
        with patch.object(build, "github", side_effect=[first, [repository("last")]]) as api:
            result = build.public_repositories()
        self.assertEqual(99, len(result))
        self.assertEqual("last", result[-1]["name"])
        self.assertIn("page=2", api.call_args.args[0])

    def test_build_exports_only_selected_fields_and_curated_order(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            (root / "index.html").write_text("<h1>Curated</h1>")
            (root / "projects.json").write_text(json.dumps({"curated": ["second", "first"], "excludeFromActivity": ["profile"]}))
            repos = [repository("first", secret_field="must not publish"), repository("second"),
                     repository("profile"), repository("fork", fork=True), repository("old", archived=True)]
            with patch.object(build, "ROOT", root), patch.object(build, "public_repositories", return_value=repos), patch.object(build, "github", return_value={"Python": 50, "C": 100}):
                build.build()
            text = (root / "_site/assets/github-data.json").read_text()
            data = json.loads(text)
            self.assertEqual(["second", "first"], [r["name"] for r in data["repositories"]])
            self.assertEqual(["C", "Python"], data["repositories"][0]["languages"])
            self.assertEqual({"first", "second"}, {r["name"] for r in data["recent"]})
            self.assertNotIn("must not publish", text)
            self.assertEqual("<h1>Curated</h1>", (root / "_site/index.html").read_text())

    def test_missing_public_project_stops_build(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "projects.json").write_text(json.dumps({"curated": ["missing"], "excludeFromActivity": []}))
            with patch.object(build, "ROOT", root), patch.object(build, "public_repositories", return_value=[]):
                with self.assertRaisesRegex(ValueError, "unavailable publicly"):
                    build.build()
            self.assertFalse((root / "_site").exists())


if __name__ == "__main__":
    unittest.main()
