# pip install moviepy

from moviepy.editor import VideoFileClip

# Define the path to the video file
video_path = "path/to/video/file.mp4"

# Create a VideoFileClip object
video_clip = VideoFileClip(video_path)

# Extract the audio from the video
audio_clip = video_clip.audio

# Define the output audio file path
output_audio_path = "path/to/output/audio/file.mp3"

# Write the audio to the output file
audio_clip.write_audiofile(output_audio_path)

# Close the clips
video_clip.close()
audio_clip.close()

print("Audio extracted successfully!")

