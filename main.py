# Importing necessary libraries
from pytube import YouTube  # Import YouTube class from pytube module
import tkinter as tk  # Import tkinter for GUI
from tkinter import filedialog  # Import filedialog from tkinter for selecting download location

# Function to download video
def download_video(url, save_path):
    try:
        yt = YouTube(url)  # Create a YouTube object
        streams = yt.streams.filter(progressive=True, file_extension="mp4")  # Filter for progressive streams with mp4 extension
        highest_res_stream = streams.get_highest_resolution()  # Get the highest resolution stream
        highest_res_stream.download(output_path=save_path)  # Download the video to specified directory
        print("Video downloaded successfully!")  # Print success message
    except Exception as e:
        print(e)  # Print any exception that occurs

# Function to open file dialog for selecting download location
def open_file_dialog():
    folder = filedialog.askdirectory()  # Open file dialog to select directory
    if folder:
        print(f"Selected folder: {folder}")  # Print selected folder
    return folder  # Return selected folder

# Main function
if __name__ == "__main__":
    root = tk.Tk()  # Create Tkinter window
    root.withdraw()  # Hide the window

    video_url = input("Please enter a YouTube URL: ")  # Ask user for YouTube URL
    save_dir = open_file_dialog()  # Open file dialog to select download location

    if save_dir:  # If valid save directory selected
        download_video(video_url, save_dir)  # Download the video
        print("Started download...")  # Print message indicating download has started
    else:
        print("Invalid save location.")  # Print message indicating invalid save location
