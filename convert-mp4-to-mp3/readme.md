# MP4-to-MP3 Conversion Script

A simple Python utility for converting `.mp4` files to `.mp3` audio. The script:

1. Attempts to import **PyDub**.
2. If the import fails, it instructs the user to switch to the correct conda environment.
3. Recommends using a **GPU-accelerated ffmpeg command** for maximum performance.
4. Gives the user the option to **continue with PyDub** or **exit**.
5. Automatically finds the first `.mp4` file in the current directory and converts it to `.mp3`.

---

## Features

* Environment-aware: instructs the user to activate the correct conda environment (“digital”) if PyDub is unavailable.
* Optional early-exit path, allowing the user to switch to a more efficient ffmpeg-based workflow.
* Automatic detection of the first `.mp4` file in the working directory.
* Conversion handled using **PyDub**, which internally relies on ffmpeg.

---

## Recommended Conversion (Fastest Method)

For high-quality and GPU-accelerated conversion, it is recommended to use ffmpeg directly:

```
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "INPUT.mp4" -vn -acodec libmp3lame -q:a 2 "OUTPUT.mp3"
```

This bypasses Python entirely and typically delivers **significantly faster** processing when a CUDA-capable GPU is available.

---

## Python-Based Conversion (PyDub)

If you choose to continue with the Python script, it will:

1. Confirm that PyDub is available.
2. Ask whether you want to continue with PyDub instead of ffmpeg.
3. Locate the first `.mp4` file in the current directory.
4. Convert it to `.mp3` using PyDub.

---

## Requirements

### Python Dependencies

* Python 3.8+
* `pydub`
* `ffmpeg` installed on your system and available in PATH

### Conda Environment

The script assumes you have a conda environment named **digital** that contains PyDub.
If the import fails, the script prints:

```
Please switch to the "digital" environment using conda (pydub is not installed here).
```

You can activate this environment using:

```
conda activate digital
```

---

## Usage

1. Place your `.mp4` file in the same directory as the script.
2. Run the script:

```
python convert.py
```

3. When prompted:

   * Enter **y** to use PyDub for conversion.
   * Enter **n** to exit and use the ffmpeg command manually instead.

4. If you proceed, the script will generate an `.mp3` file with the same base name.

---

## Example Output

```
Note: For fastest and highest-quality conversion, you may prefer to use FFMPEG directly:
    ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "INPUT.mp4" -vn -acodec libmp3lame -q:a 2 "OUTPUT.mp3"

Would you like to continue with the PyDub conversion instead? (y/n): y
Successfully converted example.mp4 to example.mp3
```

---

## Troubleshooting

### PyDub import error

You are not in the correct conda environment. Run:

```
conda activate digital
```

### No .mp4 files found

Ensure your input file is in the same directory as the script.

### ffmpeg not found

Install via:

* Conda: `conda install -c conda-forge ffmpeg`
* Homebrew (macOS): `brew install ffmpeg`
* Windows: Install from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add to PATH.

---

## Licence

MIT Licence.

---

If you want, I can also generate a `convert.bat` file for easy one-click launching, or a conda environment file (`environment.yml`) for reproducibility.
