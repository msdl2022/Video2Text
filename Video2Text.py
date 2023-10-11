import os
from moviepy.editor import VideoFileClip

# Function to extract audio and save it to a text file
def extract_audio_to_txt(video_path, txt_path):
    try:
        # Load the video file
        video_clip = VideoFileClip(video_path)
        
        # Extract audio
        audio = video_clip.audio.to_soundarray()
        
        # Convert audio to text (replace this part with your desired audio-to-text processing)
        audio_text = "This is where you can implement your audio-to-text processing."
        
        # Save the text to a file
        with open(txt_path, 'w') as txt_file:
            txt_file.write(audio_text)
    except Exception as e:
        print(f"Error processing {video_path}: {e}")

# Directory containing video files
video_directory = 'path_to_video_directory'

# Output directory for text files
output_directory = 'output_text_files_directory'

# List of video formats to consider
video_formats = ['.mp3', '.mkv', '.avi']

# Iterate through the video directory and process the video files
for root, dirs, files in os.walk(video_directory):
    for file in files:
        if os.path.splitext(file)[1] in video_formats:
            video_path = os.path.join(root, file)
            txt_filename = os.path.splitext(file)[0] + '.txt'
            txt_path = os.path.join(output_directory, txt_filename)
            extract_audio_to_txt(video_path, txt_path)
            print(f"Processed {video_path} and saved audio text to {txt_path}")
