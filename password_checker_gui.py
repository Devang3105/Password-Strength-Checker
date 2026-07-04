import tkinter as tk
from password_checker import check_password

def create_gui():
    window = tk.Tk()
    window.title("Password Strength Checker")
    window.geometry("500x450")
    window.resizable(False, False)
    
    title = tk.Label(window, text="Password Strength Checker", font=("Arial", 16, "bold"))
    title.pack(pady=15)
    
    password_label = tk.Label(window, text="Enter Password:", font=("Arial", 12))
    password_label.pack()
    
    password_entry = tk.Entry(window, show="*", font=("Arial", 12), width=30)
    password_entry.pack(pady=10)
    
    result_label = tk.Label(window, text="", font=("Arial", 14,"bold"))
    result_label.pack(pady=10)
    
    suggestions_label = tk.Label(window, text="", font=("Arial", 11), justify="left")
    suggestions_label.pack(pady=10)
    
    def check_strength():
        password = password_entry.get()
        result = check_password(password)
        
        score = result["Score"]
        strength = result["Strength"]
        suggestions = result["Suggestions"]
        
        result_label.config(text=f"Score: {score} | Strength: {strength}")
        
        if suggestions:
            suggestions_text = "Suggestions:\n" + "\n".join(suggestions)
            suggestions_label.config(text=suggestions_text)
        else:
            suggestions_label.config(text="Your password is strong!")
            
    check_button = tk.Button(window, text="Check Strength", font=("Arial", 12), command=check_strength)
    check_button.pack(pady=10)
    
    window.mainloop()