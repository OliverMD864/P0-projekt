import cv2 as cv
import numpy as np
import os

# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")

    folder_path = r"King Domino dataset"
    folderLen = len(os.listdir(folder_path))

    for file in range(1, folderLen + 1):
        image_path = fr"{folder_path}\{file}.jpg"

        if not os.path.isfile(image_path):
            print(f"Image {file} not found")
            continue
        image = cv.imread(image_path)
        tiles = get_tiles(image)

        print(len(tiles))

        if not process_tiles(tiles):
            print(f"Stopped at file {file} due to Unknown terrain")
            break


def process_tiles(tiles):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            terrain = get_terrain(tile)
            if terrain == "Unknown":
                return False  # signal: stop everything
            print(f"Tile ({x}, {y}):")
            print(terrain)
            print("=====")
    return True  # finished without hitting Unknown


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
    if 26.3026 <= hue <= 26.3026 and 245.1842 <= saturation <= 245.1842 and 191.1801 <= value <= 191.1801:
        return "Field"
    if 36.5725 <= hue <= 48.1779 and 100.3718 <= saturation <= 172.7378 and 60.6874 <= value <= 70.603:
        return "Forest"
    if 78.9684 <= hue <= 101.9646 and 193.0165 <= saturation <= 239.8913 and 139.3264 <= value <= 176.1833:
        return "Lake"
    if 32.4253 <= hue <= 43.3704 and 191.8896 <= saturation <= 219.9982 and 123.546 <= value <= 151.1209:
        return "Grassland"
    if 23.7077 <= hue <= 24.3891 and 132.757 <= saturation <= 134.6243 and 107.1856 <= value <= 111.7854:
        return "Swamp"
    if 0 <= hue <= 0 and 0 <= saturation <= 0 and 0 <= value <= 0:
        return "Mine"
    if 28.5602 <= hue <= 28.5602 and 110.4772 <= saturation <= 110.4772 and 139.92550 <= value <= 139.9255:
        return "Home"
    return "Unknown"

if __name__ == "__main__":
    main()