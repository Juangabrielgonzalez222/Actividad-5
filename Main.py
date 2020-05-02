import csv
from clase import Alumno
if __name__ =='__main__':
    #Funciones menu de opciones:
    def op1(lista):
        año=int(input("Ingresa año: "))
        division=input("Ingresa division:")
        print("{0:<10}                   {1:^5}".format("Alumno","Porcentaje"))
        for alumno in lista:
            if(alumno.Retorna_Año()==año and alumno.Retorna_Division()==division):
                inasistencias=alumno.Retorna__Inasistencias()
                maximo=alumno.RetornaMaximoInasistencias()
                if inasistencias > maximo :
                    if (maximo!=0):
                        porcentaje=(inasistencias*100)/maximo
                        print("{:<19}            {:^5.1f}%".format(alumno.Retorna_nombre(),porcentaje))
                    else:
                        print("No se puede dividir por 0")
    def op2():
        maximo=int(input("Ingresa el maximo de inasistencias nuevo:"))
        Alumno.maximo_inasistencias=maximo
        print("Se establecio el nuevo valor:",maximo)
    def op3():
        test=Alumno()
        test.Test()
    def op4():
        print("Usted salio del programa")
    lista=[]
    bandera=0
    archivo=open("alumnos.csv")
    reader=csv.reader(archivo,delimiter=";")
    for fila in reader:
        if(bandera==0):
            bandera=1
        else:
            lista.append(Alumno(fila[0],int(fila[1]),fila[2],int(fila[3])))
    op=None
    dicdeopciones={1:op1,2:op2,3:op3,4:op4}
    while (op!=4):
        print("Menu:")
        print("Ingresa 1 para obtener un listado con los alumnos que superan el maximo de inasistencias")
        print("Ingresa 2 para modificar cantidad maxima insasistencias ")
        print("Ingresa 3 para llevar a cabo un test")
        print("Ingresa 4 para salir")
        op=int(input("Ingresa opcion:"))
        opcion=dicdeopciones.get(op,lambda:print("Opcion ingresada erronea rango 1-3, 3 para salir"))
        if op == 1:
            opcion(lista)
        else:
            opcion()