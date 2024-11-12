
import sys
from convert import str_to_float
def main():
    total_sum = 0.0
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number is not None:
            total_sum += number
        else:
            print(f"'{arg}' is not a valid number and will be skipped.")
    print("Sum of valid numbers:", total_sum)


if __name__ == '__main__':
    main()
