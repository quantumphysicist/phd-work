import os
import sys

# Try to import pydub; if unavailable, instruct the user to switch environments
try:
    from pydub import AudioSegment
except ImportError:
    print('Please switch to the "digital" environment using conda (pydub is not installed here).')
    sys.exit()

# Recommend using ffmpeg + GPU before proceeding
print(
    '\nNote: For fastest and highest-quality conversion, you may prefer to use FFMPEG directly:\n'
    '    ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "INPUT.mp4" -vn -acodec libmp3lame -q:a 2 "OUTPUT.mp3"\n'
)

choice = input("Would you like to continue with the PyDub conversion instead? (y/n): ").strip().lower()
if choice not in ("y", "yes"):
    print("Exiting without conversion.")
    sys.exit()

# Find the first .mp4 file in the current working directory
mp4_file = None
for file in os.listdir('.'):
    if file.endswith('.mp4'):
        mp4_file = file
        break

if mp4_file is not None:
    # Set the output .mp3 filename
    mp3_filename = mp4_file.replace('.mp4', '.mp3')

    # Convert .mp4 to .mp3 using PyDub
    track = AudioSegment.from_file(mp4_file, format='mp4')
    track.export(mp3_filename, format='mp3')
    print(f'Successfully converted {mp4_file} to {mp3_filename}')
else:
    print('No .mp4 files found in the current working directory')
