nom = input("Enter your name : ")
age = input("Enter your age : ")

try:
    int(age)+1
except:
    print("Erreur: Enter a valid age !")