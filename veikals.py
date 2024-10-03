import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price*self.quantity
        
class ShopingCart:
    def __init__(self):
        self.produkti = []

    def add_product_to_cart(self, produkts):
        self.produkti.append(produkts)
      

    def get_total_price(self):
        return sum(produkts.get_total_price() for produkts in self.produkti)

    def remove_product_to_cart(self):
        self.produkti.clear()
       



class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Internetveikals")
        self.master.geometry("500x500")
        self.master.configure(background="gray")
        self.cart=ShopingCart()

        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        self.name_label = tk.Label(input_frame, text='Produkts:')
        self.name_label.grid(row=0, column=1)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=2)


        self.price_label = tk.Label(input_frame, text='Cena:')
        self.price_label.grid(row=1, column=1)
        self.price_entry = tk.Entry(input_frame)
        self.price_entry.grid(row=1, column=2)


        self.quantity_label = tk.Label(input_frame, text='Daudzums:')
        self.quantity_label.grid(row=2, column=1)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=2, column=2)

        self.add_button = tk.Button(master, text="Pievienot grozam", command=self.add_to_card)
        self.add_button.pack(pady=5)

        self.cart_listbox = tk.Listbox(master, width=50)
        self.cart_listbox.pack(pady=5)

        self.total_label = tk.Label(master, text='Kopējā cena: 0.00 EUR')
        self.total_label.pack(pady=10)
        
        self.clear_button = tk.Button(master, text="Dzēst grozu", command=self.clear_cart)
        self.clear_button.pack(pady=5)

    def add_to_card(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = float(self.quantity_entry.get())

        produkts = Product(name, price, quantity)
        self.cart.add_product_to_cart(produkts)
        self.cart_listbox.insert(tk.END, f"Produkts: {name} Cena: {price} EUR Daudzums: {quantity} gab")

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.update_total_price()

    def update_total_price(self):
        total = self.cart.get_total_price()
        self.total_label.config(text=f"Kopējā cena: {total:.2f} EUR")

    def clear_cart(self):
        self.cart.remove_product_to_cart()
        self.cart_listbox.delete(0, tk.END)
        self.total_label.config(text='Kopējā cena: 0.00 EUR')



    




if __name__ == '__main__':
    root= tk.Tk()
    app=App(root)
    root.mainloop()