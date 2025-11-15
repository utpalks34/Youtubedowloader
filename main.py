import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
import threading

def download_video():
    url = url_entry.get()

    if not url.strip():
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        yt = YouTube(url)

        # Update status
        status_label.config(text="Fetching video details...")

        stream = yt.streams.get_highest_resolution()

        # Ask user for download location
        folder = filedialog.askdirectory()
        if not folder:
            return

        status_label.config(text="Downloading... please wait")

        stream.download(output_path=folder)

        status_label.config(text="Download Completed ✔")
        messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")
        status_label.config(text="")

def start_download_thread():
    thread = threading.Thread(target=download_video)
    thread.start()

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")

title_label = tk.Label(root, text="YouTube Video Downloader", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12))
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

download_btn = tk.Button(root, text="Download Video", font=("Arial", 12), bg="#008CBA", fg="white",
                         command=start_download_thread)
download_btn.pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
status_label.pack(pady=10)

root.mainloop()
