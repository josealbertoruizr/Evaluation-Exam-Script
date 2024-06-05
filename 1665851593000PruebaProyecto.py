
from colorama import Fore,Back,Style,init
import pygame

#Resetea cada vez que pones un color
init(autoreset=True)
import math
import colorsys
from pygame import *
import sys

import random
#Aclarar donde esta el archivo
import pandas as pd
import openpyxl

path_excel= "/Users/joseruiz/Desktop/proyecto final/excelproyectofinal.xlsx"

#Opciones de temas
corre= True
puntaje=0
while corre==True:
    respuesta=0
    print()
    print(Fore.LIGHTBLACK_EX + 'A: Matemáticas')
    print(Fore.LIGHTBLACK_EX + 'B: Ciencias')
    print(Fore.LIGHTBLACK_EX + 'C: Lectura')
    print(Fore.LIGHTMAGENTA_EX + 'P: PREMIO')
    print(Fore.CYAN + 'E: Salir del Exámen')
    print(Fore.YELLOW +'Puntaje: ',puntaje)
    seccion = str(input('Selecciona que inciso quieres repasar para tu exámen PISA: '))


    #----------------------------ABRE MATE-----------------------------------
    #Programa cuando selecciona MATE
    if seccion == 'A' or seccion=='a':
        df = pd.read_excel(path_excel,sheet_name= 'Matemáticas' )
        #Columnas de preguntas y respuestas   
        
        columna1_mate= df["preguntas"].to_list()
        columna2_mate= df["respuestas"].to_list()
        columna3_mate= df ["correcion"].to_list()
        for i in range(len(columna1_mate)):
            print()
            print(columna1_mate[i])
            intentos=1
            respuesta= float(input("Respuesta (solo el número): "))
            while respuesta != columna2_mate[i] and intentos<3:
                
                print(Fore.RED + "Respuesta incorrecta: ")
                intentos+=1
                respuesta= float(input("Respuesta (solo el número): "))

            if respuesta != columna2_mate[i] and intentos==3:
                #Printea como la respuesta y la explicación
                print(columna3_mate[i])
                print()

            if respuesta == columna2_mate[i]:
                print( Fore.GREEN + "¡ C O R R E C T A !")
                puntaje+=1
                print(Fore.YELLOW + 'Puntaje: ',puntaje)
                print()
                
        #----------------------------CIERRA MATE-----------------------------------



        #----------------------------ABRE CIENCIAS-----------------------------------
     #Programa cuando selecciona CIENCIAS
    elif seccion == 'B' or seccion=='b':
        ciencias = pd.read_excel(path_excel, sheet_name= 'Ciencias' )

        #Columnas de preguntas y respuestas  CIENCIAS
        columna1_ciencias= ciencias["preguntasb"].to_list()
        columna2_ciencias= ciencias["respuestasb"].to_list()
        columna3_ciencias= ciencias["explicaciónb"].to_list()

        for i in range(len(columna1_ciencias)):
            print()
            print(columna1_ciencias[i])
            intentos=1
    #------IMAGEN PARA PREGUNTA CIENCIAS 6 o 7 en la columna de excel---------   
            if i == 5:
                init()
                screen = display.set_mode((500,600))
                imagen= image.load(r'/Users/joseruiz/Desktop/proyecto final/ADN biologia.png')
                imagen = transform.scale(imagen,(500,600))

                while True:
                    for e in event.get():
                        if e.type == QUIT: sys.exit()
                
                    screen.blit(imagen,(0,0))
                    display.flip()
                    break     
#--------------------------CIERRA BLOQUE DE CODIGO IMAGEN---------------------------------------- 

            respuesta= str(input("Respuesta : "))
            while respuesta != columna2_ciencias[i] and intentos<3:
                
                print(Fore.RED + "Respuesta incorrecta: ")
                print()
                print('Revisa que tu respuesta este escrita con la primera letra mayuscula')
                intentos+=1
                respuesta= str(input("Respuesta (con mayúsculas): "))

            if respuesta != columna2_ciencias[i] and intentos==3:
                #Printea como la respuesta y la explicación
                print()
                print(columna3_ciencias[i])
                print()

            if respuesta == columna2_ciencias[i]:
                print( Fore.GREEN + "¡ C O R R E C T A !")
                puntaje+=1
                print(Fore.YELLOW + 'Puntaje: ',puntaje)
                print()
