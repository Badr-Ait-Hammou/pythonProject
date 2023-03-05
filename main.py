gestion_stock={}

while True:
    print("**************menu gestion de stock************")
    print("1.ajouter un article")
    print("2.retirer un article")
    print("3.afficher le stock")
    print("4.quitter le programme")

    choix=input("veuillez saisir votre choix :")
    if choix=='1':
        nom=input("saisir le nom de l'article : ")
        prix_un=int(input("saisir le prix de l'article : "))
        qtt=int(input("saisir la qtte disponible de l'article : "))
        if nom in gestion_stock: #le nom c'est l'id
            gestion_stock[nom]["qtt"]=gestion_stock[nom]["qtt"]+qtt
            gestion_stock[nom]["prix_un"]=gestion_stock[nom]["prix_un"]+prix_un
        else:
            gestion_stock[nom]={"qtt":qtt,"prix_un":prix_un}

    elif choix=="2":
         nom=input("saisir le nom de l'article a supprimer : ")
         if nom in gestion_stock:
            del gestion_stock[nom]
         else:
             print("ce nom ou bien cet article n'existe pas dans le stock")
    elif choix=="3":
        print("*********stock********")
        total=0
        for nom, produit in gestion_stock.items():
            quantite = produit["qtt"]
            prix_un = produit["prix_un"]
            valeur_total = qtt * prix_un
            total =total+valeur_total
            print(f"{nom}: {qtt}pcs x {prix_un}dh = {valeur_total}dh")
        print(f"Valeur totale du stock: {total}dh")

    elif choix=="4":
        break
    else:
        print("veuillez choisir un choix valide")


