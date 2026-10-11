import tkinter as tk
import ast

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x420")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief="flat",
            bg="#f2f2f2"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Buttons
        buttons = [
            ("C", 1, 0, "clear"),
            ("÷", 1, 1, "op"),
            ("×", 1, 2, "op"),
            ("⌫", 1, 3, "back"),
            ("7", 2, 0, "num"),
            ("8", 2, 1, "num"),
            ("9", 2, 2, "num"),
            ("-", 2, 3, "op"),
            ("4", 3, 0, "num"),
            ("5", 3, 1, "num"),
            ("6", 3, 2, "num"),
            ("+", 3, 3, "op"),
            ("1", 4, 0, "num"),
            ("2", 4, 1, "num"),
            ("3", 4, 2, "num"),
            ("=", 4, 3, "equal"),
            ("0", 5, 0, "num", 2),
            (".", 5, 2, "num"),
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            kind = button[3]
            span = button[4] if len(button) > 4 else 1

            b = tk.Button(
                root,
                text=text,
                font=("Arial", 18),
                command=lambda t=text, k=kind: self.on_click(t, k),
                width=5,
                height=2,
                bg="#eaeaea" if kind != "op" and kind != "equal" else "#f0ad4e",
                fg="black" if kind != "op" and kind != "equal" else "white",
                bd=0
            )
            b.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=4, pady=4)

        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    def on_click(self, value, kind):
        if kind == "num":
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        elif kind == "op":
            if not self.expression:
                return
            last_char = self.expression[-1]
            if last_char in "+-÷×":
                self.expression = self.expression[:-1] + value
            else:
                self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        elif kind == "clear":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif kind == "back":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        elif kind == "equal":
            self.calculate()

    def calculate(self):
        if not self.expression:
            return

        expr = self.expression
        expr = expr.replace("÷", "/").replace("×", "*")

        try:
            safe_expr = ast.parse(expr, mode="eval")
            allowed_nodes = (
                ast.Expression, ast.BinOp, ast.UnaryOp, ast.Add, ast.Sub,
                ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd, ast.Constant
            )

            for node in ast.walk(safe_expr):
                if not isinstance(node, allowed_nodes):
                    raise ValueError("Invalid expression")

            result = eval(compile(safe_expr, "<string>", "eval"), {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        except Exception:
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()