#----------------------------CIERRA CIENCIAS-----------------------------------
            
    

        
    #----------------------------ABRE LECTURA-----------------------------------
    #Columna de preguntas y respuestas LECTURA
    elif seccion == 'C' or seccion == 'c':
        lectura = pd.read_excel(path_excel,sheet_name= 'Lectura' )
        columna1_lect= lectura["preguntas"].to_list()
        columna2_lect= lectura["respuestas"].to_list()
        columna3_lect= lectura["correcion"].to_list()

        for i in range(len(columna1_lect)):
            print()
            print(columna1_lect[i])
            intentos=1

 #------IMAGEN PARA PREGUNTA CIENCIAS 6 o 7 en la columna de excel---------   
            if i == 0:
                
                init()
                screen = display.set_mode((500,600))
                imagen= image.load(r'/Users/joseruiz/Desktop/proyecto final/Grafitti.png')
                imagen = transform.scale(imagen,(500,600))
                
                while True:
                    for e in event.get():
                        if e.type == QUIT: sys.exit()
                
                    screen.blit(imagen,(0,0))
                    display.flip()
                    break
             
            elif i == 1:
                init()
                screen = display.set_mode((500,600))
                imagen= image.load(r'/Users/joseruiz/Desktop/proyecto final/El lago chaang.png')
                imagen = transform.scale(imagen,(500,600))

                while True:
                    for e in event.get():
                        if e.type == QUIT: sys.exit()
                
                    screen.blit(imagen,(0,0))
                    display.flip()
                    break
            elif i == 5:
                init()
                screen = display.set_mode((500,600))
                imagen= image.load(r'/Users/joseruiz/Desktop/proyecto final/La moto.png')
                imagen = transform.scale(imagen,(500,600))

                while True:
                    for e in event.get():
                        if e.type == QUIT: sys.exit()
                
                    screen.blit(imagen,(0,0))
                    display.flip()
                    break
            elif i == 8:
                init()
                screen = display.set_mode((500,600))
                imagen= image.load(r'/Users/joseruiz/Desktop/proyecto final/DESTINO BUENOS AIRES.png')
                imagen = transform.scale(imagen,(500,600))

                while True:
                    for e in event.get():
                        if e.type == QUIT: sys.exit()
                
                    screen.blit(imagen,(0,0))
                    display.flip()
                    break
                
#--------------------------CIERRA BLOQUE DE CODIGO IMAGEN-----------------------------------

            respuesta= str(input("Escribe aquí la respuesta:  "))
            while respuesta != columna2_lect[i] and intentos<3:
                
                print(Fore.RED + "Respuesta incorrecta: ")
                print()
                print('Revisa que tu respuesta este escrita con la primera letra mayuscula')
                intentos+=1
                respuesta= str(input("Respuesta (solo el número): "))

            if respuesta != columna2_lect[i] and intentos==3:
                #Printea como la respuesta y la explicación
                print()

            if respuesta == columna2_lect[i]:
                print( Fore.GREEN + "¡ C O R R E C T A !")
                puntaje+=1
                print(Fore.YELLOW + 'Puntaje: ',puntaje)
                print()
    #----------------------------CIERRA LECTURA-----------------------------------

    elif seccion == 'E' or seccion == 'e':
        print()
        corre = False
        print(Fore.CYAN + "¡ S A L I S T E      D E L      E X A M E N !")
        quit()
    

#----------------------------------- PREMIO ------------------------------------------
    elif seccion == 'P' or seccion =='p':
        if puntaje >= 30:
            import math
            pygame.init()
            white = (255, 255, 255)
            black = (0, 0, 0)
            hue = 0

            WIDTH = 1920
            HEIGHT = 1080

            x_start, y_start = 0, 0

            x_separator = 10
            y_separator = 20

            rows = HEIGHT // y_separator
            columns = WIDTH // x_separator
            screen_size = rows * columns

            x_offset = columns / 2
            y_offset = rows / 2

            A, B = 0, 0  # rotating animation

            theta_spacing = 10
            phi_spacing = 1 # for faster rotation change to 2, 3 or more, but first change 86, 87 lines as commented

            chars = ".,-~:;=!*#$@"  # luminance index

            screen = pygame.display.set_mode((WIDTH, HEIGHT))

            display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
            # display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            pygame.display.set_caption('Donut')
            font = pygame.font.SysFont('Arial', 18, bold=True)

            def hsv2rgb(h, s, v):
                return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


            def text_display(letter, x_start, y_start):
                text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
                display_surface.blit(text, (x_start, y_start))

            # def text_display(letter, x_start, y_start):
            #     text = font.render(str(letter), True, white)
            #     display_surface.blit(text, (x_start, y_start))


            run = True
            while run:

                screen.fill((black))

                z = [0] * screen_size  # Donut. Fills donut space
                b = [' '] * screen_size  # Background. Fills empty space

                for j in range(0, 628, theta_spacing):  # from 0 to 2pi
                    for i in range(0, 628, phi_spacing):  # from 0 to 2pi
                        c = math.sin(i)
                        d = math.cos(j)
                        e = math.sin(A)
                        f = math.sin(j)
                        g = math.cos(A)
                        h = d + 2
                        D = 1 / (c * h * e + f * g + 5)
                        l = math.cos(i)
                        m = math.cos(B)
                        n = math.sin(B)
                        t = c * h * g - f * e
                        x = int(x_offset + 40 * D * (l * h * m - t * n))  # 3D x coordinate after rotation
                        y = int(y_offset + 20 * D * (l * h * n + t * m))  # 3D y coordinate after rotation
                        o = int(x + columns * y)  
                        N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))  # luminance index
                        if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                            z[o] = D
                            b[o] = chars[N if N > 0 else 0]

                if y_start == rows * y_separator - y_separator:
                    y_start = 0

                for i in range(len(b)):
                    A += 0.000004  # for faster rotation change to bigger value
                    B += 0.000002  # for faster rotation change to bigger value
                    if i == 0 or i % columns:
                        text_display(b[i], x_start, y_start)
                        x_start += x_separator
                    else:
                        y_start += y_separator
                        x_start = 0
                        text_display(b[i], x_start, y_start)
                        x_start += x_separator


                pygame.display.update()

                hue += 0.005

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            run = False
        
        else:
            print()
            print(Fore.RED + 'No tienes la cantidad suficiente de puntos :,(')
            print()
            print(Fore.RED + 'Aun tienes oportunidad de conseguir...LA DONA')



    #Por si no ponen una de nuestras tres opciones
    else:
        print()
        print(Fore.RED + "No seleccionaste ninguna de los incisos anteriores...")
    

      