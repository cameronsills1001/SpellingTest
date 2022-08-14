__author__ = 'cameron'

import pygame

class Player:

    def phrase_player(self, file):
        #uses pygame to play mp3 files
        self.file = file
        #the pre_init was set because pygame played file too fast
        pygame.mixer.pre_init(16384)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)



