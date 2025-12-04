import sys

def solution(input):
    total = 0

    for x in range(0, len(input)):
        for y in range(0, len(input[x])):
            if input[x][y] == '@':
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        if 0 <= x + dx < len(input) and 0 <= y + dy < len(input[x + dx]):
                            if input[x + dx][y + dy] == '@':
                                count += 1

                if count < 4:
                    total += 1

    return total

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = [list(line.strip()) for line in f if line.strip()]

    result = solution(input_data)
    
    with open('../output.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")