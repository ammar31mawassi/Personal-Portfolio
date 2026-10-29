"""Build the static portfolio with a fresh, public-only GitHub snapshot."""

import json
import os
from pathlib import Path
import shutil
import urllib.request
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
USERNAME = "ammar31mawassi"


def github(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "portfolio-sync"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    request = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def public_repositories():
    repositories = []
    page = 1
    while True:
        batch = github(f"/users/{USERNAME}/repos?per_page=100&page={page}&sort=pushed&direction=desc")
        repositories.extend(repo for repo in batch if not repo["private"] and repo["owner"]["login"].lower() == USERNAME)
        if len(batch) < 100:
            return repositories
        page += 1


def build():
    config = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    repositories = public_repositories()
    by_name = {repo["name"]: repo for repo in repositories}
    curated = []
    for name in config["curated"]:
        if name not in by_name:
            raise ValueError(f"Curated repository is unavailable publicly: {name}. Update projects.json.")
        repo = by_name[name]
        languages = github(f"/repos/{USERNAME}/{name}/languages")
        curated.append({
            "name": name,
            "url": f"https://github.com/{USERNAME}/{name}",
            "description": config.get("descriptionOverrides", {}).get(name, repo["description"]),
            "languages": sorted(languages, key=languages.get, reverse=True)[:3],
            "pushedAt": repo["pushed_at"],
        })
    recent = sorted(
        (repo for repo in repositories if not repo["fork"] and not repo["archived"]
         and repo["name"] not in config["excludeFromActivity"] and repo["pushed_at"]),
        key=lambda repo: repo["pushed_at"], reverse=True,
    )[:3]
    snapshot = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "repositories": curated,
        "recent": [{
            "name": repo["name"], "url": f"https://github.com/{USERNAME}/{repo['name']}",
            "description": config.get("descriptionOverrides", {}).get(repo["name"], repo["description"]), "pushedAt": repo["pushed_at"],
        } for repo in recent],
    }
    output = ROOT / "_site"
    output.mkdir(exist_ok=True)
    shutil.copy2(ROOT / "index.html", output / "index.html")
    shutil.copytree(ROOT / "assets", output / "assets", dirs_exist_ok=True)
    (output / ".nojekyll").touch()
    (output / "assets" / "github-data.json").write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built {len(curated)} curated projects and {len(recent)} recent public updates in _site/")


if __name__ == "__main__":
    build()
