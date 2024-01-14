# Import necessary modules and functions from other files
from shared_modules import turtle, screen, my_turtle, transformed_vertices
import interactiveMode
import fileMode
import transformations


def mode_selection():
    wrong_entry = False
    description = "0 for reading from File\n1 for interactive mode\n2 for reading all the directory files :"
    while True:
        user_input = turtle.textinput("Input", description)
        if user_input in ['0', '1', '2']:
            return (user_input)
        else:
            if not wrong_entry:
                description = "Invalid input. Please enter either 0 or 1 or 2.\n"+description
                wrong_entry = True

# Define the main function


def main():
    # Get user input for choosing between file mode and interactive mode and directory files
    choice = mode_selection()

    # Check the user's choice
    if choice == '0':
        # If the choice is 0, handle file mode and then enter transformation mode
        fileMode.handleFileMode()
        transformations.transformation_mode()

    elif choice == '1':
        # If the choice is 1, handle interactive mode
        interactiveMode.handleInteractiveMode()

    else:
        fileMode.handleDirecotryMode()


# Check if the script is being run as the main module
if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
