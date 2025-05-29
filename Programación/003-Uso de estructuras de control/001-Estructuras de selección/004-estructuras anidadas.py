edad = 47

if edad < 20:
    print("Eres un niño")
    if edad < 10:
        print("Eres un niño pequeño")
    else:
        print("Eres un niño mayor")
elif edad >= 20 and edad < 30:  
    print("Eres un joven")
    if edad < 25:
        print("Eres un joven menor de 25")
    else:
        print("Eres un joven mayor de 25")
