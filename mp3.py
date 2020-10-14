# Simple CLI MP3 player written in Python

import random
from time import sleep

class Mp3Player:
    def __init__(self, owner, model):
        self.owner = owner
        self.model = model
        self.library = {}
    
    def greet(self):
        print(f'Hello, {self.owner}! Welcome to your {self.model}')
        print("What would you like to do?")

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

print("Turning on your device...")
sleep(2)
print("What is your name?")
name = input()
print("Which device are you using?")
model = input()

mp3 = Mp3Player(name, model)
mp3.greet()
