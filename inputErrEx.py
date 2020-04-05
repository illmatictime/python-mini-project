message = "What is the cost of your book? >>"
while True:
    bookPrice = input(message)
    try:
        bookPrice = float(bookPrice)

        if bookPrice <= 0:
            message = "Use whole # or decimal, no spaces: >> "
            continue
        currect_user_input = True

    except ValueError:
        currect_user_input = False
        message = "Use whole # or decimal, no spaces: >> "

    if currect_user_input:
        print("Your book price is ${0:<.2f}.".format(bookPrice))
        break
