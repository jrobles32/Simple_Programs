import tkinter as tk
from tkinter import ttk
from Password_Generator import generate_password


class PasswordApp(tk.Tk):
    """
    An object that represents a tkinter user interface.
    """
    def __init__(self):
        """
        Creating the basic outline of the user interface and initializing empty variable for later use.
        """
        # Inheriting properties of the base class tk.Tk
        super().__init__()

        self.title('Password Generator')

        # Frame to place multiple buttons into one grid
        self.buttonContainer = tk.Frame(self)

        # Initializing variable for later assignment
        self.lengthEntry = tk.Entry(self)
        self.password_label = tk.Entry(self)
        self.user_num = tk.StringVar(self)

        # Placing label of the desired password characteristics into appropriate grid positions
        tk.Label(self, text='Desired Length of Password:').grid(row=0, sticky='w')
        tk.Label(self, text='Number of Uppercase Letters:').grid(row=1, sticky='w')
        tk.Label(self, text='Number of Lowercase Letters:').grid(row=2, sticky='w')
        tk.Label(self, text='Total Number of Digits:').grid(row=3, sticky='w')
        tk.Label(self, text='Do you want special characters?').grid(row=4, sticky='w')
        tk.Label(self, text='Password:').grid(row=6, sticky='e')

        # Initializing empty combobox [Helps for dynamic length of lists]
        self.upperEntry = ttk.Combobox(self)
        self.lowerEntry = ttk.Combobox(self)
        self.digitsEntry = ttk.Combobox(self)
        self.dropMenu = ttk.Combobox(self)

        # Extracting users desired password length with Enter keystroke
        self.lengthEntry.bind('<Return>', self.starting_lists)

        # Creating buttons to generate password, copy it, and quit program
        self.generate_password = tk.Button(self.buttonContainer, text='Generate', command=self.button_generate)
        self.copy_pass = tk.Button(self.buttonContainer, text='Copy', command=self.copy_password)
        self.quit_app = tk.Button(self.buttonContainer, text='Quit', command=self.quit)

        # Placing buttons and user entry box into appropriate grid position
        self.lengthEntry.grid(row=0, column=1)
        self.buttonContainer.grid(row=5, column=1)
        self.generate_password.grid(row=0, column=0, sticky='ew')
        self.copy_pass.grid(row=0, column=1, sticky='ew')
        self.quit_app.grid(row=0, column=2, sticky='ew')

    def button_generate(self):
        """
        Button command to generate a password and place it into an entry box. Also places the entry box in appropriate
        grid position.

        :return: None
        """
        # Removes any previously created password
        self.password_label.destroy()

        # Creating a variable to store password in and generating it based on user desired characteristics
        password = tk.StringVar()
        password.set(generate_password(int(self.upperEntry.get()),
                                       int(self.lowerEntry.get()),
                                       int(self.digitsEntry.get()),
                                       self.special_select()))

        # Placing password into entry box and placing it in grid
        self.password_label = tk.Entry(self, textvariable=password, state='readonly', bd=0, justify='center')
        self.password_label.grid(row=6, column=1, columnspan=2, sticky='ew')

    def copy_password(self):
        """
        Button command to copy created password onto clipboard.

        :return: None
        """
        password_copy = self.password_label.get()
        self.clipboard_clear()
        self.clipboard_append(password_copy)

    def special_select(self):
        """
        Gets the user input from the dropdown menu of special characters. Default is False.

        :return: True is user wants special character, False otherwise
        :rtype: bool
        """
        if self.dropMenu.get() == 'Yes':
            return True
        else:
            return False

    def setting_values(self):
        """
        Sets the default values of characteristics to a length of 0 and for special characters to false.

        :return: None
        """
        self.upperEntry.current(0)
        self.lowerEntry.current(0)
        self.digitsEntry.current(0)
        self.dropMenu.current(1)

    def starting_lists(self, event):
        """
        Creates a list of the range of the users desired password length. And, updates the value of comboboxs
        initialized to the list created. Function also creates a combobox to represent the desire of special characters,
        places comboboxs in appropriate grib position, and binds the selection of a value to update other lists.

        :param event: None [Event is required in order to be assigned to keystroke]
        :return: None
        """
        # Setting initialized variable user_num to desired user length of password
        self.user_num.set(self.lengthEntry.get())

        # Creating lists for combobox user options
        values_list = [num for num in range(0, int(self.user_num.get()) + 1)]
        options = ['Yes', 'No']

        # Updating values of initialized comboboxes
        self.upperEntry = ttk.Combobox(self, values=values_list, state='readonly', justify='center')
        self.lowerEntry = ttk.Combobox(self, values=values_list, state='readonly', justify='center')
        self.digitsEntry = ttk.Combobox(self, values=values_list, state='readonly', justify='center')
        self.dropMenu = ttk.Combobox(self, values=options, state='readonly', justify='center')

        # Placing comboboxes in appropriate grid position
        self.upperEntry.grid(row=1, column=1)
        self.lowerEntry.grid(row=2, column=1)
        self.digitsEntry.grid(row=3, column=1)
        self.dropMenu.grid(row=4, column=1)

        # Selecting a value from the lists reduces values of other lists
        self.upperEntry.bind('<<ComboboxSelected>>', self.reducing_lists)
        self.lowerEntry.bind('<<ComboboxSelected>>', self.reducing_lists)
        self.digitsEntry.bind('<<ComboboxSelected>>', self.reducing_lists)

        # Setting default values of lists
        self.setting_values()

    def reducing_lists(self, event):
        """
        Updates the values of lists by reducing other lists based on a select value.

        :param event: None [Event is required in order to be assigned to selection of value]
        :return: None
        """
        # Extracting desired length of user and sum of characteristics used
        desired_length = int(self.lengthEntry.get())
        taken_values = int(self.upperEntry.get()) + int(self.lowerEntry.get()) + int(self.digitsEntry.get())

        # Creating different list based on if desired length matches the sum of characteristics used
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


if __name__ == '__main__':
    app = PasswordApp()
    app.mainloop()