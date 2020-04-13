#!/usr/bin/python3
import argparse
import re

def part_one(data, width, height):
    # Create fabric and calculates area overlap
    fabric = create_fabric(width, height)
    area_overlap = 0
    for line in data:
        # Find coordinates in string stored in data
        coords = [pair for pair in re.findall(r'(\d+),(\d+)', line)].pop()
        # Find dimensions in string stored in data
        dims = [pair for pair in re.findall(r'(\d+)x(\d+)', line)].pop()
        for x in range(int(coords[0]), (int(coords[0]) + int(dims[0]))):
            for y in range(int(coords[1]), (int(coords[1]) + int(dims[1]))):
                if fabric[x][y] == 0:
                    # Marks fabric coordinate as visited
                    fabric[x][y] = 1
                elif fabric[x][y] == 1:
                    # Mark visited fabric square as overlap
                    fabric[x][y] = -1
                    area_overlap = area_overlap + 1
    return area_overlap

def part_two(data, width, height):
    # Create fabric and find non unique claims
    fabric = create_fabric(width, height)
    claims = set()
    non_unique_claims = set()
    for line in data:
        # Gather claim ids and add it to the set of claims
        claim = [id_num for id_num in re.findall(r'#(\d+)', line)].pop()
        claims.add(claim)
        # Find coordinates in string stored in data
        coords = [pair for pair in re.findall(r'(\d+),(\d+)', line)].pop()
        # Find dimensions in string stored in data
        dims = [pair for pair in re.findall(r'(\d+)x(\d+)', line)].pop()
        for x in range(int(coords[0]), (int(coords[0]) + int(dims[0]))):
            for y in range(int(coords[1]), (int(coords[1]) + int(dims[1]))):
                if fabric[x][y] == 0:
                    # Add claim number to unvisited fabric location
                    fabric[x][y] = claim
                elif fabric[x][y] != 0:
                    # Add claim to non unique set for visited coordinate
                    non_unique_claims.add(fabric[x][y])
                    non_unique_claims.add(claim)
    return claims.difference(non_unique_claims)

def create_fabric(w, h):
    # Create 2D grid filled with 0s
    return [[0 for x in range(w)] for y in range(h)]

if __name__ == '__main__':
    # Set up command line parameters filename, width, and height of fabric
    parser = argparse.ArgumentParser(description = '2018 D3 Code Advent')
    parser.add_argument('filename')
    parser.add_argument('width', type = int)
    parser.add_argument('height', type = int)
    args = parser.parse_args()
    with open(args.filename) as f:
        data = list(f)
    p1_ans = part_one(data, args.width, args.height)
    p2_ans = part_two(data, args.width, args.height)
    print(f'Part one results: {p1_ans} \nPart two results: {p2_ans}')