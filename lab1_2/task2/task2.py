def task2_solv():
    people = []
    numb_of_people = input_numb("Enter the number of people: ")

    # Input all the info about people
    for i in range(int(numb_of_people)):
        print(f"======----|{i+1}|----======")
        name = input_str("Enter the name: ")
        surname = input_str("Enter the surname: ")
        age = input_numb("Enter the age: ")
        people.append((name, surname, age))
    print("=======================")

    for person in people:
        print(f"{person[0]} {person[1]} {person[2]}")
    ages_info = age_statistic(people)

    print(f"The smallest age: {ages_info[0]}")
    print(f"The biggest age: {ages_info[1]}")
    print(f"The average age: {ages_info[2]:.2f}")


def age_statistic(people: list) -> tuple:
    try:
        min_age = min(people, key=lambda x: x[2])[2]
        max_age = max(people, key=lambda x: x[2])[2]
        avg_age = sum(person[2] for person in people) / len(people)
        return min_age, max_age, avg_age
    except Exception:
        raise Exception("Invalid data")


def input_str(message="") -> str:
    """ Correct string input (only letters) """

    while True:
        string = input(message)
        if string.isalpha():
            return string
        print("Error, try again")


def input_numb(message="") -> int:
    """ Correct number(int) input (add.  a number greater than 0) """

    while True:
        try:
            string_numb = int(input(message))
            if string_numb > 0:
                return string_numb
            print("The number must be greater than 0")
        except ValueError:
            print("Error, try again")


if __name__ == "__main__":
    task2_solv()
