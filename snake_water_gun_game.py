import tkinter as tk
import random

# Define the computer choices
choices = {-1: "Snake", 1: "Water", 0: "Gun"}

# Function to determine the game outcome
def play_game(user_choice_key):
    computer_choice = random.choice(list(choices.values()))
    user_choice = choices[user_choice_key]
    
    # Display choices
    computer_choice_label.config(text=f"Computer chooses: {computer_choice}")
    user_choice_label.config(text=f"You chose: {user_choice}")
    
    # Determine the result
    if user_choice == computer_choice:
        result_text = "Match drawn!"
    elif (user_choice == "Snake" and computer_choice == "Water") or \
         (user_choice == "Water" and computer_choice == "Gun") or \
         (user_choice == "Gun" and computer_choice == "Snake"):
        result_text = "You win!"
    else:
        result_text = "Computer wins!"
    
    # Display the result
    result_label.config(text=result_text)

# Set up the main window
root = tk.Tk()
root.title("Snake-Water-Gun Game")

# Display labels for showing choices and results
computer_choice_label = tk.Label(root, text="Computer chooses: ", font=("Arial", 14))
computer_choice_label.pack()

user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 14))
user_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack()

# Buttons for user choices
snake_button = tk.Button(root, text="Snake", font=("Arial", 14), command=lambda: play_game(-1))
snake_button.pack(pady=5)

water_button = tk.Button(root, text="Water", font=("Arial", 14), command=lambda: play_game(1))
water_button.pack(pady=5)

gun_button = tk.Button(root, text="Gun", font=("Arial", 14), command=lambda: play_game(0))
gun_button.pack(pady=5)

# Run the GUI main loop
root.mainloop()
