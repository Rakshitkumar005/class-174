from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.geometry("900x500")
root.title("Food Oder")

burger=ImageTk.PhotoImage(Image.open("burger1.png"))
burger_image=Label(root)
burger_image["image"]=burger
burger_image.place(relx=0.7,rely=0.5,anchor=CENTER)

label1=Label(root,text="Rdonalds",font=("times",40,"bold"),fg="orange")
label1.place(relx=0.12,rely=0.1,anchor=CENTER)

label_dish=Label(root,text="Choose A Dish",font=("times",15))
label_dish.place(relx=0.06,rely=0.2,anchor=CENTER)

dish=["Burger","Iced_americano"]
dropDown_dish=ttk.Combobox(root,state="readonly",values=dish)
dropDown_dish.place(relx=0.25,rely=0.2,anchor=CENTER)

label_addOns=Label(root,text="Choose a Add Ons",font=("times",15))
label_addOns.place(relx=0.08,rely=0.5,anchor=CENTER)

toppings=[]
dropDown_addOns=ttk.Combobox(root,state="readonly",values=toppings)
dropDown_addOns.place(relx=0.25,rely=0.5,anchor=CENTER)

label_amount=Label(root)
label_amount.place(relx=0.2,rely=0.75,anchor=CENTER)

class Parent:
    def menu(dish):
        if(dish=="Burger"):
            print("You can add Chesse and Jalapeno")
            
        elif(dish=="Iced_americano"):
            print("You can add caramel and chocolate flavours")
            
    def final_amount(dish,add_ons):
        if(dish=="Burger" and add_ons=="Cheese"):
            print("You have to pay 250 USD")
             
        elif(dish=="Burger" and add_ons=="Jalapeno"):
             print("You have to pay 350 USD")
        
        if(dish=="Iced_americano" and add_ons=="caramel"):
             print("You have to pay 250 USD")
             
        elif(dish=="Iced_americano" and add_ons=="chocolate"):
             print("You have to pay 350 USD")
                        
class Child1(Parent):
    def __init__(self,dish):
       self.new_dish=dish 
        
    def get_menu(self):
        Parent.menu(self.new_dish)
        
class Child2(Parent):
    def __init__(self,dish,add_ons):
        self.new_dish=dish
        self.new_add_ons=add_ons
      
    def get_final_amount(self):
        Parent.final_amount(self.new_dish, self.new_add_ons)
   
cust1=Child1(dropDown_dish.get()) 
cust1.get_menu()        
             
cust2=Child2(dropDown_addOns.get(),dropDown_dish.get())            
cust2.get_final_amount()           
 
btn_amount=Button(root,text="Amount",command=cust2.get_final_amount)
btn_amount.place(relx=0.04,rely=0.6,anchor=CENTER) 

btn_addons=Button(root,text="Check Add Ons",command=cust1.get_menu)
btn_addons.place(relx=0.06,rely=0.3,anchor=CENTER) 

          
root.mainloop()