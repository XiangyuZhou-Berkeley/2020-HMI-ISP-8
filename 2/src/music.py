import pygame
import os
import time
import random

def switch_music(choice):
        filepath = ""
        if choice == 1:
                num = random.randint(1,3)
                if num == 1:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\1\1.mp3"
                elif num == 2:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\1\2.mp3"
                elif num == 3:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\1\3.mp3"
        elif choice == 2:
                num = random.randint(1,3)
                if num == 1:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\2\1.mp3"
                elif num == 2:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\2\2.mp3"
                elif num == 3:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\2\3.mp3"
        elif choice == 3:
                num = random.randint(1,3)
                if num == 1:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\3\1.mp3"
                elif num == 2:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\3\2.mp3"
                elif num == 3:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\3\3.mp3"


        pygame.mixer.init()
        # 加载音乐
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(start=0.0)
        #播放时长，没有此设置，音乐不会播放，会一次性加载完
        time.sleep(15)
        pygame.mixer.music.stop()

