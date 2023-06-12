# import modules 
import pygame 
import time # used to control playback 

# initialize pygame 
pygame.init()

# Load mp3 file 
pygame.mixer.music.load(r"C:\Users\ADMIN\Documents\KY\PROJECTS\python_mp3\Bad_Things.mp3")

# Start playing the song
pygame.mixer.music.play()

# Add a delay 
time.sleep(60) # wait for the specified time

# Stop 
pygame.mixer_music.stop()

# Quit program 
pygame.quit()