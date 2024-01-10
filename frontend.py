import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        # Get scores from entry widgets
        subject1_score = float(entry_subject1.get())
        subject2_score = float(entry_subject2.get())
        subject3_score = float(entry_subject3.get())

        # Calculate average score
        average_score = (subject1_score + subject2_score + subject3_score) / 3

        # Determine grade based on average score
        if average_score >= 90:
            grade = "A"
        elif 80 <= average_score < 90:
            grade = "B"
        elif 70 <= average_score < 80:
            grade = "C"
        elif 60 <= average_score < 70:
            grade = "D"
        else:
            grade = "F"

        # Display result in a messagebox
        result_message = f"Your average score is {average_score:.2f}, and your grade is {grade}."
        messagebox.showinfo("Result", result_message)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric scores.")

# Create the main window
root = tk.Tk()
root.title("Grade Calculator")

# Create and place entry widgets
tk.Label(root, text="Subject 1 Score:").grid(row=0, column=0)
tk.Label(root, text="Subject 2 Score:").grid(row=1, column=0)
tk.Label(root, text="Subject 3 Score:").grid(row=2, column=0)

entry_subject1 = tk.Entry(root)
entry_subject2 = tk.Entry(root)
entry_subject3 = tk.Entry(root)

entry_subject1.grid(row=0, column=1)
entry_subject2.grid(row=1, column=1)
entry_subject3.grid(row=2, column=1)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=3, column=0, columnspan=2)

# Run the main loop
root.mainloop()
