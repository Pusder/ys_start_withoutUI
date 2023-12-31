import pygame


def play_music(path=r"music/提示音Ciallo.MP3"):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() is True:
        continue


if __name__ == '__main__':
    play_music()