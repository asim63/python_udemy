import colorgram

colors = colorgram.extract("Day 18\hirst_image_painting.jpg", 25)
rgb_colour = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    t = (r, g, b)
    rgb_colour.append(t)
print(rgb_colour)
