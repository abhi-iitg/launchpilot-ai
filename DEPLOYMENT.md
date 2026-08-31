# Deployment Guide

## Streamlit Community Cloud

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Connect the GitHub account.
4. Create an app.
5. Select the repository, `main` branch, and `app.py` as the entrypoint.
6. Select Python 3.12 in Advanced settings.
7. Deploy.
8. Open the app and run the QA checklist in `README.md`.

The repository keeps `requirements.txt` at the root because Community Cloud installs dependencies from a recognized dependency file in the app/repository structure.

## Troubleshooting

### ModuleNotFoundError
Confirm the missing package is declared in `requirements.txt`, then commit and redeploy.

### Wrong entrypoint
Use `app.py` exactly.

### File not found
Run the app from the repository root locally and keep repository paths relative. The application uses `pathlib` and does not depend on `C:\Users\...` paths.

### Python version mismatch
Use Python 3.12 locally and in Community Cloud.

### State appears reset
Streamlit session state belongs to a browser session. A browser reload can reset session state. Use the workspace reset/demo controls to restore a known starting state.
