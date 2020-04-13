#!/usr/bin/python3
import argparse

def part_one(data):
    # Find total sum of frequency changes
    return sum(data)

def part_two(data):
    # Find first repeating frequency
    freq_spectrum = set()
    current_freq = 0
    while True:
        # Repeat going through list of freq changes until find repeat freq
        for freq_change in data:
            # Calculate freq with current freq change
            current_freq = current_freq + freq_change
            if current_freq not in freq_spectrum:
                # Add new freq to set
                freq_spectrum.add(current_freq)
            else:
                # Return first non unique freq
                return current_freq

if __name__ == '__main__':
    # Set up command line argument for filename
    parser = argparse.ArgumentParser(description = '2018 D1 Code Advent')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        # Convert freq changes to list of ints
        data = list(map(int, f))
    p1_ans = part_one(data)
    p2_ans = part_two(data)
    print(f'Part one results: {p1_ans} \nPart two results: {p2_ans}')