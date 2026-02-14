@echo off
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "INPUT.mp4" -vn -acodec libmp3lame -q:a 2 "OUTPUT.mp3"
pause
