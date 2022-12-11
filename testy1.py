def fizzbuzz(number):
    if number%3 == 0:
        return "Fizz"
    elif number%5 == 0:
        return "Buzz"
    elif number%3 == 0 and number&5 == 0:
        return "FizzBuzz"
    return number