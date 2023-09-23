from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from random import random

from ground import Ground
from player import Player
from snowflake import SnowFlake

#If the player walks a lot
def update():                           
   if(abs(player.x) > 100 or abs(player.z) > 100):
            Text(text='it\'s snowing')
   if (abs(player.x) > 101 or abs(player.z) > 101):
         snowstorm_sound.stop()

#just escape
def input(key):
    if key == "escape":
        quit()

#window settings
app = Ursina(
    title = "it's snowing",
    fullscreen = True,
    development_mode = False
    )

player = Player()

#3x3 ground planes
ground_objects = []
for x in range(-1,2):
    for z in range(-1,2):
        ground_objects.append(Ground(x,z, player))

#500 snow flakes
for count in range(0,500):
    flake = SnowFlake(player)

#some settings of scene
fog_color = color.rgb(61,66,89)
Sky(color=fog_color, texture="textures\white")
scene.default_shader = lit_with_shadows_shader
scene.fog_density = .35
scene.fog_color = fog_color

snowstorm_sound = Audio("sounds\snowstorm.mp3", autoplay = True, loop = True, pitch = random())

#run!
app.run()