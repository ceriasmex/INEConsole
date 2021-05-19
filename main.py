# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import platform


def serverdata():
    import platform
    hostname=platform.node()
    return(hostname)

def validatestatus():
    import schedule
    import time, os
    import psutil

    PROCNAME="docker"



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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    host=serverdata()
    print_menu(host)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
