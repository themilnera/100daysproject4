import tkinter as tk
from tkinter import ttk
import questions
import manual_unescape

root = tk.Tk()
root.geometry("1200x600")
root.config(bg="#b6f0ee")
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 14), padding=10, background="blue", foreground="black")
style_radio = ttk.Style()
style_radio.configure("Custom.TRadiobutton", font=("Arial", 14), padding=10, background="#b6f0ee", foreground="black", anchor="w")

chosen_answer = ""
correct_answer = ""
running = True
correct_count = 0
incorrect_count = 0
current_question_index = 0
questions_list = []
radio_var = tk.StringVar()
selected_option = tk.StringVar()

def clear_window():
    # Destroy all widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

def check_answer(answer=""):
    global correct_answer, correct_count, incorrect_count
    if answer == correct_answer:
        print("correct")
        clear_window()
        correct_count += 1
        label_index = tk.Label(root, text=f"You got it right! {correct_count} correct, {incorrect_count} incorrect.", font=("Arial", 22), bg="#b6f0ee")
        label_index.pack(pady=50)
    else:
        print("incorrect")
        clear_window()
        incorrect_count += 1
        label_index = tk.Label(root, text=f"Wrong! {correct_count} correct, {incorrect_count} incorrect.", font=("Arial", 22), bg="#b6f0ee")
        label_index.pack(pady=50)
        label_correct_answer = tk.Label(root, text=f"The correct answer was: {correct_answer}", font=("Arial", 22), bg="#b6f0ee")
        label_correct_answer.pack(pady=50)
    root.after(2500, show_next_question)

def end_quiz():
    label_result = tk.Label(root, text=f"Final results: {correct_count} correct, {incorrect_count} incorrect.", font=("Arial", 22), bg="#b6f0ee")
    label_result.pack(pady=50)
    if incorrect_count == 0:
        label_wow = tk.Label(root, text="Perfect score!", font=("Arial", 22), bg="#b6f0ee")
        label_wow.pack(pady=50)
    start_button = ttk.Button(root, text="Play Again?", style="Custom.TButton", command=configure_start)
    start_button.pack(pady=160)

def show_next_question():
    global current_question_index
    current_question_index +=1
    if current_question_index < len(questions_list):
        display_question(questions_list[current_question_index], current_question_index +1)
    else:
        clear_window()
        end_quiz()
        #end the quiz

def display_question(q, index):
    clear_window()
    label_index = tk.Label(root, text=f"Question #{index}:", font=("Arial", 16), bg="#b6f0ee")
    label_index.pack(pady=20)

    label_question = tk.Label(root, text=q.question, font=("Arial", 18, "bold"), bg="#b6f0ee", wraplength=1000)
    label_question.pack(pady=20)

    global correct_answer, chosen_answer
    correct_answer = q.correct_answer
    y_place = 200
    for answer in q.answers:
        answer = manual_unescape.manual_unescape(answer)
        button_letter = tk.Button(root, command=lambda a=answer: check_answer(a), width=50, wraplength=500, text=f"{answer}", font=("Arial", 18), bg="#0bd9a9", fg="black", activebackground="darkblue", activeforeground="white")
        button_letter.place(x=245, y=y_place)
        y_place += 80

def start_game():
    global current_question_index, correct_count, incorrect_count
    difficulty = 0
    match radio_var.get():
        case "1": difficulty = 1
        case "2": difficulty = 2
        case "3": difficulty = 3
        case _: difficulty = 1
    q_obj = questions.get_questions(str(selected_option.get()), difficulty)
    global questions_list
    questions_list = q_obj
    current_question_index = 0
    correct_count = 0
    incorrect_count = 0
    display_question(questions_list[current_question_index], current_question_index+1)

def configure_start():
    global radio_var, selected_option
    clear_window()
    radio_var.set("1")
    radiobutton1 = ttk.Radiobutton(root, text="Easy", variable=radio_var, value="1", style="Custom.TRadiobutton")
    radiobutton2 = ttk.Radiobutton(root, text="Medium", variable=radio_var, value="2", style="Custom.TRadiobutton")
    radiobutton3 = ttk.Radiobutton(root, text="Hard", variable=radio_var, value="3", style="Custom.TRadiobutton")
    label_number = tk.Label(root, text="Number of questions:", bg="#b6f0ee", font=("Arial", 12, "bold"))

    selected_option.set(5)  # Set default value
    number_options = [5, 10, 25, 50]
    dropdown = tk.OptionMenu(root, selected_option, *number_options)
    dropdown.config(font=("Arial", 12, "bold"))
    label_invisible = tk.Label(root, text="", bg="#b6f0ee")  # just to add space for some packed elements

    label_invisible.pack(pady=20)
    radiobutton1.pack()
    radiobutton2.pack()
    radiobutton3.pack()

    label_number.place(x=518, y=230)
    dropdown.place(x=573, y=270)

    start_button = ttk.Button(root, text="Start Quiz Game", style="Custom.TButton", command=start_game)
    start_button.pack(pady=160)

configure_start()
root.mainloop()