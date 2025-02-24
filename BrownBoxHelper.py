import tkinter as tk
from tkinter import messagebox

class BrownBoxHelper:
    def __init__(self, master):
        self.master = master
        master.title("Chest Guess Assistant")
        master.attributes("-topmost", True)  # Keep the window always on top
        master.geometry("300x200")
        
        # Initialize game parameters.
        self.low = 10
        self.high = 99
        self.attempt = 1
        self.max_attempts = 9
        self.guess = (self.low + self.high) // 2
        
        # Instruction label.
        self.label = tk.Label(master, text="Guess the chest combination (10-99)")
        self.label.pack(pady=10)
        
        # Label displaying current attempt and guess.
        self.guess_label = tk.Label(master, text=f"Attempt {self.attempt} of {self.max_attempts}: {self.guess}")
        self.guess_label.pack(pady=10)
        
        # Frame for feedback buttons.
        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack(pady=10)
        
        # Button for "Greater" feedback.
        self.greater_btn = tk.Button(self.btn_frame, text="Greater", command=lambda: self.process_feedback("greater"))
        self.greater_btn.grid(row=0, column=0, padx=5)
        
        # Button for "Lesser" feedback.
        self.lesser_btn = tk.Button(self.btn_frame, text="Lesser", command=lambda: self.process_feedback("lesser"))
        self.lesser_btn.grid(row=0, column=1, padx=5)
        
        # Button for "Correct" feedback.
        self.correct_btn = tk.Button(self.btn_frame, text="Correct", command=lambda: self.process_feedback("correct"))
        self.correct_btn.grid(row=0, column=2, padx=5)
        
        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=10)
    
    def process_feedback(self, fb):
        if fb == "greater":
            self.low = self.guess + 1
            self.attempt += 1
        elif fb == "lesser":
            self.high = self.guess - 1
            self.attempt += 1
        elif fb == "correct":
            messagebox.showinfo("Success", f"The chest opened with {self.guess} on attempt {self.attempt}!")
            self.reset_game()   # Automatically reset the game after a correct guess.
            return
        
        # Check for inconsistent feedback or exceeded attempts.
        if self.low > self.high or self.attempt > self.max_attempts:
            messagebox.showinfo("Failed", f"Failed to open the chest within {self.max_attempts} tries.")
            self.disable_buttons()
            return
        
        # Calculate the next guess using binary search.
        self.guess = (self.low + self.high) // 2
        self.guess_label.config(text=f"Attempt {self.attempt} of {self.max_attempts}: {self.guess}")
    
    def disable_buttons(self):
        self.greater_btn.config(state=tk.DISABLED)
        self.lesser_btn.config(state=tk.DISABLED)
        self.correct_btn.config(state=tk.DISABLED)
    
    def reset_game(self):
        # Reset the game to its initial state.
        self.low = 10
        self.high = 99
        self.attempt = 1
        self.guess = (self.low + self.high) // 2
        # Update the guess label.
        self.guess_label.config(text=f"Attempt {self.attempt} of {self.max_attempts}: {self.guess}")
        # Re-enable the buttons.
        self.greater_btn.config(state=tk.NORMAL)
        self.lesser_btn.config(state=tk.NORMAL)
        self.correct_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = BrownBoxHelper(root)
    root.mainloop()
