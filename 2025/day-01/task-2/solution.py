import sys

def solution(input):

    DIAL_POS = 50 # Starting position
    count = 0

    for instruction in input:
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'L':
            count += abs(DIAL_POS - distance) // 100 + (DIAL_POS != 0 and DIAL_POS <= distance)
            DIAL_POS = (DIAL_POS - distance) % 100

        elif direction == 'R':
            count += (DIAL_POS + distance) // 100
            DIAL_POS = (DIAL_POS + distance) % 100

    return count

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = [line.strip() for line in f if line.strip()]
    
    result = solution(input_data)
    
    with open('output.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")
