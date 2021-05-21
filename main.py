# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform

import netifaces


def serverdata():
    import platform
    hostname=platform.node()
    return(hostname)

def validatestatusc():
    import docker
    import schedule
    import time, os
    import psutil
    from colorama import init, Fore, Back, Style
    from pythonping import ping
    import netifaces


# Define tags to review if the container it is running.
    incodef="incodetech/ms-incodesmile-recognition-service:cpu"
    incodeinew="incodetech/incode-ine-gateway"
    incodeb="incodetech/nginx-loadbalancer"
# Define counters per each kind of container.
    incodefc=0
    incodeinewc=0
    incodebc=0

#process to validate how many contairner are running.
    client=docker.from_env()
    for container in client.containers.list():
        runc=container.attrs
        runc=str(runc)
        #print(runc )
        if runc.find(incodef) != -1:
           incodefc+=1
        elif runc.find(incodeinew) != -1:
           incodeinewc+=1
        elif runc.find(incodeb) != -1:
           incodebc+=1

    init(autoreset=True)
    alertfc="Contenedores de incodesmile corriendo: " + str(incodefc)
    alertinew="Contenedores de incode ine gateway correindo: " + str(incodeinewc)
    alertb="Contenedores de incode loadbalancer: " + str(incodebc)

    if incodefc == 2:
        alertfc=alertfc + "\t\t\tEs el numero correcto de contenedores."
        print(Style.BRIGHT + Back.GREEN + Fore.WHITE + alertfc)
    else:
        alertfc = alertfc + "\t\t\tNO es el numero correo de contenedores."
        print(Style.BRIGHT + Back.RED + Fore.WHITE + alertfc)

    if incodeinewc == 1:
        alertinew=alertinew + "\t\t\tEs el numero correcto de contenedores."
        print(Style.BRIGHT + Back.GREEN + Fore.WHITE + alertinew)
    else:
        alertinew = alertinew + "\t\t\tNO es el numero correo de contenedores."
        print(Style.BRIGHT + Back.RED + Fore.WHITE + alertinew)

    if incodebc == 1:
        alertb=alertb + "\t\t\t\tEs el numero correcto de contenedores."
        print(Style.BRIGHT + Back.GREEN + Fore.WHITE + alertb)
    else:
        alertb = alertb + "\t\t\t\tNO es el numero correo de contenedores."
        print(Style.BRIGHT + Back.RED + Fore.WHITE + alertb)
    gws = netifaces.gateways()
    for key, value in gws.items():
        gwp=ping(gws['default'][netifaces.AF_INET][0], count=10)
        if gwp.rtt_avg_ms < 0.1:
            print(Style.BRIGHT+Back.GREEN+Fore.WHITE+"Se tiene acceso al GW Local")
        else:
            print(Style.BRIGHT + Back.RED + Fore.WHITE + "No se tiene acceso al GW Local")
    f=open("network.conf","r")
    while True:
        count =+ 1
        line=f.readline()
        if not line:
            break
        service,value=line.split("=")
        service=str(service).strip()
        if service.find('INEGW') != -1:
            inewp=ping(value,count=10)
            if inewp.rtt_avg_ms < 0.1:
                gwine="Se tiene acceso al GW de la red INE"+value
                print(Style.BRIGHT + Back.GREEN + Fore.WHITE + gwine )
            else:
                gwine="No alcanza el GW o tiempos muy altos." + value
                print(Style.BRIGHT + Back.RED + Fore.WHITE+ gwine)
        if service.find('INCODEVPN') != -1:
            inewp=ping(value,count=10)
            if inewp.rtt_avg_ms < 0.1:
                gwinc="Se tiene acceso al GW de la VPN INCODE"+value
                print(Style.BRIGHT + Back.GREEN + Fore.WHITE + gwinc )
            else:
                gwinc="No alcanza el VPN de Incode o tiempos muy altos." + value
                print(Style.BRIGHT + Back.RED + Fore.WHITE+ gwinc)



def print_menu(hostname):
    import platform
    # Use a breakpoint in the code line below to debug your script.
    print(f'Consola de validación de servicios INCODE en el INE, Nodo - {hostname}.\n')
    print("El menu tiene la finalida de facilitar el soporte remoto de los servidores de comparación de incode.\n")
    print("Opciones:\n")
    print("1. Revisar estado de servicio(s).\n")
    print("2. Reinicar servidor.\n")
    print("3. Revisar disponibilidad de disco.\n")
    print("4. Recolectar bitacoras.")
    #menu=input("Indica la opción desada: ")
    menu="0"
    if menu == "0":
        validatestatusc()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host=serverdata()
    print_menu(host)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
