from tkinter import *

fen = Tk()
fen.title('CHOIX')
fen.geometry('300x50')

def check(*args):
	fichier = open("data.txt", "w")
	fichier.write(variable.get())
	fichier.close()
    

variable = StringVar(value='')
variable.trace('w', check)


# choices available with user.
import requests 
import json 

rq1 = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
data = json.loads(rq1.text)


pokemon = []
for x in range(data["count"]):
	pokemon.append(data["results"][x]["name"])
pokemon = sorted(pokemon)
variable.set(pokemon[6])

dropdown = OptionMenu(
    fen,
    variable,
    *pokemon
)
# positioning widget
dropdown.pack(expand=True)

bouton = Button(fen, text="QUITTER", command=fen.quit)
bouton.pack()


# infinite loop 
fen.mainloop()
