import cv2 as cv
import numpy as np
import os

margin=2
image_number=73
# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = rf"King Domino dataset\{image_number}.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
    print(len(tiles))
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print(get_terrain(tile))
            print("=====")
            with open(f"answer{image_number}.txt", "a") as f:
                f.write(str(get_terrain(tile)) + "\n")

# Break a board into tiles
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100])
    return tiles

# Determine the type of terrain in a tile
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.median(hsv_tile, axis=(0,1))
    print(f"H: {hue}, S: {saturation}, V: {value}")

    
    if (23-margin) <= hue <= (26+margin) and (223-margin) <= saturation <= (255+margin) and (145-margin) <= value <= (205+margin):
        return "Field"
    if (23-margin) <= hue <= (66+margin) and (65-margin) <= saturation <= (222+margin) and (34-margin) <= value <= (68+margin):
        return "Forest"
    if (104-margin) <= hue <= (108+margin) and (232-margin) <= saturation <= (255+margin) and (116-margin) <= value <= (191+margin):
        return "Lake"
    if (34-margin) <= hue <= (51+margin) and (156-margin) <= saturation <= (247+margin) and (92-margin) <= value <= (166+margin):
        return "Grassland"
    if (20-margin) <= hue <= (43+margin) and (34-margin) <= saturation <= (155+margin) and (28-margin) <= value <= (64+margin):
        return "Mine"
    if (17-margin) <= hue <= (25+margin) and (23-margin) <= saturation <= (161+margin) and (33-margin) <= value <= (142+margin):
        return "Swamp"
    if (17-margin) <= hue <= (87+margin) and (41-margin) <= saturation <= (194+margin) and (61-margin) <= value <= (123+margin):
        return "Home"
    return "Unknown"



if __name__ == "__main__":
    main()

