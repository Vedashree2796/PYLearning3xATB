def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n = n // 10 #Quotient
        # / is div
        # // is Quotient
        # % is Reminder
    return sum_digits




print(sum_of_digits(12345))