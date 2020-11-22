import os
import random

def switch_video(choice):
        if choice == 1:
                num = random.randint(1,3)
                if num == 1:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m1\1.mp4"
                elif num == 2:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m1\2.mp4"
                elif num == 3:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m1\3.mp4"
        elif choice == 2:
                num = random.randint(1,3)
                if num == 1:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m2\1.mp4"
                elif num == 2:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m2\2.mp4"
                elif num == 3:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m2\3.mp4"
        elif choice == 3:
                num = random.randint(1,3)
                if num == 1:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m3\1.mp4"
                elif num == 2:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m3\2.mp4"
                elif num == 3:
                        filepath= r"D:\git_projects\hiv_image\08\2\music\m3\3.mp4"

        class Video(object):
            def __init__(self,path):
             self.path = path

            def play(self):
                from os import startfile
                startfile(self.path)

        class Movie_MP4(Video):
            type = 'MP4'

        movie = Movie_MP4(filepath)
        movie.play()
