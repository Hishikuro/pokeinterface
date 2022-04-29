class PokeApi():
	def __init__(self ,nom):

		self.__nom = nom #nom du pokemon
		
		import requests 
		import json 

		rq1 = requests.get('https://pokeapi.co/api/v2/pokemon/'+self.__nom)
		data = json.loads(rq1.text)

		self.__id = data["id"] #ID de pokemon
		rq2 = requests.get('https://pokeapi.co/api/v2/pokemon-species/'+str(self.__id))
		data2 = json.loads(rq2.text) 

		
		self.__pm = data["sprites"]["front_default"] #photo male
		self.__pf = data["sprites"]["front_female"] #photo female
		
		self.__t = data["types"][0]["type"]["name"] #type
		self.__p = data["weight"] #poid
		self.__w = data ["height"] #taille

		self.__c = data2["genera"][7]["genus"] #categorie 
	def info(self) :
		return ([self.__nom,self.__id,self.__pm,self.__pf,self.__t,self.__p,self.__w ,self.__c])
	def repr(self):
		print(f"Le pokemon se nomme {self.__nom} son numero est le {self.__id} voici sa forme par default : {self.__pm} et sa forme femele : {self.__pf} il est de type {self.__t} avec un poid de {self.__p}  il mesure {self.__w } sa cathédori est {self.__c}")

if __name__ == '__main__':
	pokemon = PokeApi("pachirisu")
	print(pokemon.repr())