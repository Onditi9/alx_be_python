# Personal Daily Reminder

# Ask the user to input a task description,task priority and time bound option
task = input("Enter your task: ")
print()
priority = input("Priority (high/medium/low): ")
print()
time_bound =input("Is it time-bound? (yes/no): ")

# Match Case statements that react differently based on the task’s priority
match priority:
    case "high":
      if time_bound == "yes":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    
      else:
        print(f"Note:{task} is a high priority task. Consider completing it before the day ends.")

    case "medium":
      if time_bound == "yes":
        print(f"{task} is a medium priority task that should be atttended as soon possible!")
    
      else:
        print(f"{task} is a medium priority task. Consider doing it when you are less busy .")

    case "low":
      if time_bound == "yes":
        print(f"{task} is a low priority task that can be completed within the week")
    
      else:
        print(f"{task} is a low priority task. Consider completing it when you have free time.")