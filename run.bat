@echo off
if not exist "venv" (
    python -m venv venv
)
call venv\Scripts\activate
pip install telethon cryptg >nul 2>&1
python main.py

