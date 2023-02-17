import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Criar campo de entrada
        self.entry = tk.Entry(master, width=25, borderwidth=5, font=('Arial', 12))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Criar botões
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]
        r = 1
        c = 0
        for btn in buttons:
            command = lambda x=btn: self.handle_click(x)
            tk.Button(master, text=btn, width=5, height=2, command=command).grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c == 4:
                c = 0
                r += 1

        # Criar botão "C"
        tk.Button(master, text='C', width=5, height=2, command=lambda: self.entry.delete(0, tk.END)).grid(row=4, column=1, padx=5, pady=5)

        # Criar botão "0"
        tk.Button(master, text='0', width=5, height=2, command=lambda: self.entry.insert(tk.END, '0')).grid(row=4, column=0, padx=5, pady=5)

        # Criar botão "="
        tk.Button(master, text='=', width=5, height=2, command=lambda: self.handle_click('=')).grid(row=4, column=1, padx=5, pady=5)

    def handle_click(self, key):
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erro")
        elif key == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, key)


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
