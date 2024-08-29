# pass some information to the f(n)

# def greet(name):  # name - parameter or argument
#     print("Hi, How are you", name)
#
#
# greet("Pramod")
# greet("Amit")
# greet("123")
# greet(123)





def allowed_to_enter_the_Python_Class(name):
    match name:
        case "DELL":
            print("DELL is allowed")
        case "Veda":
            print("Veda is allowed")
        case "Namasvi":
            print("Namasvi is allowed")
        case _:
            print("Not allowed")


allowed_to_enter_the_Python_Class("vasu")
