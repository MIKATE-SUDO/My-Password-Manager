import json
donnees = {
    "url": "https://exemple-site-1.com",
    "identifiant": "ton_pseudo",
    "mot_de_passe": "ton_mdp_secret"
}

choix = int(input("voulez vous cree un neauveau pass oui,1 ou non,0: "))
if choix == 1:
    print("vous avez choisi de créer un nouveau pass")
else:
    exit()

identifiant = input("veuillez choisir votre identifiant: ")
if len(identifiant) < 2:
    print("identifiant indisponible")
    exit()
else: print("identifiant disponible")

mot_de_passe = input("veuillez choisir votre mot de passe: ")
if len(mot_de_passe) > 1:
    print("mot de passe disponible")
    
else:
    print("mot de passe indisponible")
    exit()

url = input("veuillez entrer l'url du site: ")
if url.startswith("http://") or url.startswith("https://"):
    print("url valide")
else:
    print("url invalide")
donnees = {"site": url, "user": identifiant, "mdp": mot_de_passe}

# On ouvre le fichier 'passwords.json' pour écrire dedans
with open("passwords.json", "w") as fichier:
    # On pousse le dictionnaire 'donnees' à l'intérieur
    json.dump(donnees, fichier, indent=4)

print("✅ Terminé ! Va voir dans ton dossier, le fichier passwords.json est créé.")