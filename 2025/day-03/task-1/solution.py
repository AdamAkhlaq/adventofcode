import sys

def solution(input):

    total_output_joltage = 0

    for line in input:
        batteries = [int(digit) for digit in line]
        
        first_battery = max(batteries[:-1]) # Don't check last battery
        first_battery_pos = batteries.index(first_battery)

        second_battery = max(batteries[first_battery_pos + 1:])

        total_output_joltage += int(f"{first_battery}{second_battery}")
        print(f"First battery: {first_battery}, Second battery: {second_battery}")

    return total_output_joltage

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = [line.strip() for line in f if line.strip()]
    
    result = solution(input_data)
    
    with open('../task1.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")