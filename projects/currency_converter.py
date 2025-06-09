while True:
    try:
        amount = float(input("Enter the amount : "))
        if amount <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid amount ")

valid_currency = ("USD", "EUR", "CAD")

while True:
    source_currency = input("Enter the Source Currency: ").upper()
    if source_currency in valid_currency:
        while True:
            convert_to_currency = input("Enter the currency to be converted: ").upper()
            if convert_to_currency in valid_currency:
                #convert()
                print("valid currency")
                break
            else:
                ("Enter the valid currency choice ")
        break
    else:
        print("Enter the valid source currency :) ")


