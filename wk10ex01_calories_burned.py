# wk10ex01_calories_burned.py
# Multi-session calorie calculator

def calculate_calories(activity, minutes):
    if activity == "walk":
        rate = 4
    elif activity == "run":
        rate = 10
    elif activity == "cycle":
        rate = 8
    else:
        rate = 0

    return rate * minutes


def main():
    sessions = int(input("How many sessions? "))
    calories_list = []
    total_calories = 0

    for i in range(sessions):
        activity = input("Enter activity (walk/run/cycle): ")
        minutes = int(input("Enter minutes: "))

        calories = calculate_calories(activity, minutes)
        calories_list.append(calories)
        total_calories += calories

    print("Calories per session:", calories_list)
    print("Total calories:", total_calories)


if __name__ == "__main__":
    main()
