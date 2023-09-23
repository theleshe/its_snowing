from ursina import *
from random import random

class SnowFlake(Entity):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.model="quad"
        self.scale = 0.04
        self.double_sided = True
        self.texture = "textures\white"
        self.position = Vec3(random() * 5 - 5 + player.x, random() * 10, random() * 5 - 5 + player.z)
        self.rotation = Vec3(random(), random(), random())
        self.fallingSpeed = 0.06
        self.color = color.gray

    def update(self):
        self.y -= self.fallingSpeed
        self.x -= self.fallingSpeed*2
        if (self.y < 0):
            self.position = Vec3(random() * 10 - 5 + self.player.x, random() * 10, random() * 10 - 5 + self.player.z)
        if (abs(self.player.x) > 101 or abs(self.player.z) > 101):
            self.fallingSpeed = 0
            self.player.dx = 0