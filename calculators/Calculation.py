import pyttsx3
import time

def print_and_say_invalid_messeage(iterable):
    print(f"Please type a positive number next time ( {iterable} ) , an invalid!")
    engine = pyttsx3.init()
    engine.say(f"Please type a positive number next time ( {iterable} ) , an invalid!")
    engine.runAndWait()

def calculation():
    def say_result():
        engine = pyttsx3.init()
        engine.say(f"the result is: {round(result, 3)} ")
        engine.runAndWait()

    def try_convert_type(num):
        try:
            num = float(num)
            return num
        except:
            print(f"please type a number next time, {num} is not a namber! ")
            engine = pyttsx3.init()
            engine.say(f"please type a number next time, {num} is not a namber! ")
            engine.runAndWait()
            exit()

    num1 = input("Enter the first number: \n")
    num1 = try_convert_type(num1)

    operation = input("Enter an operation to perform > (+ , - , * , / , % , // , **) < : \n")
    operations = ["+", "-" , "*" , "/" , "%" , "//" , "**"]
    
    num2 = input("Enter the second number: \n")
    num2 = try_convert_type(num2)
    
    if  operation in operations: 
        match operation:
            case "+":
                result = num1 + num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result()
            
            case "-":
                result = num1 - num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result()

            case "*":
                result = num1 * num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result()

            case "/":
                result = num1 / num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result()

            case "%":
                result = num1 % num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result()
                
            case "//":
                result = num1 // num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result() 
            case "**":
                result = num1 ** num2
                print(f"{num1} {operation} {num2} = {round(result, 3)}")
                say_result()
    else:
        print (f"{operation} is an Invalid operation!")
        engine = pyttsx3.init()
        engine.say(f"{operation} is an Invalid operation!")
        engine.runAndWait()


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

while True:
    iterable = input(f"{CLEAR} {CLEAR_AND_RETURN} how many time for call function ? \n")
    try:
        iterable = int(iterable)
    except:
        continue

    if iterable < 0:  # if n > 0 : break
        print_and_say_invalid_messeage(iterable)
        continue
    else:
        break


try:
    for _ in range(iterable):
        print(f"{CLEAR} {CLEAR_AND_RETURN}")
        calculation()
except:
    print("Good bye!")