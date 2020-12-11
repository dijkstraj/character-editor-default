from PIL import Image
import json

source = Image.open('roguelikeChar_transparent.png')

sprite_size = {
    'w': 16,
    'h': 16,
    'm': 1
}

def pos(size, x, y):
    return [x * (size['w'] + size['m']) + (1 if x > 1 else 0), y * (size['h'] + size['m'])]

def sprite_position(x, y):
    return pos(sprite_size, x, y)

def render_strip(name, sprites):
    strip = Image.new(source.mode, (len(sprites[0]) * 16, len(sprites) * 16), None)
    for j, sprs in enumerate(sprites):
        for i, sprite in enumerate(sprs):
            bounds_in = (sprite[0], sprite[1], sprite[0] + 16, sprite[1] + 16)
            bounds_out = (i * 16, j * 16, i * 16 + 16, j * 16 + 16)
            region = source.crop(bounds_in)
            strip.paste(region, bounds_out)
    strip.save('output/' + name + '_16.png')

output_map = {
    'size': 16,
    'sprites': {}
}

render_strip('body', [[sprite_position(i, j) for j in range(4)] for i in range(2)])
render_strip('trousers', [[sprite_position(3, i) for i in range(4)] + [sprite_position(3, i + 5) for i in range(4)]])
render_strip('shoes', [
    [sprite_position(4, i) for i in range(4)]
    + [sprite_position(4, i + 5) for i in range(4)]
    + [sprite_position(i + 3, 4) for i in range(2)]
    + [sprite_position(i + 3, 9) for i in range(2)]
])
render_strip('shirt', [[sprite_position(i + 6 + ci*4, j + cj*5) for j in range(5) for i in range(4)] for cj in range(2) for ci in range(3)])
render_strip('hair', [[sprite_position(i + 19 + ci*4, j + cj*4) for j in range(4) for i in range(4)] for cj in range(3) for ci in range(2)][:-1])
render_strip('headgear', [[sprite_position(c + 28, i) for i in range(9)] for c in range(4)])
render_strip('shield', [[sprite_position(i + 33 + ci*4, j + cj*3) for j in range(3) for i in range(4)][:-2] for cj in range(3) for ci in range(2)])
render_strip('weapon', [
    [sprite_position(c + 43, i + 6) for i in range(4)]
    + [sprite_position(i + 42, c) for i in range(4)]
    + [sprite_position(i + 47, 2 + c*2 + j) for j in range(2) for i in range(5)]
    for c in range(4)
])
