# Name: [Yang Jinhui]
# Assignment One
# ddl is 22/9/2026 23:59pm

def calculator():
    print("Simple Calculator")
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    op=input("Choose operation(+,-,*,/):")
    if op == "+":
        print("Result:",num1+num2)
    elif op == "-":
        print("Result:",num1-num2)
    elif op == "*":
        print("Result:",num1*num2)
    elif op == "/":
        print("Result:",num1/num2)
    else:
        print("Invalid operation")

def QA_BOT():
    print("Question Answering Bot")
    condition=True
    while condition:
        question=input("Ask me something:")
        if question=="hello":
            print("Bot: Hello! Nice to meet you.")
        elif question=="python":
            print("Bot: Python is a language.")
        elif question=="jetson":
            print("Bot: Jetson Nano is an AI computer.")
        elif question=="ai":
            print("Bot: AI means Artificial Intelligence.")
        elif question=="name":
            print("Bot: My name is Python Bot.")
        elif question=="exit":
            condition=False
        else:
            print("Bot: Sorry, I don't understand.")

while True:
    function=input("Enter the function you want:")
    print("Enter exit if you want to quit from current function or end this program.")
    if function=="QA":
        QA_BOT()
    if function=="calculator":
        calculator()
    op=input("Enter any keys to continue(exit to quit):")
    if op=="exit":
        break
    
    
