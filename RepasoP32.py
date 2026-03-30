print("Super calculadora de sueldo :)")
print("© Polonius inc. 2026")
print("")
carnes = True
while carnes is True:
    try:
        sueldx = 0
        horx = 0
        diex = 0

        horx = int(input("Insertar horas por día: "))
        sueldx = float(input("Ahora, ingrese cuanto le pagan por hora: "))
        diex = int(input("Ingrese cuantos días a la semana trabaja: "))
        if horx > 24 or diex > 7:
            print("ERROR, Usted ha insertado su cantidad de horas o días mal!")
        else:
            carnes = False
    except ValueError:
        print("ERROR, Usted ha insertado algun caracter erroneo!")
        
print(f"Usted gana {(sueldx * horx) * diex}$ por semana.")


