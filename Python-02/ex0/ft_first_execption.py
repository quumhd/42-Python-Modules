#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None:
    try:
        temp = (int(temp_str))
    except ValueError:
        print(f"Error '{temp_str}' is not a number")
    else:
        if temp > 40:
            print(f"Error: {temp}℃ is to hot for the plants (max 40℃)")
        elif temp < 0:
            print(f"Error: {temp}℃ is to cold for the plants (min 0℃)")
        else:
            print(f"Temperature {temp}℃  is perfect for the plants!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing with temperature: fail")
    check_temperature("fail")
    print()
    print("Testing with temperature: 55")
    check_temperature("55")
    print()
    print("Testing with temperature: -15")
    check_temperature("-15")
    print()
    print("Testing with temeprature: 15")
    check_temperature("15")
    print()
    print("All tests completed!")
