# MP4 to MP3 Converter

A simple utility for converting MP4 video files to MP3 audio format using GPU-accelerated ffmpeg.

## Quick Start (Recommended)

### Using the Batch File

The easiest method - simply double-click `convert.bat`:

1. Ensure your input file is named `INPUT.mp4` (or edit the batch file with your filename)
2. Double-click `convert.bat`
3. Wait for the conversion to complete
4. Your converted audio will be saved as `OUTPUT.mp3`

The batch file uses GPU-accelerated ffmpeg with CUDA for fast, high-quality conversion:

```batch
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "INPUT.mp4" -vn -acodec libmp3lame -q:a 2 "OUTPUT.mp3"
```

**Parameters explained:**
- `-hwaccel cuda` - Use NVIDIA GPU acceleration
- `-hwaccel_output_format cuda` - Keep data on GPU
- `-vn` - Strip video, keep only audio
- `-acodec libmp3lame` - Use high-quality MP3 encoder
- `-q:a 2` - High quality audio (scale: 0-9, lower is better)

---

## Alternative Method: Python Script

If you prefer a more flexible Python-based approach, use `convert-mp4-to-mp3.py`.

### Features

- Environment checking (requires PyDub)
- Automatic detection of the first `.mp4` file in the directory
- User prompts and error handling
- Works on systems without CUDA support

### Requirements

- Python 3.8+
- PyDub: `pip install pydub` or use conda environment "digital"
- ffmpeg installed and in PATH

### Usage

```bash
python convert-mp4-to-mp3.py
```

The script will:
1. Check if PyDub is available
2. Suggest using the faster ffmpeg method
3. Allow you to continue with PyDub if you prefer
4. Find and convert the first `.mp4` file automatically

---

## Requirements

### For Batch File Method
- Windows OS
- ffmpeg installed with CUDA support
- NVIDIA GPU with CUDA drivers

### For Python Method
- Python 3.8+
- ffmpeg
- PyDub library

---

## Installation

### Install ffmpeg

**Windows:**
1. Download from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract and add to PATH
3. For CUDA support, ensure you have NVIDIA GPU drivers installed

**Conda:**
```bash
conda install -c conda-forge ffmpeg
```

### Install Python Dependencies

```bash
pip install pydub
```

Or activate the conda environment:
```bash
conda activate digital
```

---

## Troubleshooting

**Batch file doesn't run:**
- Check that ffmpeg is in your PATH: `ffmpeg -version`
- Verify CUDA drivers are installed: `nvidia-smi`
- Ensure input file is named correctly

**Python script fails:**
- Activate correct environment: `conda activate digital`
- Install PyDub: `pip install pydub`
- Verify ffmpeg is installed: `ffmpeg -version`

**No .mp4 files found:**
- Place your MP4 file in the same directory as the script
- For batch file: rename to `INPUT.mp4` or edit the batch file

---

## License

MIT License
