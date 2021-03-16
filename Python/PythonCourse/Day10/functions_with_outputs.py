# def format_name(f_name, l_name):
#    f = f_name.title()
#    l = l_name.title()

# Days in a month

# def is_leap(year):
#  if year % 4 == 0:
#    if year % 100 == 0:
#      if year % 400 == 0:
#        return True
#      else:
#        return not True
#    else:
#      return True
#  else:
#    return not True
#
# def days_in_month(years, months):
#  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#  if is_leap(years) and months == 2:
#      return 29
#  return month_days[months - 1]
#
#
#year = int(input("Enter a year: "))
#month = int(input("Enter a month: "))
#days = days_in_month(year, month)
# print(days)

# Calculator challenge

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def new_calc():
    num1 = int(input("Type in your first value: "))

    for operation in operations:
        print(operation)
    symbol = input("Select an action from the list above: ")
    num2 = float(input("Type in your second value: "))
    # Assigning a new variable name to a function call
    calc = operations[symbol]
    answer = calc(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")

    continue_calcing = False
    ans = input(
        "Do you want to continue calculating? 'y' for yes, 'n' for no: ").lower()
    if ans == "y":
        continue_calcing = True

    while continue_calcing:
        symbol = input(
            "Select another action (type 'help' to see them again): ")
        while symbol == "help":
            for operation in operations:
                print(operation)
            symbol = input("Select an action from the list above: ")

        next_value = float(input("Type in your next value: "))
        new_answer = operations[symbol]
        new_answer(answer, next_value)
        print(f"{answer} {symbol} {next_value} = {new_answer}")


new_calc()
