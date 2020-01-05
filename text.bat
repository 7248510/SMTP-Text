@echo off
cd directoryofthescript
REM (To time the execution of a script you can delay is via the TIMEOUT command.) (5 second delay) TIMEOUT /T 5 /NOBREAK
python text.py
REM (Python must be added to your path)