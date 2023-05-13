import tkinter as tk
from tkinter import *
order_items = []
def add_sixinch_pizza():
    order_items.append("6-inch Pizza")
    order_label.config(text="Your order: " + ", ".join(order_items))
def add_eightinch_pizza():
    order_items.append("8-inch Pizza")
    order_label.config(text="Your order: " + ", ".join(order_items))
def add_footlong_pizza():
    order_items.append("10-inch Pizza")
    order_label.config(text="Your order: " + ", ".join(order_items))
def calculate_total():
    total = 0
    for item in order_items:
        if item == "6-inch Pizza":
            total += 10
        elif item == "8-inch Pizza":
            total += 11
        elif item == "10-inch Pizza":
            total += 12
    total_label.config(text="Your total: $" + str(round(total, 2)))
root = tk.Tk()
root.title("placeholder name for now")
root.geometry("600x700")
title = tk.Label(root, text="What would you like?")
title.config(font=("Arial", 20))
title.pack()
sixinch_label = tk.Label(root, text="6-inch Pizza: $10")
sixinch_label.config(font=("Arial", 16))
sixinch_label.pack()
eightinch_label = tk.Label(root, text="8-inch Pizza: $11")
eightinch_label.config(font=("Arial", 16))
eightinch_label.pack()
footlong_label = tk.Label(root, text="12-inch Pizza: $12")
footlong_label.config(font=("Arial", 16))
footlong_label.pack()
order_label = tk.Label(root, text="Your order: ")
order_label.pack()
total_label = tk.Label(root, text="Your total: ")
total_label.pack()
sixinch_button = tk.Button(root, text="Click here to order a six-inch pizza.", height=2,
width=30, command=add_sixinch_pizza)
sixinch_button.config(font=("Arial", 8))
sixinch_button.pack()
eightinch_button = tk.Button(root, text="Click here to order an eight-inch pizza.",
height=2, width=30, command=add_eightinch_pizza)
eightinch_button.config(font=("Arial", 8))
eightinch_button.pack()
footlong_button = tk.Button(root, text="Click here to order a twelve inch pizza.", height=2,
width=30, command=add_footlong_pizza)
footlong_button.config(font=("Arial", 8))
footlong_button.pack()
submit_button = tk.Button(root, text="Submit your order.", height=2, width=30,
command=calculate_total)
submit_button.config(font=("Arial", 8))
submit_button.pack()
total_button = tk.Button(root, text="Calculate Total", height=2, width=30,
command=calculate_total)
total_button.config(font=("Arial", 8))
total_button.pack()
exit_button = tk.Button(root, text="Exit", command=root.destroy, height=2,
width=30)
exit_button.config(font=("Arial", 8))
exit_button.pack()
root.mainloop()
#After staring at this damn .py file all night, my eyes can no longer feel joy. The only good thing about this is that I could make a pun. Pizza.py = Pizza pie.
#Nevermind, I saw I had to submit it with a specific name. Let it be known that that pun would have been funny.
#I'm not doing images. I give up.