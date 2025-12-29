from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random



app = Ursina()
player = FirstPersonController()
Sky()

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

# Untere Ebene: 22x22 (1 Block größer in alle Richtungen)
for x in range(-1, 21):
    for z in range(-1, 21):
        add_box((x, -1, z))

def update():
    # Finde den tiefsten Punkt der Welt (Y-Position des untersten Blocks)
    lowest_block_y = 0
    for box in boxes:
        if box.y < lowest_block_y:
            lowest_block_y = box.y
    
    # Prüfe, ob Spieler 100 Meter unter dem tiefsten Block ist
    # 1 Block = 1 Meter, also 100 Blöcke unter dem tiefsten Block
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
