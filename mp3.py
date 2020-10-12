# Simple MP3 player written in Python

import random

class Mp3Player:
    def __init__(self, model):
        self.model = model
        self.library = {}

    def greet(self, name):
        print(f'Hello, {name}! Welcome to your {self.model}.')

    def add(self, artist, title):
        if not artist in self.library:
            self.library[artist] = [title]
        else:
            self.library[artist].append(title)

    def remove(self, artist, title):
        self.library[artist].remove(title)

    def shuffle(self):
        shuffle = [random.choice(v) for k, v in self.library.items()]
        song = random.choice(shuffle)
        print(f'Now playing: {song}')

