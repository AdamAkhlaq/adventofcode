import sys

def solution(input):
    ranges = input.split(',')
    count = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for id in range(start, end + 1):
            # Check if the ID is made up of the same digits repeated twice
            if str(id) == str(id)[0:len(str(id))//2] * 2:
                count += id

    return count

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
    
    result = solution(input_data)

    with open('../task1.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")