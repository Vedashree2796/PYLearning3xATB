# Web Automation - Selenium
# Page - You are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "Veda@gmail.com" and self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")


# This is the end of the class

email = input("Enter the email \n")
password = input("Enter the password \n")
vani = VWOLoginPage(email, password)
vani.login_confirm()


email = input("Enter the email \n")
password = input("Enter the password \n")

Veda = VWOLoginPage("Veda@gmail.com", "Pass123")
Veda.login_confirm()