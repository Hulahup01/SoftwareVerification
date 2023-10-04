"""
Task 3. Write a program that receives two numbers from the command line – the length and width
of a rectangle, and then calculates its area. For those who did not know or forgot: the area
of the rectangle is calculated by the formula S = a* b. Remember about reliability, pay maximum
attention to it.
"""


def task3_solv():
    width = input_numb("Enter the width: ")
    height = input_numb("Enter the height: ")
    area = area_calc(width, height)
    print(f"S = width * height = {area}")


def area_calc(width: float, height: float) -> float:
    """ Calculating the area of a rectangle """
    try:
        if width > 0 and height > 0:
            return width * height
        raise ValueError
    except ValueError:
        print("Invalid data")


def input_numb(message="") -> float:
    """ Correct number(float) input (add.  a number greater than 0) """
    while True:
        try:
            string_numb = float(input(message))
            if string_numb > 0:
                return string_numb
            print("The number must be greater than 0")
        except ValueError:
            print("Error, try again")


if __name__ == "__main__":
    task3_solv()
