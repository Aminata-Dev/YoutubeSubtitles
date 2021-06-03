#Youtube video > Inspect > Network > Settings > Subtitles > English > Go back to Network > Double click on the "timedtext" file and put the link on the console

import json
import requests
import os

def ecriture_sous_titres_fichier_texte(video):
    with open("youtubesubtitles.txt", 'w') as fichier: #creation du fichier texte
            fichier.write(video)

sous_titres_video = ''

url = input("URL ?\n@> ")
req = requests.get(url)
# liste = []

liste_sous_titres = list(req.json()['events'])
for i in range(len(liste_sous_titres)):
    # print(liste_sous_titres[1]['segs'])
    try:
        for j in range(len(liste_sous_titres[i]['segs'])): #certaines listes segs contiennent plusieurs sous titres
            sous_titre = liste_sous_titres[i]['segs'][j]['utf8']
            if sous_titre != '\n':
                sous_titres_video += f"{sous_titre} "
                # liste.append(sous_titre)
    except KeyError: #le premier evenement n'est pas toujours un sous titre
        pass

ecriture_sous_titres_fichier_texte(sous_titres_video.replace(str("\u0301"), "e"))
print(sous_titres_video)
# print(liste)