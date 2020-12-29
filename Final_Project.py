# Wasn't sure what to make and didn't receive a reply back so made this.. This is a program that lets the user add
# ingredients to their pizza. They can choose to add their own ingredient by using the entry box, typing in the
# ingredient and then clicking add ingredient. Or they could choose to use one of the pizza bases, and add from there.
# The user can also delete ingredients, save their ingredients, and load their ingredients.

import tkinter
import tkinter.messagebox

# GUI
root = tkinter.Tk()
root.title("Pizza Ingredients")
framez = tkinter.Frame(root)
framez.pack()
listbox = tkinter.Listbox(framez, height=10, width=55)
listbox.pack(side=tkinter.LEFT)

# Scrollbar
scrollbarz = tkinter.Scrollbar(framez)
scrollbarz.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scrollbarz.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbarz.set)


# Inheritance
class Pizza():
    def __init__(self, meat, sauce, dough, veggie):
        self.meat = meat
        self.sauce = sauce
        self.dough = dough
        self.veggie = veggie


class Pepperoni(Pizza):
    def __init__(self, meat, sauce, dough, veggie):
        super().__init__(meat, sauce, dough, veggie)


class Canadian_Bacon(Pizza):
    def __init__(self, meat, sauce, dough, veggie):
        super().__init__(meat, sauce, dough, veggie)


class Chicken_Artichoke(Pizza):
    def __init__(self, meat, sauce, dough, veggie):
        super().__init__(meat, sauce, dough, veggie)


# Function to add ingredients
def add_ingredient():
    ingredient = entry_ingredient.get()
    if ingredient != "":
        listbox.insert(tkinter.END, ingredient)
        entry_ingredient.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must add an ingredient.")


# Function to delete ingredients
def delete_ingredient():
    try:
        ingredient = listbox.curselection()[0]
        listbox.delete(ingredient)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select an ingredient.")


# Function to save ingredients
def save_ingredients():
    with open('ingredients.txt', 'w') as f:
        for i in listbox.get(0, tkinter.END):
            f.write(i + "\n")

            # Testing to see if properly writing listbox into file
            print(i)
        f.close()


# Function to load ingredients
def load_ingredients():
    ingredients = []
    with open('ingredients.txt') as f:
        ingredients = f.readlines()
        ingredients = [x.strip() for x in ingredients]

        # Testing to see if properly storing text into list
    print(ingredients)

    # This inserts what is loaded into listbox
    for i in range(len(ingredients)):
        listbox.insert(i + 1, ingredients[i])

        # Testing to see if properly inserting into listbox
        print(i)
        print(ingredients)

def pizza_presets():
    # This creates a popup window that contains the pizza presets
    global popup
    popup = tkinter.Toplevel(root)
    popup.title("Pizza Presets")
    popup.geometry("250x104")

    my_frame = tkinter.Frame(popup)
    my_frame.pack()

    button_pep = tkinter.Button(my_frame, text="Pepperoni Base", width=50, command=load_pep)
    button_pep.pack()

    button_bac = tkinter.Button(my_frame, text="Canadian Bacon Base", width=50, command=load_bac)
    button_bac.pack()

    button_art = tkinter.Button(my_frame, text="Chicken Artichoke Base", width=50, command=load_art)
    button_art.pack()

    button_exit = tkinter.Button(my_frame, text="Exit", width=50,command=popup.destroy)
    button_exit.pack()

# Function to load pepperoni preset
def load_pep():
    listbox.insert(tkinter.END, pepper.meat, pepper.sauce, pepper.dough, pepper.veggie)


# Function to load canadian bacon preset
def load_bac():
    listbox.insert(tkinter.END, bacon.meat, bacon.sauce, bacon.dough, bacon.veggie)


# Function to load chicken artichoke preset
def load_art():
    listbox.insert(tkinter.END, artichoke.meat, artichoke.sauce, artichoke.dough, artichoke.veggie)


# Creating the objects with arguments
pepper = Pepperoni("pepperoni", "red sauce", "wheat dough", "no veggies")
bacon = Canadian_Bacon("bacon", "red sauce", "gluten free dough", "pineapple")
artichoke = Chicken_Artichoke("chicken", "white sauce", "wheat dough", "artichoke")

# Creating the buttons
entry_ingredient = tkinter.Entry(root, width=50)
entry_ingredient.pack()

button_add_ingredient = tkinter.Button(root, text="Add ingredient", width=50, command=add_ingredient)
button_add_ingredient.pack()

button_delete_ingredient = tkinter.Button(root, text="Delete ingredient", width=50, command=delete_ingredient)
button_delete_ingredient.pack()

button_save_ingredients = tkinter.Button(root, text="Save ingredients", width=50, command=save_ingredients)
button_save_ingredients.pack()

button_load_ingredients = tkinter.Button(root, text="Load ingredients", width=50, command=load_ingredients)
button_load_ingredients.pack()

button_preset = tkinter.Button(root, text="Pizza Presets", width=50, command=pizza_presets)
button_preset.pack()

root.mainloop()