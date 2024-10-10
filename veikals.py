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
        self.master.geometry("500x650")
        self.master.configure(background="black")
        self.cart=ShopingCart()

        
        
        
        
        frame_input = tk.Frame(master, bg="black")
        frame_input.pack(pady=10)


        self.virsraksts_label = tk.Label(frame_input, text="Internetveikals #Tumšais Tīkls#", font=("Arial", 16, "bold"), bg="black", fg="white")
        self.virsraksts_label.grid(row=0, column=1)

        self.bilde_frame = tk.Frame(master, bg="black")
        self.bilde_frame.pack(pady=5)

        self.bilde_image =Image.open("image.png")
        self.resized_bilde = self.bilde_image.resize((150,125))#bildes garums
        self.bilde = ImageTk.PhotoImage(self.resized_bilde)
        self.bilde_label = ttk.Label(self.bilde_frame, image=self.bilde, background="black")
        self.bilde_label.grid(row=1, column=0, padx=1, pady=1)


        
        input_frame = tk.Frame(master, bg="black")
        input_frame.pack(pady=10)


        self.name_label = tk.Label(input_frame, text='Produkts:', font=(9), bg="black", fg="white")
        self.name_label.grid(row=1, column=1)
        self.name_entry = tk.Entry(input_frame, bg="#505050", fg="white", font=(9))
        self.name_entry.grid(row=1, column=3)


        self.price_label = tk.Label(input_frame, text='Cena:', font=(9), bg="black", fg="white")
        self.price_label.grid(row=2, column=1)
        self.price_entry = tk.Entry(input_frame, bg="#505050", fg="white", font=(9))
        self.price_entry.grid(row=2, column=3)


        self.quantity_label = tk.Label(input_frame, text='Daudzums:', bg="black", fg="white", font=(9))
        self.quantity_label.grid(row=3, column=1)
        self.quantity_entry = tk.Entry(input_frame, bg="#505050", fg="white", font=(9))
        self.quantity_entry.grid(row=3, column=3)

        self.add_button = tk.Button(master, text="Pievienot grozam", bg="#505050", fg="white", font=(11), command=self.add_to_card, bd=3)
        self.add_button.pack(pady=5)

        self.cart_listbox = tk.Listbox(master, width=50, bg="#505050", fg="white")
        self.cart_listbox.pack(pady=5)

        self.total_label = tk.Label(master, bg="#505050", fg="white", font=(10), text='Kopējā cena: 0.00 EUR')
        self.total_label.pack(pady=10)
        
        self.clear_button = tk.Button(master, text="Dzēst grozu", bg="#505050", fg="white", font=(11), bd=3, command=self.clear_cart)
        self.clear_button.pack(pady=5)

        self.add_aizvert=Button(master, text="Aizvērt", bg="#505050", fg="white", font=(11), bd=3, command=master.destroy)
        self.add_aizvert.pack(pady=6)


    def add_to_card(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        quantity = float(self.quantity_entry.get())

        produkts = Product(name, price, quantity)
        self.cart.add_product_to_cart(produkts)
        self.cart_listbox.insert(tk.END, f"Produkts: {name} | Cena: {price} | EUR Daudzums: {quantity} gab")

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