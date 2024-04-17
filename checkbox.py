from tkinter import *


def display():
    if (x.get()):
        print("Zaznaczono zgode")
    else:
        print("Odznaczono zgode")


window = Tk()

image = PhotoImage(file='Zrzut ekranu 2024-03-05 194020.png')
x = BooleanVar()

check_button = Checkbutton(window,
                           text="Do you agree ?",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 30),
                           fg='red',
                           bg='black',
                           activeforeground='red',
                           activebackground='black',
                           padx=30,
                           pady=15,
                           image=image,
                           compound='left',




                           )

check_button.pack()
window.mainloop()
