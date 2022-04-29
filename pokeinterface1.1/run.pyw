import pygame 

from urllib.request import urlopen
import io 

from pokeapi import PokeApi

fichier = open("data.txt", "r")
nom = fichier.read()  # NOM
fichier.close()
pokemon = PokeApi(nom)

ID = "N." + str(pokemon.info()[1]) #ID

typ ="TYPE :" + pokemon.info()[4].capitalize() # type
poids = "WEIGHT : " +str(round(float(pokemon.info()[5]),2)) # poids
taille = "SIZE : " +str(round(float(pokemon.info()[6]),2))# taille
categorie =  str(pokemon.info()[7]) #categorie

imgDefault = pokemon.info()[2]
imgFemale = pokemon.info()[3]

white = (255, 255, 255)
ROUGE =(164, 164, 164) #33
VERT = (255,255,255) #43
BLEU = (66, 66, 66) #53
JAUNE = (48, 167, 215) #66
NOIR = (0, 0, 0) #70

colorID = "#FFFFFF"
colorNom = "#FFFFFF"

colorTyp = "#FFFFFF"
colorPoids = "#FFFFFF"
colorTaille = "#FFFFFF"
colorCategory = "#FFFFFF"

titre = "Pokemon [ EN ]"
url ="https://st2.depositphotos.com/3213441/12022/v/600/depositphotos_120226152-stock-illustration-pokemon-go-pokeball-round-sign.jpg"
x= 680
y= 540
icone =io.BytesIO(urlopen(url).read())


pygame.display.set_caption(titre) 

icone = pygame.image.load(icone)
pygame.display.set_icon(icone)

pygame.init()


screen = pygame.display.set_mode((x,y))
screen.fill(white)

pygame.draw.rect(screen, ROUGE, pygame.Rect(18, 20, 362, 360)) 
try:
    image_str1 = urlopen(imgDefault).read()
    image_file1 = io.BytesIO(image_str1)
    image1 = pygame.image.load(image_file1)
    image1 = pygame.transform.scale(image1, (362, 360))
    screen.blit(image1, (18, 20))
except Exception as e:
        pass




  
pygame.draw.rect(screen, VERT, pygame.Rect(420, 20, 240, 200)) 

try:

    image_str2 = urlopen(imgFemale).read()
    image_file2 = io.BytesIO(image_str2)
    image2 = pygame.image.load(image_file2)
    image2 = pygame.transform.scale(image2, (240, 200))
    screen.blit(image2, (420, 20))
except Exception as e:
        pass


pygame.draw.rect(screen, BLEU, pygame.Rect(21, 400, 359, 120)) 


police = pygame.font.Font(None,24)
texte = police.render(ID,True,pygame.Color(colorID))
screen.blit(texte,(21+10,400+10))


police = pygame.font.Font(None,359//(len(nom)-1))
texte = police.render(nom.upper(),True,pygame.Color(colorNom))
screen.blit(texte,(21+10 +(359//(len(nom))),400+10+24  ))


pygame.draw.rect(screen, JAUNE, pygame.Rect(420, 260, 240, 260)) 



pygame.draw.rect(screen, NOIR, pygame.Rect(440, 280, 200, 40)) 

police = pygame.font.Font(None,200*2//(len(typ)))
texte = police.render(typ,True,pygame.Color(colorTyp))
screen.blit(texte,(440+10 +(200*2//(len(typ))),280+10  ))

pygame.draw.rect(screen, NOIR, pygame.Rect(440, 344, 200, 40)) 

police = pygame.font.Font(None,200*2//(len(poids)))
texte = police.render(poids,True,pygame.Color(colorPoids))
screen.blit(texte,(440+10 +(200*2//(len(poids))),344+10  ))

pygame.draw.rect(screen, NOIR, pygame.Rect(440, 408, 200, 40)) 


police = pygame.font.Font(None,200*2//(len(taille)))
texte = police.render(taille,True,pygame.Color(colorTaille))
screen.blit(texte,(440+10 +(200*2//(len(taille))),408+10  ))

pygame.draw.rect(screen, NOIR, pygame.Rect(440, 472, 200, 40)) 

police = pygame.font.Font(None,200*2//(len(categorie)))
texte = police.render(categorie,True,pygame.Color(colorCategory))
screen.blit(texte,(440+(200*2//(len(categorie))),472+10  ))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit