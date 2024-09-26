from tkinter import *
from tkinter import messagebox
from PIL import ImageTk




def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 's' and passwordEntry.get() == '1':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        show_ewallet_gui()
    else:
        messagebox.showerror('Error', 'The username or password you entered is incorrect')


def register():
    register_window = Toplevel(window)
    register_window.title("Registration")
    register_window.geometry("1280x700+0+0")

    # Set the background image
    background_image = ImageTk.PhotoImage(file="r1.jpg")
    background_label = Label(register_window, image=background_image)
    background_label.place(x=0, y=0)



    # Full Name Label and Entry
    fullname_label = Label(register_window, text="Full Name:", bg="skyblue1")
    fullname_label.grid(row=0, column=0, padx=10, pady=10)
    fullname_entry = Entry(register_window)
    fullname_entry.grid(row=0, column=1, padx=10, pady=10)

    # Email Label and Entry
    email_label = Label(register_window, text="Email:",bg="skyblue1")
    email_label.grid(row=1, column=0, padx=10, pady=10)
    email_entry = Entry(register_window)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    # Occupation Label and Entry
    occupation_label = Label(register_window, text="Occupation:", bg="skyblue1")
    occupation_label.grid(row=2, column=0, padx=10, pady=10)
    occupation_entry = Entry(register_window)
    occupation_entry.grid(row=2, column=1, padx=10, pady=10)

    # Gender Label and Entry
    gender_label = Label(register_window, text="Gender:", bg="skyblue1")
    gender_label.grid(row=3, column=0, padx=10, pady=10)
    gender_entry = Entry(register_window)
    gender_entry.grid(row=3, column=1, padx=10, pady=10)

    # Date of Birth Label and Entry
    dob_label = Label(register_window, text="Date of Birth:", bg="skyblue1")
    dob_label.grid(row=4, column=0, padx=10, pady=10)
    dob_entry = Entry(register_window)
    dob_entry.grid(row=4, column=1, padx=10, pady=10)

    # Username Label and Entry
    username_label = Label(register_window, text="Username:", bg="skyblue1")
    username_label.grid(row=5, column=0, padx=10, pady=10)
    username_entry = Entry(register_window)
    username_entry.grid(row=5, column=1, padx=10, pady=10)

    # Password Label and Entry
    password_label = Label(register_window, text="Password:", bg="skyblue1")
    password_label.grid(row=6, column=0, padx=10, pady=10)
    password_entry = Entry(register_window, show="*")
    password_entry.grid(row=6, column=1, padx=10, pady=10)

    def create_account():
        # Get the values from the entry fields
        fullname = fullname_entry.get()
        email = email_entry.get()
        occupation = occupation_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # Perform account creation logic here
        # ...

        # Show registration success message
        messagebox.showinfo("Registration Successful", "Account created successfully.")

        # Clear entry fields
        fullname_entry.delete(0, END)
        email_entry.delete(0, END)
        occupation_entry.delete(0, END)
        gender_entry.delete(0, END)
        dob_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)

    create_button = Button(register_window, text="Create Account", command=create_account, bg="skyblue1")
    create_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


