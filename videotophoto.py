import os
import cv2
import tkinter as tk
from tkinter import filedialog
from datetime import datetime


def choose_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Video File")
    return file_path


def get_output_folder():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")

    # Create the "Output" folder with the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_folder = os.path.join(home_dir, "Downloads", f"Output_{current_time}")

    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    return output_folder


# Prompt the user to choose the video file
video_path = choose_video_file()

# Get the path to the output folder
output_folder = get_output_folder()

# Prompt the user to choose the number of photos
num_photos = int(input("Enter the number of photos to extract: "))

# Open the video file
video = cv2.VideoCapture(video_path)

# Calculate the total number of frames in the video
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Calculate the interval between frames
frame_interval = total_frames // num_photos

# Initialize counters
current_frame = 0
current_photo = 1

while current_frame < total_frames and current_photo <= num_photos:
    # Read the next frame from the video
    success, frame = video.read()

    if success:
        # Save the frame as an image
        photo_path = os.path.join(output_folder, f"photo{current_photo}.jpg")
        cv2.imwrite(photo_path, frame)
        print(f"Saved {photo_path}")

        # Increment counters
        current_frame += frame_interval
        current_photo += 1

        # Set the video position to the next frame
        video.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    else:
        # Unable to read the frame, break the loop
        break

# Release the video object
video.release()