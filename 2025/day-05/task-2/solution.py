from os import link
import sys

def solution(input):

    fresh_ids = []
    count = 0

    for line in input:
        if line == "":
            break

        startRange, endRange = map(int, line.split("-"))
        fresh_ids.append((startRange, endRange))
        fresh_ids.sort()


    merged_ids = []
    for current_range in fresh_ids:
        if not merged_ids:
            merged_ids.append(current_range)
        else:
            last_range = merged_ids[-1]
            if current_range[0] <= last_range[1]:
                # Overlapping ranges found, merge them
                merged_ids[-1] = (last_range[0], max(last_range[1], current_range[1]))
            else:
                merged_ids.append(current_range)

    for merged_range in merged_ids:
        count += merged_range[1] - merged_range[0] + 1

    return count

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = [line.strip() for line in f]

    result = solution(input_data)
    
    with open('../task2.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")