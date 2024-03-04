import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube


def choose_output_path():
    output_path = filedialog.askdirectory()


def download_audio():
    urls = [url_entry.get() for url_entry in url_entries]  # Retrieve URLs from all entry fields
    output_path = filedialog.askdirectory()
    try:
        downloaded = 0
        for url in urls:
            if url:
                yt = YouTube(url)
                audio = yt.streams.filter(only_audio=True).first()
                #messagebox.showinfo("Info", f"Downloading audio from {yt.title}...")
                audio.download(output_path)
                downloaded += 1
        if downloaded == len(urls):
            messagebox.showinfo("Info", "All files downloaded successfully!")
            for url_entry in url_entries:
                url_entry.delete(0, tk.END)  # Clear input boxes
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading audio: {e}")

# Create the main window
# Create the main window
root = tk.Tk()
root.title("Pointi YT Downloader")
root.configure(bg="Grey")  # Set the background color

# Define a custom font color
font_color = "white"  # Example font color: black
bg_color = "grey"    # Example background color: white

url_labels = []
url_entries = []

# Create and pack frames with custom background color
url_frame = tk.Frame(root, bg="Grey")
url_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

output_path_frame = tk.Frame(root, bg="Grey")
output_path_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Create and pack widgets with custom font color
url_labels = []
url_entries = []

for i in range(5):
    url_label = tk.Label(url_frame, text=f"YouTube URL {i+1}:", fg=font_color, bg=bg_color)
    url_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    url_labels.append(url_label)

    url_entry = tk.Entry(url_frame, width=50, fg=font_color, bg=bg_color)
    url_entry.grid(row=i, column=1, padx=5, pady=5)
    url_entries.append(url_entry)

output_path_label = tk.Label(output_path_frame, text="Output Path:", fg=font_color, bg=bg_color)
output_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

output_path_entry = tk.Entry(output_path_frame, width=50, fg=font_color, bg=bg_color)
output_path_entry.grid(row=0, column=1, padx=5, pady=5)

output_path_button = tk.Button(output_path_frame, text="Choose", command=choose_output_path, fg=font_color, bg=bg_color)
output_path_button.grid(row=0, column=2, padx=5, pady=5)

download_button = tk.Button(root, text="Download Audio", command=download_audio, fg=font_color, bg=bg_color)
download_button.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()