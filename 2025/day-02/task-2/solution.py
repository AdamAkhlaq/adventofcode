import sys

def solution(input):
    ranges = input.split(',')
    count = 0


    for r in ranges:
        start, end = map(int, r.split('-'))
        for id in range(start, end + 1):
            s = str(id)
            length = len(s)

            # Check if the ID is made up of digits repeated by its length factors, e.g. length of 12 = 12x1 repeated digit, 6x2 repeated digits, or 4x3 repeated digits
            for pattern_length in range(1, length // 2 + 1):
                if length % pattern_length == 0:
                    pattern = s[:pattern_length]
                    repetitions = length // pattern_length

                    if pattern * repetitions == s:
                        count += id
                        break # Stop duplicate checks for numbers with the same pattern e.g. 222222
  
    return count

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
    
    result = solution(input_data)

    with open('../task2.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")
