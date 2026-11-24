@echo off
title Asset Expiry Tracker

cd /d "%~dp0"

echo Starting Asset Expiry Tracker...
echo.

python -m pip install pandas openpyxl

python asset_expiry_tracker.py

echo.
echo Program finished.
pause
