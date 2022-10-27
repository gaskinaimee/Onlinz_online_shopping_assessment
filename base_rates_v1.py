def base_rates():
    volume = input(question)

    if volume <= 6000:
        print("The bass rate for your package is $8.00.")

    elif volume > 6000 and volume < 100000:
        print("The base rate for your package is $12.00.")

    elif volume >= 100000:
        print("The base rate for your package is $15.00.")

