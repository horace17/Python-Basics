def greet(age : int, school, name = "Guest"):
    print(f"Hello, {name.upper()} you are {age} years old.")

def avr(number1 : int, number2 : int, number3 = 10):
    return (number1 + number2 + number3) / 3

average = avr(45,76,84)
print(average)
# greet(name = "Horace", age = 18, school="emobilis")
# greet("Joseph")