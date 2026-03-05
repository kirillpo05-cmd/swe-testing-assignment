import tkinter as tk
from tkinter import font


class CalculatorApp:
    """A simple GUI calculator application using Tkinter."""
    
    def __init__(self, root):
        """Initialize the calculator GUI."""
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variables
        self.display_var = tk.StringVar(value="0")
        
        # Create GUI
        self.create_widgets()
    
    def create_widgets(self):
        """Create and arrange GUI widgets."""
        # Display
        display_frame = tk.Frame(self.root, bg="#333333")
        display_frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 28),
            border=0,
            justify="right",
            bg="#333333",
            fg="#FFFFFF"
        )
        display.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Button layout: 4 columns
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
            ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
            ("C", 4, 0)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(buttons_frame, text, row, col)
    
    def create_button(self, parent, text, row, col):
        """Create a single button."""
        # Determine button color and span
        if text == "C":
            bg_color = "#FF6B6B"
            fg_color = "white"
            colspan = 4
        elif text in ["+", "-", "*", "/"]:
            bg_color = "#FFA500"
            fg_color = "white"
            colspan = 1
        elif text == "=":
            bg_color = "#4CAF50"
            fg_color = "white"
            colspan = 1
        else:
            bg_color = "#E8E8E8"
            fg_color = "black"
            colspan = 1
        
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 18, "bold"),
            bg=bg_color,
            fg=fg_color,
            border=0,
            activebackground=bg_color,
            activeforeground=fg_color,
            height=2
        )
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights
        parent.grid_rowconfigure(row, weight=1)
        for col_idx in range(4):
            parent.grid_columnconfigure(col_idx, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
