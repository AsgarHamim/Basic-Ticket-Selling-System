def ticket_price():
    global age, showtime, price, discount, d_price
    age = int(input("Age: "))
    showtime = int(input("Showtime: "))
    try:
        if showtime < 1700:
            if age <= 10:
                price = 300
                discount = 0.10 * price
                d_price = price - discount
                print("Ticket Price: ", price)
                print("Discount: ", discount)
                print("Discounted Price: ", d_price)
            elif age >= 11:
                price = 500
                discount = 0.10 * price
                d_price = price - discount
                print("Ticket Price: ", price)
                print("Discount: ", discount)
                print("Discounted Price: ", d_price)
            elif age >= 26:
                price = 800
                discount = 0.10 * price
                d_price = price - discount
                print("Ticket Price: ", price)
                print("Discount: ", discount)
                print("Discounted Price: ", d_price)
            elif age > 60:
                price = 400
                discount = 0.10 * price
                d_price = price - discount
                print("Ticket Price: ", price)
                print("Discount: ", discount)
                print("Discounted Price: ", d_price)
        else:
            if age <= 10:
                price = 300
                print("Ticket Price: ", price)
            elif age >= 11:
                price = 500
                print("Ticket Price: ", price)
            elif age >= 26:
                price = 800
                print("Ticket Price: ", price)
            elif age > 60:
                price = 400
                print("Ticket Price: ", price)
    except ValueError:
        ticket_price()

ticket_price()