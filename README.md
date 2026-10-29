# Ammar Mawassi — Personal Portfolio

An editorial portfolio for a Computer Science student exploring software by building it.

[Live portfolio](https://ammar31mawassi.github.io/Personal-Portfolio/)

## Design and content

- Warm paper, black typography, and a red accent, based on the selected Software Editorial concept.
- Exactly three featured projects with wide conceptual covers: Chess AI, Concurrent Robotics, and Scheme Compiler.
- Six compact project cards, a personal introduction, tutoring, contact links, and recent public GitHub activity.
- Local Anton font with its OFL license in `assets/fonts/`; system sans-serif body text.
- Responsive layouts, a keyboard skip link, visible focus styles, image alt text, and reduced-motion support.

The featured images are generated editorial concept covers. They are not application screenshots or photographs of hardware built for these projects.

## Local preview

Python 3 is the only build dependency. JavaScript has no package dependencies.

```powershell
python scripts/build.py
python -m http.server 4182 --directory _site --bind 127.0.0.1
```

Open `http://127.0.0.1:4182/`.

```powershell
python -m unittest discover -s scripts -p 'test_*.py'
node --check assets/github-sync.js
```

## GitHub synchronization

`.github/workflows/deploy.yml` builds and deploys through GitHub Pages on pushes to `main`, manual workflow runs, and hourly at minute 17 UTC. Commits to other repositories appear on the next refresh, not immediately. GitHub may delay schedules and may disable scheduled workflows in public repositories after 60 days without activity. Re-enable the workflow in Actions if needed.

The build creates `_site/assets/github-data.json` with selected public fields. Visitors load that local snapshot rather than calling GitHub. Build failures preserve the last deployed site; the complete curated HTML remains usable if the snapshot cannot load.

Edit `index.html` to choose projects, order, labels, and imagery. Keep matching repository names in `projects.json` and `data-repo` attributes. Descriptions, detected languages, repository URLs, and last-push dates refresh automatically. `descriptionOverrides` supports editorial corrections when repository metadata differs from the current implementation; Chess AI uses its verified supervised-training scope rather than claiming PUCT or self-play.

Biography, learning notes, and cover images stay editorial. `excludeFromActivity` controls exclusions from the three recent public repositories. Forks and archived repositories are excluded from recent activity.

`GITHUB_TOKEN` is optional locally and used only during builds. No token is published.

## Main files

- `index.html`: semantic page and curated content.
- `assets/portfolio.css`: visual system and responsive layouts.
- `assets/github-sync.js`: snapshot rendering and static fallback.
- `scripts/build.py`: public GitHub data collection and static build.
- `projects.json`: repository selection and editorial overrides.
- `design-qa.md`: design comparison and verification results.
