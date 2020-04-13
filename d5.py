#!/usr/bin/python3
import string
import argparse

def part_1(polymer):
    # Fully react polymer and return shortened polymer
    # Units are destroyed if chars are opposite polarity
    # ex: aA reacts, but aa and AA does not
    c = 0
    polymer_len = len(polymer)
    while c < polymer_len - 1:
        # Go through polymer
        current_char = polymer[c]
        next_char = polymer[c + 1]
        if (current_char != next_char 
                and current_char.lower() == next_char.lower()):
            # If current char and next char are not equal, but equal after case change
            # Remove next car and continue
            polymer = polymer[:c] + polymer[c+2:]
            if c < 1:
                c = 0
            else:
                c -= 1
            polymer_len = len(polymer)
        else:
            c += 1
    return polymer

def part_2(polymer):
    # Find min polymer by removing bad unit preventing full reaction
    lower_case = string.ascii_lowercase
    min_length = len(polymer)
    for letter in lower_case:
        # Go through alphabet and remove that letter instance from polymer
        new_polymer = polymer.replace(letter, "")
        new_polymer = new_polymer.replace(letter.upper(), "")
        shortened_polymer = part_1(new_polymer)
        if len(shortened_polymer) < min_length:
            # Update min length
            min_length = len(shortened_polymer)
    return min_length

if __name__ == '__main__':
    # Set up command line parameter for filename
    parser = argparse.ArgumentParser(description = '2018 D5 Code Advent')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        data = f.read()
    shortened_polymer = part_1(data)
    p1_ans = len(shortened_polymer)
    p2_ans = part_2(shortened_polymer)
    print(f'Part one results: {p1_ans}\nPart two results: {p2_ans}')