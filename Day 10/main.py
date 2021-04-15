import art

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def calculator():
    print(art.logo)
    n1=float(input("What's the first Number? "))
    for x in operations:
        print(x)

    run=True
    while run:
        op=input("Pick an operation to perform? ")
        n2=float(input("What's the second Number? "))
        fun=operations[op]
        result=round(fun(n1,n2),2)
        print(f"{n1} {op} {n2} = { result}")
        ask=input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation or 'e' to exit:")
        if ask == "y":
            n1=result
        elif ask=="n":
            calculator()
        elif ask=="e":
            print("Good Bye")
            run=False
calculator()
