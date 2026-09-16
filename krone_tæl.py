import cv2 as cv
import numpy as np
import os

margin=2


# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    image_path = r"KingDominoTestsaet\64.jpg"

    grid = []
    points = 0

    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image)
    print(len(tiles))
    for y, row in enumerate(tiles):
        row_data = []

        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print("terrain type:", get_terrain(tile))
            print("=====")
            row_data.append(get_terrain(tile))
        
        grid.append(row_data)

    terrain_types = ["Mine", "Field", "Forest", "Lake", "Grassland", "Swamp", "Home"]

    for terrain in terrain_types:
        points += count_points(grid, terrain)

    print(f"Grid: {grid}")
    print(f"Points: {points}")

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

    if (23-margin) <= hue <= (43+margin) and (40-margin) <= saturation <= (155+margin) and (29.5-margin) <= value <= (47+margin):
        return "Mine"
    if (23-margin) <= hue <= (26+margin) and (223-margin) <= saturation <= (255+margin) and (145-margin) <= value <= (205+margin):
        return "Field"
    if (23-margin) <= hue <= (66+margin) and (65-margin) <= saturation <= (222+margin) and (37-margin) <= value <= (68+margin):
        return "Forest"
    if (104-margin) <= hue <= (108+margin) and (232-margin) <= saturation <= (255+margin) and (123-margin) <= value <= (191+margin):
        return "Lake"
    if (37-margin) <= hue <= (51+margin) and (156-margin) <= saturation <= (238+margin) and (92-margin) <= value <= (166+margin):
        return "Grassland"
    if (20-margin) <= hue <= (25+margin) and (62-margin) <= saturation <= (157+margin) and (33-margin) <= value <= (130+margin):
        return "Swamp"
    if (17-margin) <= hue <= (38+margin) and (41-margin) <= saturation <= (128+margin) and (64-margin) <= value <= (123+margin):
        return "Home"
    return "Unknown"



def count_points(grid, terrain_type):
    temp_points = 0
    rows = 5

    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != terrain_type:
                continue


            has_neighbor = False
            cols = 5

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for x, y in dirs:
                new_r, new_c = r + x, c + y
                if (new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == terrain_type):
                    has_neighbor = True
                    break

            if has_neighbor:
                temp_points += 1

    return temp_points if temp_points > 1 else 0


if __name__ == "__main__":
    main()
