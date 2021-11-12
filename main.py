import tkinter as tk
from tkinter import ttk
from secrets import randbelow


# ---------------
# HELPER METHODS
# ---------------

def output_pwd():
    """
    Output the new password to the display box.

    """

    # clear password display box
    pwd.delete(0, tk.END)

    # get password length from input
    pwd_length = int(length.get())

    # determine password strength and create password
    if strength.get() == 'Medium':
        new_pwd = medium_pwd(pwd_length)
    elif strength.get() == 'Low':
        new_pwd = low_pwd(pwd_length)
    else:
        new_pwd = high_pwd(pwd_length)

    # output password to display
    pwd.insert(0, new_pwd)


def high_pwd(pwd_length):
    """
    Generate a high strength password.

    Contains numbers, letters (upper- & lowercase), and special characters.

    :param pwd_length: int
                    Length of password to be generated.
    :return: str
            New password generated.
    """

    new_pwd = ''
    for x in range(pwd_length):
        new_pwd += chr(randbelow(94) + 33)
    return new_pwd


def medium_pwd(pwd_length):
    """
    Generate a medium strength password.

    Contains only lowercase letters.

    :param pwd_length: int
                    Length of password to be generated.
    :return: str
            New password generated.
    """

    new_pwd = ''
    for x in range(pwd_length):
        new_pwd += chr(randbelow(26) + 97)
    return new_pwd


def low_pwd(pwd_length):
    """
    Generate a medium strength password.

    Contains only numbers.

    :param pwd_length: int
                    Length of password to be generated.
    :return: str
            New password generated.
    """

    new_pwd = ''
    for x in range(pwd_length):
        new_pwd += chr(randbelow(10) + 48)
    return new_pwd


def copy():
    """
    Copy the password to the clipboard.

    """

    # clear the clipboard
    root.clipboard_clear()

    # copy password to clipboard
    root.clipboard_append(pwd.get())


# ------------------
# INITIALIZE WINDOW
# ------------------

# create root window
root = tk.Tk()
root.title('Password Generator')
root.iconbitmap('')
root.geometry("350x170")
root.configure(bg="sky blue")

# --------------
# CREATE LABELS
# --------------

# make label for password length entry
length_label = tk.Label(root, text="Enter Length:", bg="sky blue")

# create label for strength drop-down menu
strength_label = tk.Label(root, text="Select Strength:", bg="sky blue")

# create label for password display
pwd_label = tk.Label(root, text="Password:", bg="sky blue")

# -------------------------------
# CREATE DATA INPUT/OUTPUT BOXES
# -------------------------------

# create entry box for password length
length = tk.Entry(root)

# create drop-down menu for strength selection
strength = ttk.Combobox(root, width=15)
strength['values'] = ('Low', 'Medium', 'High')

# create display box for password
pwd = tk.Entry(root)

# ---------------
# CREATE BUTTONS
# ---------------

generate_button = tk.Button(root, text="Generate", command=output_pwd)
copy_button = tk.Button(root, text="Copy", command=copy)

# --------------
# FORMAT LAYOUT
# --------------

length_label.grid(row=0, column=0, sticky=tk.W, pady=2)
strength_label.grid(row=1, column=0, sticky=tk.W, pady=2)
pwd_label.grid(row=2, column=0, sticky=tk.W, pady=2)

length.grid(row=0, column=1, sticky=tk.W, pady=2)
strength.grid(row=1, column=1, sticky=tk.W, pady=2)
pwd.grid(row=2, column=1, sticky=tk.W, pady=2)

generate_button.grid(row=3, column=1, pady=10)
copy_button.grid(row=4, column=1)

# ----
# RUN
# ----

# infinite loop to run the app
root.mainloop()
