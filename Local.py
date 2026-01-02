monday = input("Enter day in display")
match monday:
    case "monday":
        print("Start of the work week.")
    case "tuesday":
        print("Second day of the week.")
    case "wednesday":
        print("Midweek day.")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("End of the work week.")
    case "saturday":
        print("Weekend! Time to relax.")
    case "sunday":
        print("Enjoy your Sunday.")
    case _:
        print("Invalid day name.")