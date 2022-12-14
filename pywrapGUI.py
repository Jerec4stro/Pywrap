
#! librerias

import git
from git import Repo
import os
import time
import math
from colorama import Back, init, Fore
import tkinter as tk
from tkinter import filedialog


repo = "https://github.com/ujjwal96/xwinwrap.git"

#! funcion para clonar y compilar el repositorio


def repo_clone():
    if (os.path.exists("pywrap") == False):
        os.mkdir("pywrap")
        os.chdir("pywrap")
        path = os.getcwd()
        Repo.clone_from(f"{repo}", f"{path}") and os.system(
            "make 1> /dev/null && sudo make install 1> /dev/null && make clean 1> /dev/null && clear")

    elif (os.path.exists("pywrap") == True):
        print("Ya tiene instaladas todas las dependencias")


#! funcion para setear el wallpaper
def SetVW(videoPath):
    CMND = "xwinwrap -fs -fdt -ni -b -nf -un -o 1.0 -debug -- mpv -wid WID --loop --no-audio " + videoPath
    os.system(f"{CMND} > /dev/null 2>&1 &")
    exit()


#! Instancia de la clase Tk
root = tk.Tk()
root.geometry("500x300+100+100")

#! funcion que ejecuta ambas funciones


def seleccionar_archivo_y_setear_wallpaper():
    videoPath = filedialog.askopenfilename()
    SetVW(videoPath=videoPath)


#! _Botón que llamará a la nueva funcion cuando se haga click en el

button = tk.Button(root, text="Seleccione el video",
                   command=seleccionar_archivo_y_setear_wallpaper)


#! Barra de progreso

def barra_progreso(progreso, total):
    porcentaje = 100 * (progreso / float(total))  # ! calcula el porcentaje
    bar = (Back.GREEN+' '+Back.RESET) * int(porcentaje) + \
        '-' * (100 - int(porcentaje))  # ! define la barra
    # ! muestra barra + porcentaje
    print(f"\r | {bar} {porcentaje:.2f}%|", end="\r")


#! genera lista de valores
numeros = [x * 5 for x in range(1000, 3000)]

#! resultados
resultados = []

#! realiza calculos
for i, x in enumerate(numeros):
    resultados.append(math.factorial(x))
    # ! llamada a la funcion 'barra_progreso'
    barra_progreso(i + 1, len(numeros))


print("\n")
print("\n")
print("\n")
print("\n")



print(Fore.GREEN +"""                          -----------------------------------
                          !!    Bienvenidx a PyWrap       !!
                          -----------------------------------   """)


# ! banner 

print("\n")
print("\n")
print(Fore.GREEN +"""                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'""")
print("""                                                  by ninj4""")
print("\n")
print("\n")
print("\n")
print("\n")



repo_clone()

button.pack()

root.mainloop()
