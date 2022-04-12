from random import randint
import os

print("COMBATE POKEMON")
op = input("(S)Sólo, (M)Multijugador: ")

if op == "S":
    vida_pikachu = 80
    vida_squirtle = 90

    while vida_pikachu > 0 and vida_squirtle > 0:
        #turno pikachu
        print("Turno de pikachu")
        ataque_pikachu = randint(1, 2)
        if ataque_pikachu == 1:
            print("Pikachu ataca con bola voltio")
            vida_squirtle -= 10
        else:
            print("Pikachu ataco con onda trueno")
            vida_squirtle -= 11
        
        print("La vida de pikachu es {}, y la de squirtle es {}".format(vida_pikachu,vida_squirtle))

        input("Pulsa enter para continuar...\n")
        os.system("cls")

        #turno squirtle
        ataque_squirtle = None
        while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "S":
            ataque_squirtle = input("(P)Placaje, (S)Surf, (A)Agua lodosa, elige ataque: ")
            
        if ataque_squirtle == "P":
            print("Squirtle uso placaje")
            vida_pikachu -= 7
        elif ataque_squirtle == "A":
            print("Squirtle uso agua lodosa")
            vida_pikachu -= 10
        elif ataque_squirtle == "S":
            print("Squirtle uso Surf")
            vida_pikachu -= 14

        print("La vida de pikachu es {}, y la de squirtle es {}".format(vida_pikachu,vida_squirtle))

        input("Pulsa enter para continuar...\n")
        os.system("cls")

    if vida_pikachu > vida_squirtle:
        print("Pikachu gana")
    else:
        print("Squirtle gana")

elif op == "M":
    vida_pikachu = 80
    vida_squirtle = 90

    while vida_pikachu > 0 and vida_squirtle > 0:
        #turno pikachu
        print("Turno de pikachu")
        ataque_pikachu = None
        while ataque_pikachu != "R" and ataque_pikachu != "T" and ataque_pikachu != "C":
            ataque_pikachu = input("(R)Rayo, (T)Trueno, (C)Cola ferrea, elige ataque: ")

        if ataque_pikachu == "R":
            print("Pikachu uso rayo")
            vida_squirtle -= 10
        elif ataque_pikachu == "T":
            print("Pikachu uso trueno")
            vida_squirtle -= 14
        elif ataque_pikachu == "C":
            print("Pikachu uso cola ferrea")
            vida_squirtle -= 6
        
        print("La vida de pikachu es {}, y la de squirtle es {}".format(vida_pikachu,vida_squirtle))

        input("Pulsa enter para continuar...\n")
        os.system("cls")

        #turno squirtle
        ataque_squirtle = None
        while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "S":
            ataque_squirtle = input("(P)Placaje, (S)Surf, (A)Agua lodosa, elige ataque: ")
            
        if ataque_squirtle == "P":
            print("Squirtle uso placaje")
            vida_pikachu -= 7
        elif ataque_squirtle == "A":
            print("Squirtle uso agua lodosa")
            vida_pikachu -= 10
        elif ataque_squirtle == "S":
            print("Squirtle uso Surf")
            vida_pikachu -= 14

        print("La vida de pikachu es {}, y la de squirtle es {}".format(vida_pikachu,vida_squirtle))

        input("Pulsa enter para continuar...\n")
        os.system("cls")

    if vida_pikachu > vida_squirtle:
        print("Pikachu gana")
    else:
        print("Squirtle gana")
