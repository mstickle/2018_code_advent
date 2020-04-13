#!/usr/bin/python3
import argparse
import re
import time

def part_one(data):
    # Create guard log with id, tot time asleep, and max min asleep
    guard_log = {'guard_id': None, 'tot_time': 0, 'max_min': 0}
    for i, string in enumerate(data):
        if "Guard" in string:
            guard_id = [id_num for id_num in re.findall(r'#(\d+)', string)].pop()
            # Check if id is already in log
            if guard_id not in guard_log.keys():
                guard_log[guard_id] = {
                    'tot_time': 0,
                    'tally': [0 for min in range(60)],
                    'max_min': 0,
                    'min_count': 0
                }
        elif "asleep" in string:
            # Get start and end time
            start_time = [time for time in re.findall(r'(\d+):(\d+)', string)].pop()
            start = int(start_time[1])
            end_time = [time for time in re.findall(r'(\d+):(\d+)', data[i+1])].pop()
            end = int(end_time[1])
            # Update tot_time
            guard_log[guard_id]['tot_time'] += (end - start)
            # Update tally
            current_tally = guard_log[guard_id]['tally']
            for minute in range(start, end):
                current_tally[minute] += 1
            guard_log[guard_id]['tally'] = current_tally
            guard_log[guard_id]['max_min'] = current_tally.index(max(current_tally))
            guard_log[guard_id]['min_count'] = max(current_tally)

            # Update info on sleepiest guard
            if guard_log[guard_id]['tot_time'] > guard_log['tot_time']:
                guard_log['guard_id'] = guard_id
                guard_log['tot_time'] = guard_log[guard_id]['tot_time']
                guard_log['max_min'] = guard_log[guard_id]['max_min']
    return guard_log

def part_two(guard_log):
    # Find guard who slept the longest on any given minute
    sleep_log = {'guard_id': None, 'max_min': 0, 'min_count': 0}
    for k in guard_log.keys():
        if 'guard_id' in k or 'tot_time' in k or 'max_min' in k:
            # Skip info on all guards
            continue
        if guard_log[k]['min_count'] > sleep_log['min_count']:
            # Check if current guard slept more than current max
            sleep_log = {
                'guard_id': int(k),
                'max_min': guard_log[k]['max_min'],
                'min_count': guard_log[k]['min_count']
            }
    # Return guard id * max min of sleepiest guard
    return sleep_log['guard_id'] * sleep_log['max_min']

if __name__ == '__main__':
    start_time = time.time()
    parser = argparse.ArgumentParser(description = '2018 D4 Code Advent')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        data = list(f)
    # Sort data and parse info
    data.sort()
    # Get log on guards that fell asleep
    guard_log = part_one(data)
    p1_ans = int(guard_log['guard_id']) * guard_log['max_min']
    p2_ans = part_two(guard_log)
    print(f'Part one results: {p1_ans}\nPart two results: {p2_ans}')
    print("--- %s seconds ---" % (time.time() - start_time))