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

liste_sous_titres = list(req.json()['events'])
for i in range(len(liste_sous_titres)):
    sous_titre = liste_sous_titres[i]['segs'][0]['utf8']
    sous_titres_video += f"{sous_titre} "
    ecriture_sous_titres_fichier_texte(sous_titres_video.replace(str("\u0301"), "e"))

print(sous_titres_video)