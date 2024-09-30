import random
import string

def generer_mot_de_passe(taille=12):
  
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
  
    mot_de_passe = ''.join(random.choice(caracteres) for i in range(taille))
    
    return mot_de_passe

if __name__ == "__main__":
    taille_mot_de_passe = 16 
    mot_de_passe = generer_mot_de_passe(taille_mot_de_passe)
    print("Mot de passe généré:", mot_de_passe)