def show_ewallet_gui():
    root = Tk()
    root.title("E-Wallet")
    root.geometry("1200x600")

    # Set the background image
    backgroundImage = ImageTk.PhotoImage(file='bN.jpg')
    backLevel = Label(root, image=backgroundImage)
    backLevel.place(x=0, y=0)

    balance = 0.0

    # My Current Balance Label
    balance_label = Label(root, text="My Current Balance:", bg='green')
    balance_label.grid(row=0, column=0, padx=100, pady=40)
    balance_amount_label = Label(root, text="$%.2f" % balance)
    balance_amount_label.grid(row=0, column=1, padx=10, pady=40)

    # Payment Label
    payment_label = Label(root, text="Payment", bg='green')
    payment_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Pay To Entry
    pay_to_label = Label(root, text="Pay To:", bg='green')
    pay_to_label.grid(row=2, column=0, padx=10, pady=5)
    pay_to_entry = Entry(root)
    pay_to_entry.grid(row=2, column=1, padx=10, pady=5)

    # Reason Entry
    reason_label = Label(root, text="Reason:", bg='green')
    reason_label.grid(row=2, column=2, padx=10, pady=5)
    reason_entry = Entry(root)
    reason_entry.grid(row=2, column=3, padx=10, pady=5)

    # Amount Entry
    amount_label = Label(root, text="Amount:", bg='green')
    amount_label.grid(row=2, column=4, padx=10, pady=5)
    amount_entry = Entry(root)
    amount_entry.grid(row=2, column=5, padx=10, pady=5)

    # Date Entry
    date_label = Label(root, text="Date:", bg='green')
    date_label.grid(row=2, column=6, padx=10, pady=5)
    date_entry = Entry(root)
    date_entry.grid(row=2, column=7, padx=10, pady=5)

    # Pay Button
    def pay():
        nonlocal balance
        pay_to = pay_to_entry.get()
        reason = reason_entry.get()
        amount = amount_entry.get()
        date = date_entry.get()

        if not all([pay_to, reason, amount, date]):
            messagebox.showerror("Error", "Please fill in all the payment details.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        if amount > balance:
            messagebox.showerror("Error", "Less balance amount.")
            return

        # Perform payment processing logic here
        # ...

        # Update balance label
        balance -= amount
        balance_amount_label.config(text="$%.2f" % balance)

        # Add payment to payment history
        payment_history_text.insert(END, "Paid to: {}\nReason: {}\nAmount: ${}\nDate: {}\n\n".format(pay_to, reason,
                                                                                                    amount, date))

        # Clear entry bars
        pay_to_entry.delete(0, END)
        reason_entry.delete(0, END)
        amount_entry.delete(0, END)
        date_entry.delete(0, END)

        # Show payment success message
        messagebox.showinfo("Payment Successful", "Payment of $%.2f to %s recorded." % (amount, pay_to))

    pay_button = Button(root, text="Pay", command=pay, font=("Arial", 12), bg='green')
    pay_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Deposit Label
    deposit_label = Label(root, text="Deposit", bg='green')
    deposit_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Deposit Amount Entry
    deposit_amount_label = Label(root, text="Amount:", bg='green')
    deposit_amount_label.grid(row=5, column=0, padx=10, pady=5)
    deposit_amount_entry = Entry(root)
    deposit_amount_entry.grid(row=5, column=1, padx=10, pady=5)

    # Deposit Date Entry
    deposit_date_label = Label(root, text="Date:", bg='green')
    deposit_date_label.grid(row=5, column=2, padx=10, pady=5)
    deposit_date_entry = Entry(root)
    deposit_date_entry.grid(row=5, column=3, padx=10, pady=5)

    # Deposit Button
    def deposit():
        nonlocal balance
        deposit_amount = deposit_amount_entry.get()
        deposit_date = deposit_date_entry.get()

        if not all([deposit_amount, deposit_date]):
            messagebox.showerror("Error", "Please fill in all the deposit details.")
            return

        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        # Perform deposit processing logic here
        # ...

        # Update balance label
        balance += deposit_amount
        balance_amount_label.config(text="$%.2f" % balance)

        # Add deposit to deposit history
        deposit_history_text.insert(END, "Amount: ${}\nDate: {}\n\n".format(deposit_amount, deposit_date))

        # Clear entry bars
        deposit_amount_entry.delete(0, END)
        deposit_date_entry.delete(0, END)

        # Show deposit success message
        messagebox.showinfo("Deposit Successful", "Deposit of $%.2f recorded." % deposit_amount)

    deposit_button = Button(root, text="Deposit", command=deposit, font=("Arial", 12), bg='green')
    deposit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Payment History
    payment_history_label = Label(root, text="Payment History",bg='green')
    payment_history_label.grid(row=13, column=0, columnspan=2, padx=10, pady=10)
    payment_history_text = Text(root, height=5, width=40)
    payment_history_text.grid(row=14, column=0, columnspan=4, padx=10, pady=5)

    # Deposit History
    deposit_history_label = Label(root, text="Deposit History", bg='green')
    deposit_history_label.grid(row=13, column=4, columnspan=2, padx=10, pady=10)
    deposit_history_text = Text(root, height=5, width=40)
    deposit_history_text.grid(row=14, column=4, columnspan=4, padx=10, pady=5)

    root.mainloop()






if __name__ == "__main__":
    window = Tk()
    window.geometry('1280x700+0+0')
    window.title('Login SRMS ')
    backgroundImage = ImageTk.PhotoImage(file='ne.jpg')

    backLevel = Label(window, image=backgroundImage)
    backLevel.place(x=0, y=0)

    loginFrame = Frame(window, bg='white')
    loginFrame.place(x=400, y=150)

    logoImage = PhotoImage(file='My project.png')

    logoLabel = Label(loginFrame, image=logoImage)
    logoLabel.pack(pady=20)

    usernameLabel = Label(loginFrame, text='Username', font=('arial', 12, 'bold'), fg='black',bg='dodgerblue1')
    usernameLabel.pack()

    usernameEntry = Entry(loginFrame, font=('arial', 12))
    usernameEntry.pack()

    passwordLabel = Label(loginFrame, text='Password', font=('arial', 12, 'bold'), fg='black',bg='dodgerblue1')
    passwordLabel.pack()

    passwordEntry = Entry(loginFrame, font=('arial', 12), show='*')
    passwordEntry.pack()

    loginButton = Button(loginFrame, text='Login', font=('arial', 12, 'bold'), fg='black', bg='dodgerblue1', command=login)
    loginButton.pack(pady=20)

    registerButton = Button(loginFrame, text='Register', font=('arial', 12, 'bold'), fg='black', bg='dodgerblue1',
                            command=register)
    registerButton.pack()

    window.mainloop()
