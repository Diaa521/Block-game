from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random


app = Ursina()
player = FirstPersonController()
Sky() # With these simple code block, you can create the sky.
player.position = (10, 100, 10)
boxes = []

def random_color():
    return color.rgb(random.random(), random.random(), random.random())

def add_box(position):
    box = Entity(
        parent=scene,
        model='cube',
        origin=(0,0,0),
        color=random_color(),
        position=position,
        texture='grass',
        collider='box'
    )
    boxes.append(box)

# Obere Ebene: 20x20
for x in range(20):
    for z in range(20):
        add_box((x, 0, z))

# Lower level: 22x22 (1 block larger in all directions)
for x in range(-1, 21):
    for z in range(-1, 21):
        add_box((x, -1, z))

def update():
    # Find the lowest point in the world (Y-position of the lowest block)
    lowest_block_y = 0
    for box in boxes:
        if box.y < lowest_block_y:
            lowest_block_y = box.y
    
    # Check if the player is 100 meters below the lowest block.
    # 1 block = 1 meter, so 100 blocks below the lowest block
    if player.y < lowest_block_y - 100:
        player.position = (10, 100, 10)
        print(f"Spieler war bei Y={player.y}, tiefster Block bei Y={lowest_block_y}")
        print("Spieler wurde 100 Meter über dem Boden gespawnt!")

def input(key):
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                add_box(box.position + mouse.normal)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)

app.run()
