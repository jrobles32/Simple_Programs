import tkinter as tk
from tkinter import ttk
import random
import string


class PasswordGen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Password Generator')

        self.buttonContainer = tk.Frame(self)

        self.lengthEntry = tk.Entry(self)
        self.pass_label = tk.Entry(self)
        self.user_num = tk.StringVar(self)

        tk.Label(self, text='Desired Length of Password:').grid(row=0, sticky='w')
        tk.Label(self, text='Number of Uppercase Letters:').grid(row=1, sticky='w')
        tk.Label(self, text='Number of Lowercase Letters:').grid(row=2, sticky='w')
        tk.Label(self, text='Total Number of Digits:').grid(row=3, sticky='w')
        tk.Label(self, text='Do you want special characters?').grid(row=4, sticky='w')
        tk.Label(self, text='Password:').grid(row=6, sticky='e')

        self.upperEntry = ttk.Combobox(self)
        self.lowerEntry = ttk.Combobox(self)
        self.digitsEntry = ttk.Combobox(self)
        self.dropMenu = ttk.Combobox(self)

        self.lengthEntry.bind('<Return>', self.starting_lists)

        self.generate_pass = tk.Button(self.buttonContainer, text='Generate', command=self.button_generate)
        self.copy_pass = tk.Button(self.buttonContainer, text='Copy', command=self.copy_pass)
        self.quit_app = tk.Button(self.buttonContainer, text='Quit', command=self.quit)

        self.lengthEntry.grid(row=0, column=1)
        self.buttonContainer.grid(row=5, column=1)
        self.generate_pass.grid(row=0, column=0, sticky='ew')
        self.copy_pass.grid(row=0, column=1, sticky='ew')
        self.quit_app.grid(row=0, column=2, sticky='ew')

    def button_generate(self):
        self.pass_label.destroy()
        password = tk.StringVar()
        password.set(generate_password(int(self.upperEntry.get()),
                                       int(self.lowerEntry.get()),
                                       int(self.digitsEntry.get()),
                                       self.special_select()))
        self.pass_label = tk.Entry(self, textvariable=password, state='readonly', bd=0, justify='center')
        self.pass_label.grid(row=6, column=1, columnspan=2, sticky='ew')

    def copy_pass(self):
        password_copy = self.pass_label.get()
        self.clipboard_clear()
        self.clipboard_append(password_copy)

    def special_select(self):
        if self.dropMenu.get() == 'Yes':
            return True
        else:
            return False

    def setting_values(self):
        self.upperEntry.current(0)
        self.lowerEntry.current(0)
        self.digitsEntry.current(0)
        self.dropMenu.current(1)

    def starting_lists(self, event):
        self.user_num.set(self.lengthEntry.get())
        print('Number Found: ' + self.user_num.get())

        values_list = [num for num in range(0, int(self.user_num.get()) + 1)]
        options = ['Yes', 'No']

        self.upperEntry = ttk.Combobox(self, values=values_list, state='readonly', justify='center')
        self.lowerEntry = ttk.Combobox(self, values=values_list, state='readonly', justify='center')
        self.digitsEntry = ttk.Combobox(self, values=values_list, state='readonly', justify='center')
        self.dropMenu = ttk.Combobox(self, values=options, state='readonly', justify='center')

        self.upperEntry.grid(row=1, column=1)
        self.lowerEntry.grid(row=2, column=1)
        self.digitsEntry.grid(row=3, column=1)
        self.dropMenu.grid(row=4, column=1)

        self.upperEntry.bind('<<ComboboxSelected>>', self.reducing_lists)
        self.lowerEntry.bind('<<ComboboxSelected>>', self.reducing_lists)
        self.digitsEntry.bind('<<ComboboxSelected>>', self.reducing_lists)

        self.setting_values()

    def reducing_lists(self, event):
        desired_length = int(self.lengthEntry.get())
        taken_values = int(self.upperEntry.get()) + int(self.lowerEntry.get()) + int(self.digitsEntry.get())

        if taken_values == desired_length:
            upper_shorten = [num for num in range(0, int(self.upperEntry.get()) + 1)]
            lower_shorten = [num for num in range(0, int(self.lowerEntry.get()) + 1)]
            digit_shorten = [num for num in range(0, int(self.digitsEntry.get()) + 1)]

            self.upperEntry['values'] = upper_shorten
            self.lowerEntry['values'] = lower_shorten
            self.digitsEntry['values'] = digit_shorten
        else:
            upper_length = int(self.lengthEntry.get()) - int(self.lowerEntry.get()) - int(self.digitsEntry.get())
            lower_length = int(self.lengthEntry.get()) - int(self.upperEntry.get()) - int(self.digitsEntry.get())
            digit_length = int(self.lengthEntry.get()) - int(self.lowerEntry.get()) - int(self.upperEntry.get())

            self.upperEntry['values'] = [num for num in range(0, upper_length + 1)]
            self.lowerEntry['values'] = [num for num in range(0, lower_length + 1)]
            self.digitsEntry['values'] = [num for num in range(0, digit_length + 1)]


def generate_password(uppercase, lowercase, digits, special=False):
    upper_let = random.sample(list(string.ascii_uppercase), k=uppercase)
    lower_lets = random.sample(list(string.ascii_lowercase), k=lowercase)
    num_choice = ''.join(random.choices(list(string.digits), k=digits))
    special_choice = random.choice(list('$!*.%'))

    first_control = upper_let[0] if uppercase > 0 else ''
    if first_control != '':
        middle_control = 0 if (uppercase - 1) + lowercase <= 0 else (uppercase - 1) + lowercase
    else:
        middle_control = lowercase
    middle_values = ''.join(random.sample(upper_let[1:] + lower_lets, k=middle_control))

    if special:
        password = first_control + middle_values + num_choice + special_choice
    else:
        password = first_control + middle_values + num_choice
    return password


def main():
    app = PasswordGen()
    app.mainloop()


if __name__ == '__main__':
    main()
