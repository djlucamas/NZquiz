import tkinter as tk
import random

# Define quiz questions
quiz_data = {
    "Sport": [
        ("Who is New Zealand’s highest test run scorer in cricket?", "Kane Williamson"),
        ("Which rugby team is known as the All Blacks?", "New Zealand National Rugby Team"),
        # Add 28 more sport questions
    ],
    "History": [
        ("In what year did New Zealand become the first country to grant women the right to vote?", "1893"),
        ("Who was the first European to discover New Zealand?", "Abel Tasman"),
        # Add 28 more history questions
    ],
    "Pop Culture": [
        ("Which New Zealand director made the Lord of the Rings movies?", "Peter Jackson"),
        ("What is the name of the popular New Zealand comedy duo?", "Flight of the Conchords"),
        # Add 28 more pop culture questions
    ],
    "Geography": [
        ("What is the name of New Zealand’s tallest mountain?", "Aoraki / Mount Cook"),
        ("Which city is known as the ‘City of Sails’?", "Auckland"),
        # Add 28 more geography questions
    ],
    "Around The Country": [
        ("What is the name of New Zealand’s capital city?", "Wellington"),
        ("Where can you find the Hobbiton movie set?", "Matamata"),
        # Add 28 more country-based questions
    ]
}

# Function to load a random question
def load_question():
    category = category_var.get()
    if category in quiz_data:
        question, answer = random.choice(quiz_data[category])
        question_label.config(text=question)
        answer_label.config(text="")
        answer_button.config(command=lambda: answer_label.config(text=answer))

# Set up GUI
root = tk.Tk()
root.title("NZ General Knowledge Quiz")
root.geometry("500x300")

tk.Label(root, text="Select a Category:", font=("Arial", 14)).pack()
category_var = tk.StringVar(root)
category_var.set("Sport")
category_menu = tk.OptionMenu(root, category_var, *quiz_data.keys())
category_menu.pack()

tk.Button(root, text="Get Question", command=load_question, font=("Arial", 12)).pack()

question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
question_label.pack()

answer_button = tk.Button(root, text="Show Answer", font=("Arial", 12))
answer_button.pack()

answer_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
answer_label.pack()

root.mainloop()
