import tkinter as tk
from tkinter import ttk
import re

COMMON_PASSWORDS = ["123456", "password", "12345678", "qwerty", "abc123"]

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add uppercase letter")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("• Add lowercase letter")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("• Add number")

    if re.search("[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("• Add special character")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("• Common password detected!")
        score = 0

    return score, feedback

def update_ui(event=None):
    password = entry.get()
    
    if password == "":
        strength_var.set("Strength: ")
        progress['value'] = 0
        output_var.set("Results will appear here...")
        return

    score, feedback = analyze_password(password)

    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength = levels[min(score, 4)]

    # Update progress
    progress['value'] = score * 20

    # Color change
    colors = ["#ff4d4d", "#ff944d", "#ffd11a", "#9acd32", "#00cc66"]
    progress.configure(style=f"{score}.Horizontal.TProgressbar")

    style.configure(f"{score}.Horizontal.TProgressbar",
                    troughcolor="#2b2b2b",
                    background=colors[min(score, 4)])

    strength_var.set(f"Strength: {strength}")

    if feedback:
        output_var.set("\n".join(feedback))
    else:
        output_var.set("✅ Excellent Password!")

# GUI
root = tk.Tk()
root.title("Password Audit Tool (Advanced)")
root.geometry("420x420")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use('default')

tk.Label(root, text="Enter Password", fg="white", bg="#1e1e1e",
         font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)
entry.bind("<KeyRelease>", update_ui)

progress = ttk.Progressbar(root, length=250, maximum=100)
progress.pack(pady=15)

strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var, fg="white", bg="#1e1e1e",
         font=("Arial", 12)).pack()

output_var = tk.StringVar(value="Results will appear here...")
output = tk.Label(root, textvariable=output_var,
                  justify="left", bg="#2b2b2b", fg="white",
                  width=40, height=10, anchor="nw", padx=10, pady=10)
output.pack(pady=15)

root.mainloop()