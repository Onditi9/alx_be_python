# daily_reminder.py

task = input("What's your task for today? ")
priority = input("Priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"High-priority alert! Don't forget to: {task}.")
        if time_bound == "yes":
            print("This is time-sensitive! Schedule it ASAP.")
        else:
            print("You’ve got time, but still—it’s important!")
    case "medium":
        print(f"Medium-priority reminder: {task}.")
        if time_bound == "yes":
            print(" It has a deadline, so plan accordingly.")
        else:
            print("Take it step-by-step. You’ve got this!")
    case "low":
        print(f"Low-priority note: {task}.")
        if time_bound == "yes":
            print("It’s time-bound, even if it’s not urgent.")
        else:
            print("Good to have on the radar. No pressure.")
    case _:
        print(" I didn’t catch that priority level. Try again with high, medium, or low.")