#!/bin/bash
if [ ! -d "venv" ]; then
	python3 -m venv venv
fi
source venv/bin/activate
pip install telethon cryptg >/dev/null 2>&1
python main.py
