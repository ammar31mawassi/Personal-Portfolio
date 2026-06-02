<!-- bettergithub:generated-file -->
# Personal Portfolio Architecture

This is a static portfolio: one HTML entry point, local image assets, and documentation that explains how project evidence should be maintained.

## Reviewer Flow

1. Read the root README for the project purpose, setup, usage, and test signal.
2. Inspect the main source locations:
   - `index.html`
   - `assets`
   - `docs`
3. Run or manually verify the project using the test plan.
4. Capture any new screenshot or terminal output under `docs/` so the README stays evidence-based.

## Boundaries

- This documentation pass does not alter runtime behavior.
- Secrets, API keys, and local machine paths should stay out of commits.
- Generated binaries and large local outputs should only be committed when they are intentional assignment artifacts.
