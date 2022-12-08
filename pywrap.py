
#! librerias 

import git 
from git import Repo
import os 
import time 
import math
from colorama import Back, init, Fore


repo = "https://github.com/ujjwal96/xwinwrap.git"

#! funcion para setear el wallpaper
def SetVW(videoPath):
      CMND = "sudo xwinwrap -fs -fdt -ni -b -nf -un -o 1.0 -debug -- mpv -wid WID --loop --no-audio " + videoPath
      os.system(f"{CMND} > /dev/null 2>&1 &")

# ! funcion para clonar el repositorio y las dependencias 
def repoClone(repo,videoPath):
  
  if(os.path.exists("pywrap") == False  ):
    os.mkdir("pywrap")
    os.chdir("pywrap")
    path = os.getcwd()
    Repo.clone_from(f"{repo}",f"{path}")
  else:
    
    CMND2 = "-fs -fdt -ni -b -nf -un -o 1.0 -debug -- mpv -wid WID --loop --no-audio " + videoPath
    os.system(f"/usr/local/bin/xwinwrap {CMND2} > /dev/null 2>&1 &")
    print("\n")
    respuesta = input("Desea añadir la configuracion a su window manager? (s/n): ")
    setupWM(respuesta, videoPath)
    exit()
    
   

#! funcion para compilar el programa
def compFile():
    os.system("make 1> /dev/null && sudo make install 1> /dev/null && make clean 1> /dev/null && clear")
   




# ! Funcion para configurar el WM
def setupWM(respuesta,videoPath):
    if(respuesta == "s"):
      print("\n")
      wm = input("cual es su window manager? (bspwm/i3): ")
      
      if(wm == "i3"):
        os.system(f"echo 'exec xwinwrap -fs -fdt -ni -b -nf -un -o 1.0 -debug -- mpv -wid WID --loop --no-audio {videoPath}' >> $HOME/.config/i3/config")
      
      elif(wm == "bspwm"):
        os.system(f"echo 'xwinwrap -fs -fdt -ni -b -nf -un -o 1.0 -debug -- mpv -wid WID --loop --no-audio {videoPath}' >> $HOME/.config/bspwm/bspwmrc")
    
    else:
      print("\n")
      print("Gracias por usar el script :) ")






init()

print("\n")
print("\n")
print("\n")
print("\n")


def barra_progreso(progreso, total):
    porcentaje = 100 * (progreso / float(total)) #! calcula el porcentaje
    bar = (Back.GREEN+' '+Back.RESET) * int(porcentaje) + '-' * (100 - int(porcentaje)) #! define la barra
    print(f"\r | {bar} {porcentaje:.2f}%|", end="\r") #! muestra barra + porcentaje
    

#! genera lista de valores 
numeros = [x * 5 for x in range(1000,3000)]

#! resultados
resultados = []

#! realiza calculos
for i, x in enumerate(numeros):
    resultados.append(math.factorial(x))
    barra_progreso( i + 1, len(numeros)) #! llamada a la funcion 'barra_progreso'

os.system("sleep 3 && clear")
print("\n")

print(Fore.GREEN +"""                          -----------------------------------
                          !!    Installation Successfull   !!
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




videoPath = input("Ingrese la ruta del video: ")


repoClone(repo,videoPath)


videoPath = input("Ingrese la ruta del video: ")
print("\n")
respuesta = input("Desea añadir la configuracion a su window manager? (s/n): ")

setupWM(respuesta, videoPath)
SetVW(videoPath)




# ! con <3 por ninj4