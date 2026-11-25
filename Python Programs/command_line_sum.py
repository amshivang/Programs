# Command-line sum of integer arguments using sys.argv[]
import sys

args = sys.argv[1:]

if not args:
    print("Usage: python command_line_sum.py <num1> <num2> ...")
    print("Example calculation (10, 20, 30):", sum([10, 20, 30]))
else:
    try:
        total = sum(int(x) for x in args)
        print("Sum of command-line arguments:", total)
    except ValueError:
        print("Error: All command-line arguments must be integers.")
