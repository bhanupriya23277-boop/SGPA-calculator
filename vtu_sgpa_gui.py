import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()

root.title("VTU SGPA Calculator")
root.geometry("700x500")

# Heading
title = tk.Label(
    root,
    text="VTU SGPA CALCULATOR",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)

# Subject Name
subject_label = tk.Label(root, text="Subject Name:")
subject_label.pack()

subject_entry = tk.Entry(root, width=30)
subject_entry.pack(pady=5)
# Credits
credits_label = tk.Label(root, text="Credits:")
credits_label.pack()

credits_entry = tk.Entry(root, width=30)
credits_entry.pack(pady=5)
# Grade
grade_label = tk.Label(root, text="Grade:")
grade_label.pack()

grade_combo = ttk.Combobox(
    root,
    values=["O", "A+", "A", "B+", "B", "C", "P", "F"],
    state="readonly",
    width=27
)

grade_combo.pack(pady=5)
grade_combo.set("Select Grade")
# Store subjects
subjects = []
grade_points = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
    "P": 4,
    "F": 0
}

# Add Subject function
def add_subject():
    subject = subject_entry.get().strip()
    grade = grade_combo.get()

    # Check subject name
    if not subject:
        result_label.config(text="Please enter subject name!")
        return

    # Check credits
    try:
        credits = float(credits_entry.get())

        if credits <= 0:
            result_label.config(text="Credits must be positive!")
            return

    except ValueError:
        result_label.config(text="Please enter valid credits!")
        return

    # Check grade
    if grade not in grade_points:
        result_label.config(text="Please select a grade!")
        return

    # Store subject information
    subjects.append((subject, credits, grade))

    # Display subject in table
    table.insert(
        "",
        "end",
        values=(subject, credits, grade)
    )

    # Clear input fields
    subject_entry.delete(0, tk.END)
    credits_entry.delete(0, tk.END)
    grade_combo.set("Select Grade")

    result_label.config(text="Subject added successfully!")   
# Subject table
table = ttk.Treeview(
    root,
    columns=("Subject", "Credits", "Grade"),
    show="headings"
)

table.heading("Subject", text="Subject")
table.heading("Credits", text="Credits")
table.heading("Grade", text="Grade")

table.pack(pady=10)

add_button = tk.Button(
    root,
    text="Add Subject",
    command=add_subject
)

add_button.pack(pady=10)
def calculate_sgpa():
    total_credits = 0
    total_points = 0

    for subject, credits, grade in subjects:
        grade_point = grade_points[grade]

        total_credits += credits
        total_points += credits * grade_point

    if total_credits > 0:
        sgpa = total_points / total_credits
    else:
        result_label.config(text="Please add subjects first.")
    result_label.config(
    text=f"Your SGPA: {sgpa:.2f}\nTotal Credits: {total_credits}"
)
# Reset function
def reset_calculator():
    subjects.clear()

    # Clear the table
    for item in table.get_children():
        table.delete(item)

    # Clear input fields
    subject_entry.delete(0, tk.END)
    credits_entry.delete(0, tk.END)
    grade_combo.set("Select Grade")

    # Reset SGPA result
    result_label.config(text="SGPA: --")
calculate_button = tk.Button(
    root,
    text="Calculate SGPA",
    command=calculate_sgpa
)

calculate_button.pack(pady=10)
reset_button = tk.Button(
    root,
    text="Reset",
    command=reset_calculator
)

reset_button.pack(pady=5)
# THIS IS WHERE THE ANSWER/RESULT IS DISPLAYED
result_label = tk.Label(
    root,
    text="Your SGPA: --",
    font=("Arial", 18, "bold"),
    fg="green",
    justify="center"
)

result_label.pack(pady=15)

# Run the application
root.mainloop()