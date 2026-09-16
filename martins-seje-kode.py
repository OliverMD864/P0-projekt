import cv2 as cv
import numpy as np
import os

margin=0.05

# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"KingDominoTestsaet\4.jpg"
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
    hue, saturation, value = np.mean(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    if (21.1051-margin) <= hue <= (29.3502+margin) and (200.7676-margin) <= saturation <= (252.1913+margin) and (134.2711-margin) <= value <= (198.6451+margin):
        return "Field"
    if (27.7865-margin) <= hue <= (61.4561+margin) and (64.4392-margin) <= saturation <= (207.1959+margin) and (41.4891-margin) <= value <= (68.7333+margin):
        return "Forest"
    if (44.2007-margin) <= hue <= (107.9628+margin) and (95.1138-margin) <= saturation <= (252.0427+margin) and (51.0296-margin) <= value <= (188.1554+margin):
        return "Lake"
    if (31.9257-margin) <= hue <= (50.9094+margin) and (144.6177-margin) <= saturation <= (219.5125+margin) and (90.9712-margin) <= value <= (155.5490+margin):
        return "Grassland"
    if (20.1137-margin) <= hue <= (38.3629+margin) and (68.9848-margin) <= saturation <= (158.7524+margin) and (72.2139-margin) <= value <= (126.0819+margin):
        return "Swamp"
    if (28.3604-margin) <= hue <= (57.9104+margin) and (63.1033-margin) <= saturation <= (151.4930+margin) and (45.8882-margin) <= value <= (79.8493+margin):
        return "Mine"
    if (0-margin) <= hue <= (0+margin) and (0-margin) <= saturation <= (0+margin) and (0-margin) <= value <= (0+margin):
        return "Home"
    return "Unknown"

if __name__ == "__main__":
    main()