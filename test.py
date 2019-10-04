from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import random
import pygame
import os

class MyGrid(GridLayout):
    songList = os.listdir("music")
    pygame.mixer.init()
    shuffle = ObjectProperty(None)
    prev = ObjectProperty(None)
    next = ObjectProperty(None)
    pauseButton = ObjectProperty(None)
    shuffledFlag = False
    currentSong = songList[0]
    paused = False
    play = True
    nextSong = ''

    def shuffler(self):
        print("shufle clicked")
        if self.shuffledFlag:
            self.nextSong = random.choice(self.songList)
            while self.nextSong is self.currentSong:
                self.nextSong = random.choice(self.songList)
            else:
                pass
            pygame.mixer.music.queue(self.nextSong)
            self.shuffledFlag = False

        else:
            self.nextSong = self.songList[self.songList.index(self.currentSong)+1]
            self.shuffledFlag = True

    def pauseOrPlay(self):
        if self.play:
            pygame.mixer.music.load(f'music/{self.currentSong}')
            pygame.mixer.music.play(-1)
            if pygame.mixer.music.get_busy():
                pass
            if self.shuffledFlag:
                pygame.mixer.music.queue(f'music/{random.choice(self.songList)}')
            else:
                nextSongToPlay = self.songList[(self.songList.index(self.currentSong))+1]
                pygame.mixer.music.queue(f'music/{nextSongToPlay}')
            self.play = False

        else:
            print(self.paused)
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True

    def nextPressed(self):
        print("next pressed")
        if self.shuffledFlag:
            pygame.mixer.music.load(f'music/{random.choice(self.songList)}')
            pygame.mixer.music.play(0)
            if pygame.mixer_music.get_busy():
                pass
        else:
            songToLoad = self.songList[self.songList.index(self.currentSong)+1]
            self.currentSong = songToLoad
            pygame.mixer.music.load(f'music/{self.currentSong}')
            pygame.mixer.music.play(0)
            if pygame.mixer.music.get_busy():
                pass

    def prevPressed(self):
        print('prev pressed')
        if self.shuffledFlag:
            pygame.mixer.music.load(f'music/{random.choice(self.songList)}')
            pygame.mixer.music.play(0)
            if pygame.mixer_music.get_busy():
                pass
        else:
            songToLoad = self.songList[self.songList.index(self.currentSong)-1]
            self.currentSong = songToLoad
            pygame.mixer.music.load(f'music/{self.currentSong}')
            pygame.mixer.music.play(0)
            if pygame.mixer.music.get_busy():
                pass


class MainApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MainApp().run()