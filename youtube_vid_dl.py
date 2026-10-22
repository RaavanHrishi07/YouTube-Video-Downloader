
import re
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from pytube import YouTube


DOWNLOAD_DIR = Path("downloads")

YOUTUBE_URL_PATTERN = re.compile(
    r"^(?:https?://)?(?:www\.)?"
    r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)"
    r"[\w-]{11}(?:[?&][^\s]*)?$"
)


def is_valid_youtube_url(url):
    """Return True if the URL matches a supported YouTube video format."""
    return bool(YOUTUBE_URL_PATTERN.fullmatch(url.strip()))


def download_video(url, output_dir=DOWNLOAD_DIR, progress_callback=None):
    """Download a progressive MP4 video and return its saved path."""
    if not is_valid_youtube_url(url):
        raise ValueError("Please enter a valid YouTube video URL.")

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    video = YouTube(url, on_progress_callback=progress_callback)
    stream = (
        video.streams
        .filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
    )

    if stream is None:
        raise RuntimeError("No suitable MP4 video stream was found.")

    return Path(stream.download(output_path=str(output_dir)))


def main():
    root = tk.Tk()
    root.geometry("700x320")
    root.resizable(False, False)
    root.title("YouTube Video Downloader")

    tk.Label(
        root,
        text="Copy the link of the video you want to download from YouTube",
        font=("Arial", 13, "bold"),
        wraplength=660,
    ).pack(pady=(20, 10))

    link_var = tk.StringVar()
    status_var = tk.StringVar(value="Ready")

    tk.Label(
        root, text="Paste Link Here:", font=("Arial", 12, "bold")
    ).pack()
    tk.Entry(root, width=75, textvariable=link_var).pack(
        padx=20, pady=10
    )

    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize or stream.filesize_approx
        if total_size:
            downloaded = total_size - bytes_remaining
            percent = downloaded / total_size * 100
            status_var.set(f"Downloading... {percent:.1f}%")
            root.update_idletasks()

    def on_download_click():
        url = link_var.get().strip()

        if not url:
            messagebox.showwarning(
                "Missing URL", "Please enter a YouTube video URL."
            )
            return

        if not is_valid_youtube_url(url):
            messagebox.showerror(
                "Invalid URL", "Please enter a valid YouTube video URL."
            )
            return

        download_button.config(state=tk.DISABLED)
        status_var.set("Preparing download...")
        root.update_idletasks()

        try:
            saved_path = download_video(
                url, progress_callback=on_progress
            )
            status_var.set("Download completed!")
            messagebox.showinfo(
                "Success", f"Video saved to:\n{saved_path.resolve()}"
            )
        except Exception as error:
            status_var.set("Download failed.")
            messagebox.showerror(
                "Download Error", f"Could not download the video:\n\n{error}"
            )
        finally:
            download_button.config(state=tk.NORMAL)

    download_button = tk.Button(
        root,
        text="DOWNLOAD",
        font=("Arial", 13, "bold"),
        bg="white",
        command=on_download_click,
    )
    download_button.pack(pady=10)

    tk.Label(root, textvariable=status_var, font=("Arial", 10)).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
