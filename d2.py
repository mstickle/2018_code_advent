#!/usr/bin/python3
import argparse

def part_one(data):
    # Calculate check sum for pairs and triplets of chars
    total_pairs = 0
    total_triples = 0
    for line in data:
        char_dict = dict()
        for char in line:
            if char in char_dict:
                # Add count to exisiting char in line
                char_dict[char] += 1
            else:
                # Establish first count for char
                char_dict[char] = 1
        # Add pairs and triples to total count
        total_pairs += any(v == 2 for v in char_dict.values())
        total_triples += any(v == 3 for v in char_dict.values())
    # Calculate check sum
    result = total_pairs * total_triples
    return result

def part_two(data):
    # Find adjacent lines w/ exactly one diff using psuedo hamming distance
    for i, l1 in enumerate(data):
            j = i
            for l2 in data[j:]:
                difference = hamming(l1, l2)
                if difference == 1:
                    # If difference is 1, return overlap of lines
                    return str(sorted(set(l1) & set(l2), key = l1.index))

def hamming(str_1, str_2):
    # Compare strs to see how many places are not the same
    assert len(str_1) == len(str_2)
    return (sum(char_1 != char_2 for char_1, char_2 in zip(str_1, str_2)))

if __name__ == '__main__':
    # Set up command line arguments for filename
    parser = argparse.ArgumentParser(description = '2018 D2 Code Advent')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        data = list(f)
    p1_ans = part_one(data)
    p2_ans = part_two(data)
    print(f'Part one results: {p1_ans} \nPart two results: {p2_ans}')