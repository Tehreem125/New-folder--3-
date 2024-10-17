#calculator program
while True:
    a = input("Enter your operator +, -, *, /: ") # fixed input operator
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    def sum (a, b):
        return a+b
    
    def sub (a, b):
       return a-b
   
    def multiply (a, b):
        return a*b

    def division (a, b):
        return a/b
       
        
    if(a == '+'):
        print('result',sum(no1, no2))
    elif(a == '-'):
        print('result', sub(no1, no2))
    elif(a == '*'):
        print('result', multiply(no1, no2))
    elif(a == '/'):
        print('result' ,division(no1, no2))
    else:
        print("Operator not found")
        

