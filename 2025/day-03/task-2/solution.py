import sys

def solution(input):

    total_output_joltage = 0

    for line in input:
        batteries = [int(digit) for digit in line]
        previous_battery_index = 0
        largest_battery_value = ""

        for i in range(12):
            remaining_picks = 12 - i
            search_end = len(batteries) - remaining_picks + 1
            
            largest_battery = batteries[previous_battery_index]
            largest_battery_index = previous_battery_index
            
            for j in range(previous_battery_index, search_end):
                if batteries[j] > largest_battery:
                    largest_battery = batteries[j]
                    largest_battery_index = j
            
            largest_battery_value += str(largest_battery)
            previous_battery_index = largest_battery_index + 1

        print(f"Final largest battery value: {largest_battery_value}")
        total_output_joltage += int(largest_battery_value)

    return total_output_joltage

if __name__ == '__main__':

    input_file = sys.argv[1] if len(sys.argv) > 1 else 'tests/input.in'
    
    with open(input_file, 'r') as f:
        input_data = [line.strip() for line in f if line.strip()]
    
    result = solution(input_data)
    
    with open('../task2.out', 'w') as f:
        f.write(str(result) + '\n')
    
    print(f"Result: {result}")