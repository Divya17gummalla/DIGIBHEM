import pygame

class Song:
    def __init__(self, file_path):
        self.file_path = file_path
        pygame.mixer.init()
        pygame.mixer.music.load(self.file_path)
        
    def play(self):
        pygame.mixer.music.play()
        
    def stop(self):
        pygame.mixer.music.stop()
