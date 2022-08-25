from Unicode_letters import *
import tkinter as tk

### Future indicative

### Things to add/change:
###     accents on labels
###     button to show conjugated verb
###     only select one radiobutton at a time
###     add documentation
###     check for irregulars

window = tk.Tk()

window.title('Verb Conjugator')

### variables for radiobuttons
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

## Verb Label
lbl_verb = tk.Label(text = "Verb")
lbl_verb.pack()

### Verb Entry
ent_verb = tk.Entry()
ent_verb.pack()

### Pronoun Label
lbl_pronoun = tk.Label(text = "Select the subject pronoun")
lbl_pronoun.pack()


"""
yo -'e
tu -'as
usted/el/ella -'a
nosotros -emos
vosotros -'eis
ustedes/ellos/ellas -'an
"""

def future_yo(verb):
    future = verb + e_accent
    return future

def future_tu(verb):
    future = verb + a_accent + 's'
    return future

def future_el(verb):
    future = verb + a_accent
    return future

def future_nos(verb):
    future = verb + 'emos'
    return future

def future_vos(verb):
    future = verb + e_accent + 'is'
    return future

def future_ellos(verb):
    future = verb + a_accent + 'n'
    return future

def select():
    verb = ent_verb.get()
    if var1.get() == 1:
        lbl_results.config(text = future_yo(verb))
    if var2.get() == 2:
        lbl_results.config(text = future_tu(verb))
    if var3.get() == 3:
        lbl_results.config(text = future_el(verb))
    if var4.get() == 4:
        lbl_results.config(text = future_nos(verb))
    if var5.get() == 5:
        lbl_results.config(text = future_vos(verb))
    if var6.get() == 6:
        lbl_results.config(text = future_ellos(verb))

R1 = tk.Radiobutton(window, text="Yo", variable=var1, value=1, command=select)
R1.pack()

R2 = tk.Radiobutton(window, text="Tu", variable=var2, value=2, command=select)
R2.pack()

R3 = tk.Radiobutton(window, text="El/Ella/Usted", variable=var3, value=3, command=select)
R3.pack()

R4 = tk.Radiobutton(window, text="Nosotros", variable=var4, value=4, command=select)
R4.pack()

R5 = tk.Radiobutton(window, text="Vosotros", variable=var5, value=5, command=select)
R5.pack()

R6 = tk.Radiobutton(window, text="Ellos/Ellas/Ustedes", variable=var6, value=6, command=select)
R6.pack()


lbl_results = tk.Label(text = '')
lbl_results.pack()


window.mainloop()

