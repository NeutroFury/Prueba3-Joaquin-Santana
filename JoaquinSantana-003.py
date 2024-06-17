def menu():
    print("-.-.-.-.-.-.- MENU -.-.-.-.-.-.-")
    print("")
    print("1.- Agregar plan")
    print("2.- Listar planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadisticas")
    print("")
    print("0.- Salir")
def agregar_plan():
    id=int(input("Ingrese id: \n"))
    nombre=input("Ingrese nombre: \n")
    porcentajelista=validar_porcentaje()
    if porcentajelista:
        if porcentajelista>=0 and porcentajelista<=25:
            categoria="Chiste"
            nueva_lista=[id,nombre,porcentajelista,categoria]
            lista.append(nueva_lista)
        elif porcentajelista>=26 and porcentajelista<=50:
            categoria="Anécdota"
            nueva_lista=[id,nombre,porcentajelista,categoria]
            lista.append(nueva_lista)
        elif porcentajelista>=51 and porcentajelista<=75:
            categoria="Peligro"
            nueva_lista=[id,nombre,porcentajelista,categoria]
            lista.append(nueva_lista)
        elif porcentajelista>=76 and porcentajelista<=99:
            categoria="Atención"
            nueva_lista=[id,nombre,porcentajelista,categoria]
            lista.append(nueva_lista)
        elif porcentajelista==100:
            categoria="Esclavitud"
            nueva_lista=[id,nombre,porcentajelista,categoria]
            lista.append(nueva_lista)
def validar_porcentaje():
    a=False
    porcentaje=int(input("Ingrese porcentaje de efectiviadad: \n"))
    if porcentaje>=0 and porcentaje<=100:
        nuevoporc=int(porcentaje)
        a=True
        return nuevoporc
    elif a==False:
        print("No se pudo agregar...")
def listar():
    print("")
    print("")
    print(".-.-.-.-.-.- LISTA PLANES -.-.-.-.-.-.")
    for x in lista:
            print(f"ID: {x[0]}  Nombre: {x[1]}  Porcentaje: {x[2]}%  Categoria: {x[3]}")
    print("")
    print("")
    print(" -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
def eliminar_plan():
    print("")
    print("-.-.-.-.- ELIMINAR PLAN -.-.-.-.-.")
    preg=int(input("Ingrese ID a eliminar: \n"))
    for x in lista:
        if int(x[0])==preg:
            verificarr=verificar()
            if verificarr:
                lista.remove(x)
                print("Se eliminó correctamente...")
def verificar():
    q=False
    pregverificar=input("Desea eliminar?: (si/no)").lower()
    if pregverificar=="si" or pregverificar=="s":
        si=pregverificar
        q=True
        return si
    elif q==False:
        print("No se eliminó")
def generar_csv():
    print("")
    print("-.-.-.- GENERAR CSV -.-.-.-")
    print("")
    with open('planes.csv', 'w',newline='') as planes:
        escritor_csv=csv.writer(planes)
        escritor_csv.writerow(['Id','Nombre','Porcentaje','Categoria'])
        escritor_csv.writerows(lista)
        print("Archivo generado correctamente...")
def cargar_csv():
    print("")
    print("-.-.-.- CARGAR CSV -.-.-.-")
    lista.clear()
    with open('planes.csv', 'r',newline='') as planes:
        lector_csv=csv.reader(planes)
        for x in lector_csv:
            lista.append(x)
        lista.pop(0)
        print("Cargado correctamente...")
def estadistica():
    print("")
    print(".-.-.-.-.- ESTADISTICAS -.-.-.-.-.")
    print("")
    total=0
    max=0
    for x in lista:
        total=total+int(x[2])
        if int(x[2])>max:
            max=int(x[2])
    largo=len(lista)
    prom=total/largo
    print("El porcentaje de efectividad promeido es: ",prom)
    print("Valor del porcentaje de efectividad más alto es: ", max)       
import csv
lista=[]
while True:
    try:
        menu()
        op=int(input("Ingrese opción: \n"))
        if op==1:
            agregar_plan()
        elif op==2:
            print("")
            listar()
        elif op==3:
            print("")
            eliminar_plan()
        elif op==4:
            print("")
            generar_csv()
        elif op==5:
            print("")
            cargar_csv()
        elif op==6:
            print("")
            estadistica()
        elif op==0:
            print("Adios....")
            break
        else:
            print("Ingrese opción válida")
    except:
        print("Error...")






