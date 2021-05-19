# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform


def serverdata():
    import platform
    hostname=platform.node()
    return(hostname)

def validatestatus():
    import docker
    import schedule
    import time, os
    import psutil

    incodef="incodetech/ms-incodesmile-recognition-service:cpu"
    incodeinew="incodetech/incode-ine-gateway"
    incodefc=0
    incodeinewc=0


    client=docker.from_env()
    for container in client.containers.list():
        runc=container.attrs
        runc=str(runc)
        #print(runc )
        if runc.find(incodef) != -1:
           incodefc+=1
        elif runc.find(incodeinew) != -1:
           incodeinewc+=1

    alertinc="Contenedores de incodesmile corriendo: " + str(incodefc) + "\nContenedores de incode ine gatewau correindo: " + str(incodeinewc)
    print(alertinc)

    PROCNAME={"docker","podman","java"}
    ppodman=0
    pjava=0
    pdocker=0
    for proc in psutil.process_iter():
        for idp in PROCNAME:
             if proc.name().find(idp) != -1:
                 if idp == "java":
                    pjava=+1

                 elif idp == "podman":
                     ppodman=+1

                 elif idp == "docker":
                     pdocker=+1


    print("java " + str(pjava) + " docker " + str(pdocker) + "  podman " + str(ppodman))


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
        validatestatus()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host=serverdata()
    print_menu(host)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
