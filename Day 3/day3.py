print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

# Check if the user is above 120 cm
if height > 120:
    print("You are tall enough to ride the rollercoaster!")

    # Ask the user for their favorite color
    favorite_color = input("What is your favorite color? ")

    # Check if the user's favorite color is red
    if favorite_color.lower() == "red":
        print("Congratulations! You've chosen the right color!")

        # Ask the user if they want to ride with an adult or child
        adult_or_child = input("Are you an adult or a child? ")

        # Check if the user's choice is adult
        if adult_or_child.lower() == "adult":
            print("The rollercoaster will cost $5 for an adult.")
        # Check if the user's choice is child
        elif adult_or_child.lower() == "child":
            print("The rollercoaster will cost $2 for a child.")
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Sorry, that's not a valid color for the rollercoaster.")
else:
    print("You're not tall enough to ride the rollercoaster.")
