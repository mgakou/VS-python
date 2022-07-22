import random
"""def demander_nom():
    reponse_nom = ""
    while not reponse_nom:
        reponse_nom = input("Entrer votre nom : ")
    return reponse_nom

def afficher_info_personne(nom,age) :
    if age < 10 :
        print("Vous etes un enfant")
    elif age ==17:
        print("Vous vous appelez " +nom +", vous avez " + str(age) + " ans"+ " et vous etes presque majeur")
    elif age < 17 and age >=10:
        print("Vous vous appelez " +nom +", vous avez " + str(age) + " ans"+ " et vous etes mineur")
    
    elif age==18:
        print("Vous vous appelez " +nom +", vous avez " + str(age) + " ans"+ " et vous etes juste majeur : Felicitation")
    elif age > 60:
        print("Vous etes senior")
    else :
        print("Vous vous appelez " +nom +" ,vous avez " + str(age) + " ans"+" et vous etes majeur")
    print("Vous aurez "+ str(age+1) + " ans")

def demander_age(nom_personne):
    age_int=0
    while age_int==0:
        age_str = input(nom_personne+ " entrer votre age : ")
        try:
            age_int = int(age_str)
        except :
            print("ERREUR ")
    return age_int
nom = demander_nom()
nom1 = demander_nom()

age = demander_age(nom)
age1 = demander_age(nom1)

afficher_info_personne(nom,age)
afficher_info_personne(nom1,age1)"""

NOMBRE_MIN =1
NOMBRE_MAX = 10
def poser_question():
    
    drapeau = True
    while drapeau:
        a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
        b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
        user_input = int(input("Calculez " + str(a) + " + " + str(b)  +" = "))
        if user_input == a+b :
            print("Resultat correct")
            print()
            user_input_2 = input("Tu veux continuer ? oui / non ?")
            if user_input_2 == "non":
                print("c'est terminé")
                break
        else:
            drapeau = False
    else :
        print("T'a menti")
poser_question()