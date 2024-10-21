from moviepy.editor import VideoFileClip

# Load the video file
video_path = 'input_video.mp4'  # Replace with your video file path
output_gif_path = 'output_animation.gif'  # Output GIF file

# Load the video
clip = VideoFileClip(video_path)

# Optionally, you can reduce the size of the video by specifying a percentage (e.g., 0.5 for half size)
clip_resized = clip.resize(0.5)  # Adjust this as needed

# Convert to GIF
clip_resized.write_gif(output_gif_path)

print(f"GIF saved as {output_gif_path}") 
