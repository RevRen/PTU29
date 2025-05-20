import tkinter as tk
from tkinter import font as tkfont


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Skaičiuotuvas")
        self.geometry("300x400")
        self.resizable(False, False)

        self.current_input = ""
        self.total_expression = ""

        self.large_font = tkfont.Font(size=20, weight="bold")

        self._setup_ui()

    def _setup_ui(self):
        self.display_frame = tk.Frame(self, height=100)
        self.display_frame.pack(expand=True, fill="both")

        self.total_label = tk.Label(
            self.display_frame,
            text=self.total_expression,
            anchor="e",
            font=self.large_font,

        )
        self.total_label.pack(expand=True, fill="both")

        self.current_label = tk.Label(
            self.display_frame,
            text=self.current_input,
            anchor="e",
            font=self.large_font,

        )
        self.current_label.pack(expand=True, fill="both")

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(expand=True, fill="both")

        self._create_buttons()

    def _create_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)
        ]

        for button in buttons:
            if len(button) == 5:
                text, row, column, rowspan, columnspan = button
                btn = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=self.large_font,
                    command=lambda x=text: self._on_button_click(x)
                )
                btn.grid(
                    row=row,
                    column=column,
                    rowspan=rowspan,
                    columnspan=columnspan,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )
            else:
                text, row, column = button
                btn = tk.Button(
                    self.buttons_frame,
                    text=text,
                    font=self.large_font,
                    command=lambda x=text: self._on_button_click(x)
                )
                btn.grid(
                    row=row,
                    column=column,
                    sticky="nsew",
                    padx=2,
                    pady=2
                )

        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)

        for i in range(5):
            self.buttons_frame.rowconfigure(i, weight=1)

    def _on_button_click(self, value):
        if value == 'C':
            self.current_input = ""
            self.total_expression = ""
        elif value == '=':
            try:
                self.total_expression += self.current_input
                self.current_input = str(eval(self.total_expression))
                self.total_expression = ""
            except:
                self.current_input = "Klaida"
        else:
            if value in '+-*/':
                self.total_expression += self.current_input + value
                self.current_input = ""
            else:
                self.current_input += value

        self._update_display()

    def _update_display(self):
        self.current_label.config(text=self.current_input[:10])  # Riboja 10 simbolių veiksmo
        self.total_label.config(text=self.total_expression[:20])  # Riboje 20 simbolių atsakymo


app = Calculator()
app.mainloop()
