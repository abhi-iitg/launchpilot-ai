# LaunchPilot AI — Windows / Anaconda Run Guide

## 1. Extract

Extract the ZIP and open **Anaconda Prompt**.

## 2. Create a clean environment

```bat
conda create -n launchpilot python=3.12 -y
conda activate launchpilot
```

## 3. Enter the project folder

Replace the path with the folder where you extracted the project:

```bat
cd C:\Users\YOUR_NAME\Downloads\launchpilot-ai
```

Check the files:

```bat
dir
```

You should see `app.py`, `requirements.txt`, `README.md`, `core`, `data`, and `tests`.

## 4. Install dependencies

```bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Run automated tests

```bat
pytest -q
```

Expected result for this release:

```text
23 passed
```

## 6. Run Python compilation checks

```bat
python -m compileall app.py core tests
```

The command should finish without syntax errors.

## 7. Start LaunchPilot AI

```bat
streamlit run app.py
```

Open the `Local URL` shown by Streamlit, normally:

```text
http://localhost:8501
```

## 8. Verify the Risk Register fix

1. Open **3 · Risk & Trust**.
2. Confirm `Hallucinated policy answer` starts at **Likelihood 2, Impact 5, Exposure 10**.
3. Change its Likelihood to 4 and Impact to 2.
4. Confirm only that row becomes **4 × 2 = 8**.
5. Confirm the other rows keep their original values.
6. Click `+` and add a new risk.
7. Confirm the new risk appears in the calculated table.
8. Delete the new risk and confirm it disappears.
9. Click **Reset demo risks**.
10. Confirm the five seed risks return with their original values.
11. Open **5 · Executive Decision** and confirm it reflects the current live risk register.

## 9. Stop the app

In Anaconda Prompt:

```text
Ctrl + C
```

## Troubleshooting

If `pytest` or `streamlit` is not recognized, confirm the environment is active:

```bat
conda activate launchpilot
```

If Streamlit reports a missing package, run:

```bat
pip install -r requirements.txt
```

Do not commit `.env` or `.streamlit/secrets.toml` files containing secrets.
