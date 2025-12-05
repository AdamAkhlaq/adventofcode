import sys

def solution(input):

    fresh_ids = []
    all_ids_read = False
    count = 0

    for line in input:
        if line == "":
            all_ids_read = True

        elif not all_ids_read:
            startRange, endRange = map(int, line.split("-"))
            fresh_ids.append((startRange, endRange))

        elif all_ids_read:
            if any(start <= int(line) <= end for start, end in fresh_ids):
                count += 1
           
    return count

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = [line.strip() for line in f]

    result = solution(input_data)
    
    with open('../task1.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")