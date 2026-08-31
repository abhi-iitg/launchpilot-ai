@echo off
setlocal
call conda activate launchpilot
if errorlevel 1 (
  echo Could not activate the launchpilot conda environment.
  echo Create it first with: conda create -n launchpilot python=3.12 -y
  pause
  exit /b 1
)
cd /d "%~dp0"
streamlit run app.py
