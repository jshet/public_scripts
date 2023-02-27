from moviepy.editor import *
import time
import math

# Define constants
WIDTH = 1920
HEIGHT = 1080
FONT = 'Helvetica'
FONTSIZE = 300
MUSIC_FILE = 'background_music.mp3'
VIDEO_FILE = 'countdown.mp4'
BACKGROUND_IMAGE = 'background_image.jpg'
TIME_PER_FRAME = 1/30.0  # 30 fps

# Define function to create countdown clip
def create_countdown_clip(duration):
    # Create countdown text clips
    clips = [TextClip(str(i), fontsize=FONTSIZE, font=FONT, color='white').set_duration(1) for i in range(duration, 0, -1)]
    # Add final 'go' text clip
    clips.append(TextClip('GO!', fontsize=FONTSIZE, font=FONT, color='white').set_duration(1))
    # Concatenate clips into a single video
    return concatenate_videoclips(clips)

# Define function to create clock clip
def create_clock_clip(duration):
    # Define clock center coordinates and radius
    cx, cy = WIDTH//2, HEIGHT//2
    radius = min(WIDTH, HEIGHT) // 3

    # Define clock hand lengths
    minute_length = radius * 0.9
    second_length = radius * 0.8

    # Create clock frames
    frames = []
    for i in range(duration*30):
        # Calculate current time
        t = i/30.0
        minutes = math.floor(t/60)
        seconds = math.floor(t % 60)

        # Calculate minute and second hand angles
        minute_angle = (minutes % 60) * 6 + (seconds / 60) * 6
        second_angle = seconds * 6

        # Create clock image with minute and second hands
        clock = ImageClip('clock_face.png').resize((2*radius, 2*radius)).set_position((cx-radius, cy-radius))
        minute_hand = Line((cx, cy), (cx + minute_length * math.sin(math.radians(minute_angle)), cy - minute_length * math.cos(math.radians(minute_angle))), width=10, color='white').set_duration(TIME_PER_FRAME)
        second_hand = Line((cx, cy), (cx + second_length * math.sin(math.radians(second_angle)), cy - second_length * math.cos(math.radians(second_angle))), width=5, color='red').set_duration(TIME_PER_FRAME)
        clock_frame = CompositeVideoClip([clock, minute_hand, second_hand]).set_duration(TIME_PER_FRAME)
        frames.append(clock_frame)

    # Concatenate frames into a single video
    return concatenate_videoclips(frames)

# Create countdown clip and clock clip
countdown_clip = create_countdown_clip(5*60)
clock_clip = create_clock_clip(5*60)

# Add background music
audio = AudioFileClip(MUSIC_FILE)
countdown_clip = countdown_clip.set_audio(audio)
clock_clip = clock_clip.set_audio(audio)

# Add background image
bg_image = ImageClip(BACKGROUND_IMAGE).set_duration(countdown_clip.duration)
countdown_clip = CompositeVideoClip([bg_image, countdown_clip])
clock_clip = CompositeVideoClip([bg_image, clock_clip])

# Set video dimensions and frame rate
countdown_clip = countdown_clip.resize((WIDTH, HEIGHT)).set_fps(30)
clock_clip = clock_clip.resize((WIDTH, HEIGHT)).set_fps(30)

# Combine countdown clip and clock clip
final_clip = CompositeVideoClip([countdown_clip, clock_clip])

