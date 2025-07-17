import random as EA
import random as EB
gol_a=EA.randint(0,9)
gol_b=EB.randint(0,9)
print(gol_a)
print(gol_b)
apuesta_a=int(input("ingrese su apuesta para el equipo A "))
apuesta_b=int(input("ingrese su apuesta para el equipo B "))
predi_a=0
predi_b=0
premio=0
if apuesta_a==gol_a and apuesta_b==gol_b:
    print("has tenido una prediccion exacta recibes un x20")
    predi_a+=20
elif apuesta_a>gol_b or apuesta_b>gol_a:
    print("tu prediccion es correcta pero no exacta recibes un x10")
    predi_b+=10
else:
    print("no has acertado no recibes nada")
premio1=apuesta_b or apuesta_a
premio2=predi_b + predi_a
premio=premio2 * premio1
print(f"recibes {premio} de premio")