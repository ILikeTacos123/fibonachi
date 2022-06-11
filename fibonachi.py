from tkinter import *

root = Tk()

root.title("MathIsBad")
root.geometry("400x400")

unput = Entry(root)

unput.place(relx=0.5, rely=0.4, anchor=CENTER)

Label1 = Label(root, text="Fibonachi = ")
Label2 = Label(root, text="SUM = ")

def fib():
    amount = int(unput.get())
    firstnumb=0
    secondnumb=1
    sum1=0
    sum2=0
    counter=1
    while (counter<=amount):
        Label1["text"] += str(sum1)
        Label2["text"] =  "fibonachi sum = " + str(sum2)
        counter = counter + 1
        firstnumb = secondnumb
        secondnumb = sum1
        sum1 = firstnumb + secondnumb
        sum2 = sum2 + sum1

button = Button(root, command=fib, text="Fibonachi")

button.place(relx=0.5, rely=0.3, anchor=CENTER)
Label1.place(relx=0.5, rely=0.6, anchor=CENTER)
Label2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()