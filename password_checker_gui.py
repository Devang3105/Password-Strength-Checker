import tkinter as tk
from password_checker import check_password


def create_gui():
    window = tk.Tk()
    window.title("Password Strength Checker")
    window.geometry("500x450")
    window.resizable(False, False)
    window.configure(bg="#f3f6ff")

    header = tk.Frame(window, bg="#f3f6ff")
    header.pack(pady=20)

    tk.Label(header, text="Password Strength Checker", font=("Arial", 18, "bold"), bg="#f3f6ff", fg="#1e3a8a").pack()
    tk.Label(header, text="Check how strong your password is", font=("Arial", 10), bg="#f3f6ff", fg="#64748b").pack(pady=4)

    form = tk.Frame(window, bg="#ffffff", padx=20, pady=20)
    form.pack(padx=25, pady=10)

    tk.Label(form, text="Enter Password", font=("Arial", 12, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")

    password_entry = tk.Entry(form, show="*", font=("Arial", 12), width=30, bd=1, relief="solid")
    password_entry.pack(pady=8)

    tk.Button(form, text="Check Strength", font=("Arial", 11, "bold"), bg="#2563eb", fg="white", padx=10, pady=6, command=lambda: check_strength(password_entry, result_label, suggestions_label)).pack(pady=12)

    result_label = tk.Label(form, text="", font=("Arial", 11, "bold"), bg="#ffffff", fg="#0f766e")
    result_label.pack(pady=6)

    suggestions_label = tk.Label(form, text="", font=("Arial", 10), bg="#ffffff", fg="#475569", justify="left", wraplength=320)
    suggestions_label.pack(pady=6)

    def check_strength(entry, result_label_widget, suggestions_label_widget):
        password = entry.get()
        result = check_password(password)

        score = result["Score"]
        strength = result["Strength"]
        suggestions = result["Suggestions"]

        result_label_widget.config(text=f"Score: {score} | Strength: {strength}")

        if suggestions:
            suggestions_text = "Suggestions:\n" + "\n".join(suggestions)
            suggestions_label_widget.config(text=suggestions_text)
        else:
            suggestions_label_widget.config(text="Your password is strong!")

    window.bind("<Return>", lambda event: check_strength(password_entry, result_label, suggestions_label))
    window.mainloop()