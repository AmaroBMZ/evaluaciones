subpago=0
pagototal=0
adescuento=0
pr=0
otr=0
pv=0
ae=0
while True:
    print("MENU")
    print("1. Pikachu Roll $4500")
    print("2. Otaku Roll $5000")
    print("3. Pulpo Venenoso Roll $5200")
    print("4. Anguila Eléctrica Roll $4800")
    print("5. Aplicar descuento")
    print("6. Pagar")
    opc=input("que desea?" )
    try:
        if opc=="1":
            subpago+=4500
            pr+=1
            print("se ha añadido un Pikachu Roll")
        elif opc=="2":
            subpago+=5000
            otr+=1
            print("se ha añadido un Otaku Roll")
        elif opc=="3":
            subpago+=5200
            pv+=1
            print("se ha añadido un Pulpo Venenoso Roll")
        elif opc=="4":
            subpago+=4800
            ae+=1
            print("se ha añadido un Anguila Eléctrica Roll")
        elif opc=="5":
            descuento=input("desea aplicar un codigo de descuento?")
            if descuento=="soyotaku":
                adescuento+=0.9
                print("se ha aplicado el descuento")
            else:
                print("no se ha aplicado el descuento")
        elif opc=="6":
            pago=subpago*adescuento
            print(f"Se lleva")
            print(f"{pr} Pikachu Roll")
            print(f"{otr} Otaku Roll")
            print(f"{pv} Pulpo Venenoso Roll")
            print(f"{ae} Anguila Eléctrica Roll")
            print("****************************")
            print(f"subtotal por pagar{subpago}")
            print(f"con un descuento de {adescuento}%")
            print(f"Pagando un total de ${pago}")
            break
    except ValueError:
        print("ingrese un valor valido")
