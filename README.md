# 🎬 Flet YouTube Video Downloader

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/mihaiapostol14/FletYoutubeVideoDownloader?style=for-the-badge)
![Code Quality](https://img.shields.io/badge/Code%20Quality-PEP8-orange?style=for-the-badge)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)

A lightweight, cross-platform **desktop GUI application** for downloading YouTube videos built with **Flet** and **yt-dlp**.

[**Quick Start**](#-quick-start) • [**Features**](#-features) • [**Architecture**](#-architecture) • [**Contributing**](#-contributing)

</div>

---
## Preview

<div align="center">

![Flet YouTube Video Downloader Preview](https://github.com/mihaiapostol14/FletYoutubeVideoDownloader/blob/0a28d9fa55484e4529921ffd140501217009c025/assets/preview.png)

</div>

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Flet YouTube Video Downloader** is a modern, user-friendly desktop application that enables seamless YouTube video downloading with a clean graphical interface. Built with Python's **Flet** framework for cross-platform compatibility and **yt-dlp** for robust video extraction, this tool provides an intuitive alternative to command-line downloaders.

**Key Highlights:**
- 🪟 **Cross-Platform**: Runs on Windows, macOS, and Linux
- ⚡ **Fast & Efficient**: Leverages yt-dlp's powerful extraction engine
- 🎨 **Modern UI**: Clean Flet-based interface
- 🔧 **No Complex Setup**: Single virtual environment setup

---

## ✨ Features

- 📥 **One-Click Video Downloads** - Paste YouTube URL and download instantly
- 🎯 **Intelligent Format Selection** - Automatically selects best available quality
- 📂 **Quick Output Access** - Direct button to open downloaded files
- 🛡️ **Error Handling** - Comprehensive error messages for debugging
- ⚙️ **Async Processing** - Non-blocking downloads using async/await
- 🌍 **Cross-Platform Support** - Windows, macOS, Linux compatible
- 📦 **Minimal Dependencies** - Lightweight and fast installation

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

| Requirement | Version | Download Link |
|-----------|---------|---------------|
| **Python** | 3.8 or higher | [python.org](https://www.python.org/downloads/) |
| **pip** | Latest | Included with Python |
| **Git** | Latest | [git-scm.com](https://git-scm.com/) |
| **Virtual Environment** | venv | [Python venv docs](https://mihaiapostol14.github.io/PyEnvLaunchpad/) |

> **Verify Installation:**
> ```bash
> python --version
> pip --version
> git --version
> ```

---

## 🚀 Quick Start

### Step 1: Clone Repository & Enter Directory

```bash
git clone https://github.com/mihaiapostol14/FletYoutubeVideoDownloader.git 
cd FletYoutubeVideoDownloader
```

### Step 2: Create & Activate Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

> **Virtual Environment Info:** A virtual environment isolates project dependencies and prevents conflicts with system Python packages.

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python interface.py
```

✅ The GUI window will open—paste a YouTube URL and click **Download video**!

---

## 📁 Project Structure

```
FletYoutubeVideoDownloader/
│
├── 📄 interface.py              # Main application & UI logic
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                 # Project documentation
│
├── 📂 assets/                   # Application assets
│   └── icon/
│       └── icon.ico             # Application icon
│
└── 📂 output/                   # Downloaded videos directory (auto-created)
    └── [downloaded_videos]/     # Saved video files
```

### File Descriptions

| File | Purpose |
|------|---------|
| `interface.py` | Core application logic using Flet framework and yt-dlp |
| `requirements.txt` | All required Python packages and versions |
| `assets/icon/icon.ico` | Application window icon |
| `output/` | Default directory for downloaded videos |

---

## 🏗️ Architecture

### Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **GUI Framework** | [Flet 0.86.2](https://flet.dev/) | Cross-platform desktop UI |
| **Video Extraction** | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | YouTube video downloading |
| **Server (Optional)** | FastAPI 0.139.2 | Future API integration |
| **Runtime** | Python 3.8+ | Application runtime |
| **OS Support** | Cross-platform | Windows, macOS, Linux |

### Application Flow

```
┌─────────────────────────────────────────┐
│   User Interface (Flet)                 │
│  ┌────────────────────────────────────┐ │
│  │  YouTube URL Input                 │ │
│  │  [Download Video Button]           │ │
│  │  [Open Output Button]              │ │
│  └────────────────────────────────────┘ │
└──────────────┬──────────────────────────┘
               │
        ┌──────▼──────┐
        │ Validate URL │
        └──────┬──────┘
               │
        ┌──────▼────────────┐
        │ yt-dlp Extraction │
        │ (Best Quality)    │
        └──────┬────────────┘
               │
        ┌──────▼──────┐
        │ Save Video  │
        │ /output/    │
        └──────┬──────┘
               │
        ┌──────▼─────────┐
        │ Show Success   │
        │ Message        │
        └────────────────┘
```

### Class Diagram

```python
YoutubeDownloader
├── __init__(page: ft.Page)
├── create_widgets() → None
├── download_video(e) → None
└── open_output_dir(e) → None

App
└── main(page: ft.Page) → None
```

---

## ⚙️ Configuration

### Download Settings

Edit `interface.py` to customize download behavior:

```python
ydl_opts = {
    "outtmpl": "output/%(title)s.%(ext)s",  # Output filename template
    "format": "best",                        # Video quality (best/worst/22/18)
    "quiet": False,                          # Show download progress
    "no_warnings": False,                    # Show warnings
}
```

**Format Options:**
- `"best"` - Highest quality available
- `"worst"` - Lowest quality (faster download)
- `"22"` - HD 720p
- `"18"` - Standard quality (default on most videos)

### Custom Output Directory

Change the output directory in `interface.py` line 71:

```python
"outtmpl": "your_custom_path/%(title)s.%(ext)s"
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Python not found** | Ensure Python 3.8+ is installed and added to PATH |
| **Module not found error** | Run `pip install -r requirements.txt` again |
| **"No such file" error** | Create `output/` folder manually: `mkdir output` |
| **YouTube URL not working** | Ensure URL is valid; yt-dlp may fail on age-restricted content |
| **Slow downloads** | Download format may be too high; try changing `"format"` setting |
| **Windows PowerShell venv issue** | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |

### Debug Mode

Add logging to `interface.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Fork & Clone
```bash
git clone https://github.com/YOUR_USERNAME/FletYoutubeVideoDownloader.git
cd FletYoutubeVideoDownloader
```

### Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### Make Changes & Test
```bash
python interface.py  # Test your changes
```

### Submit Pull Request
- Describe your changes clearly
- Ensure code follows PEP 8 standards
- Add screenshots if UI changes are made

---

## 📝 Code Quality Standards

This project follows:
- **PEP 8** - Python style guide
- **Type Hints** - For better code clarity
- **Error Handling** - Comprehensive exception management
- **Async/Await** - For non-blocking operations

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](./LICENSE) file for details.

MIT License allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

Requirements:
- ⚠️ Include license notice
- ⚠️ Provide source code

---

## 📞 Support & Contact

For issues, questions, or suggestions:
- 🐛 [Open an Issue](https://github.com/mihaiapostol14/FletYoutubeVideoDownloader/issues)
- 💬 [Start a Discussion](https://github.com/mihaiapostol14/FletYoutubeVideoDownloader/discussions)
- 📧 Contact: [Mihai Apostol](https://github.com/mihaiapostol14)

---

## 🙏 Acknowledgments

- [Flet Documentation](https://flet.dev/) - GUI Framework
- [yt-dlp Project](https://github.com/yt-dlp/yt-dlp) - Video Extraction Engine
- [Python Community](https://www.python.org/) - Language & Tools

---

<div align="center">

**Made with ❤️ by [Mihai Apostol](https://github.com/mihaiapostol14)**

⭐ Star this repository if you found it helpful!

[Back to Top](#-flet-youtube-video-downloader)

</div>
