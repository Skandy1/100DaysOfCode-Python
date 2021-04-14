from replit import clear
import art

arr={}
def add_arr(name,bid):
    arr[name]=bid
# add_arr ends
def disp():
    maxi=max(arr,key=arr.get)
    print(f"The highest bidder is {maxi} with ₹{arr[maxi]} !!")


print(art.logo)
print("Welcome to Secret Auction Program!!")
cont=True
while cont:
    nam=input("What is your name? ")
    bid=int(input("What is your bid? ₹"))
    add_arr(nam,bid)
    x=input("Are there any bidders? 'yes' or 'no' ")
    if x=="yes":
        cont=True
        clear()
    elif x=="no":
        clear()
        cont=False
        disp()