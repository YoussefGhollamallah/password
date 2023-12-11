import hashlib
import json

def mdp():
    while True:
        password = input("Veuillez entrer un mot de passe : ")
        majuscule = False
        minuscule = False
        numbers = False
        specialChar = False

        if len(password) < 8:
            print("Votre mot de passe doit contenir au moins 8 caractères")
            continue

        for j in range(len(password)):
            if password[j] >= "a" and password[j] <= "z":
                minuscule = True
            elif password[j] == "#" or password[j] == "!" or password[j] == "@" or password[j] == "$" or password[j] == "&" or password[j] == "?" or password[j] == ".":
                specialChar = True

        for i in range(len(password)):
            if password[i] >= "A" and password[i] <= "Z":
                majuscule = True
            if password[i] >= "0" and password[i] <= "9":
                numbers = True

        if majuscule and minuscule and numbers and specialChar:
            print("Votre mot de passe a bien été créé")
            hashure = password.encode()
            hasha = hashlib.sha256(hashure).hexdigest()
            print(hasha)
            break
        else:
            print("Votre mot de passe ne satisfait pas les critères, veuillez entrer un nouveau mot de passe.")

    with open("password.json", "r") as f:
        data = json.load(f)

   
    if "password" not in data:
        data["password"] = []

    data["password"].append(hasha)

    with open("password.json", "w") as f:
        json.dump(data, f, indent=2)

mdp()
