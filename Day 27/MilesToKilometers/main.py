from tkinter import *
# def function
def calc():
    kilometers_entry.config(state="normal")
    miles=int(miles_entry.get())
    km=round((miles*1.60934),3)
    kilometers_entry.delete(0,'end')
    kilometers_entry.insert(END,string=str(km))
    kilometers_entry.config(state="readonly")

window = Tk()
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
window.title("Miles to Kilometers")
# entry
miles_entry = Entry(width=8)
miles_entry.grid(row=0, column=0)

# label for miles
label_miles = Label(text="miles =", font=("Arial", 12, "bold"))
label_miles.config(padx=10, pady=10)
label_miles.grid(row=0, column=1)

# entry for kilometers
kilometers_entry=Entry(width=8)
kilometers_entry.grid(row=0, column=2)

# label for km
label_kilometers=Label(text="kilometers",font=("Arial", 12, "bold"))
label_kilometers.config(padx=10, pady=10)
label_kilometers.grid(row=0,column=3)

# calculate button
button=Button(text="Convert",font=("Arial",12,"bold"),width=10,bg="lightgreen",command=calc)
button.grid(row=1,column=2)

window.mainloop()
