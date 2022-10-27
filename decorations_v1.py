def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    print(statement)


    return ""

statement_generator("Welcome to Onlinz Online Shopping!", "*")
