
# YouTube Video Downloader

A Python desktop application built with Tkinter that provides a simple graphical interface for downloading YouTube videos.

## Features

- Simple and easy-to-use graphical interface.
- Supports common YouTube video URL formats.
- Validates URLs before starting a download.
- Downloads progressive MP4 video streams.
- Displays download progress.
- Shows success and error messages.
- Saves downloaded videos in a dedicated `downloads` folder.
- Includes automated tests using pytest.

## Tech Stack

- Python 3.11+
- Tkinter
- pytube
- pytest

## Project Structure

```text
YouTube-Video-Downloader/
├── youtube_vid_dl.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_youtube_vid_dl.py
```

## Prerequisites

- Python 3.11 or newer
- pip

Tkinter is included with many standard Python installations.

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/RaavanHrishi07/YouTube-Video-Downloader.git
cd YouTube-Video-Downloader
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Run the Application

Start the graphical interface with:

```powershell
python .\youtube_vid_dl.py
```

Paste a supported YouTube video URL into the input field and click **DOWNLOAD**. Downloaded files are saved in the `downloads` directory.

## Run Tests

Run the automated test suite from the project root:

```powershell
python -m pytest -v
```

The tests cover supported URL formats, invalid URLs, and URLs with surrounding whitespace.

## Limitations

- Download availability depends on the source video, network connection, and `pytube` compatibility.
- The application currently selects a progressive MP4 stream, which may limit available video resolutions.
- URL validation checks the URL format; it does not guarantee that a video exists or is accessible.

## Responsible Use

Only download content you own or are authorised to download. Follow applicable copyright laws and YouTube's terms.

## Author

**Hrishikesh Sharma**

- GitHub: [@RaavanHrishi07](https://github.com/RaavanHrishi07)
- Repository: [YouTube Video Downloader](https://github.com/RaavanHrishi07/YouTube-Video-Downloader)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
