import math
import pygame
import random
from Button import Button
def obliczOdleglosc(A,B):
    return math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)

pygame.init()
okno = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Fraktale")
timer = pygame.time.Clock()
FPS = 60
fontDUZA = pygame.font.SysFont('Comic Sans MS', 34)
fontDUZA.set_underline(True)
fontMALA = pygame.font.SysFont('Comic Sans MS', 22)
fontMALUTKA = pygame.font.SysFont('Comic Sans MS', 14)

krzywaKochaB = Button('aquamarine3','aquamarine','black',"KRZYWA KOCHA",45)
platekKochaB = Button('aquamarine3','aquamarine','black',"PŁATEK KOCHA",45)
dywanKwadratB = Button('aquamarine3','aquamarine','black',"DYWAN SIERPIŃSKIEGO",5)
dywanTrojkatB = Button('aquamarine3', 'aquamarine', 'black', "DYWAN TRÓJKĄT", 50)
smokB = Button('aquamarine3','aquamarine','black',"SMOK HEIGHWAYA ",45)
koniecB = Button('aquamarine3','aquamarine','black',"ZAMKNIJ",85)
menuB = Button('aquamarine3','aquamarine','black',"POWRÓT",45)
stopienUPB = Button('aquamarine3','aquamarine','black',"Stopień + 1")
stopienDOWNB = Button('aquamarine3','aquamarine','black',"Stopień - 1")
punktyDOWNB = Button('aquamarine3','aquamarine','black',"Punkty - 1000")
punktyUPB = Button('aquamarine3','aquamarine','black',"Punkty + 1000")
TRYB = 0
run = True
stopien = 0
P1 = [50, 50]
P2 = [630, 630]
K1 = [100,495]
K2 = [600,495]
K3 = [350,62]

oknoKopia = pygame.Surface((700, 550))
n = 3000
def krzywaKocha(okno, P1,P2,stopien):
    dx = P2[0] - P1[0]
    dy = P2[1] - P1[1]
    if stopien == 0:
        pygame.draw.line(okno,'black',P1,P2,1)
    else:
        krzywaKocha(okno,P1,(P1[0]+dx//3,P1[1]+dy//3),stopien-1)
        krzywaKocha(okno,(P1[0]+dx*2/3,P1[1]+dy*2/3),P2,stopien-1)
        krzywaKocha(okno,(P1[0]+dx//3,P1[1]+dy//3),((P1[0]+P2[0])/2+math.sqrt(3)/6*dy,(P1[1]+P2[1])/2-math.sqrt(3)/6*dx),stopien-1)
        krzywaKocha(okno,((P1[0]+P2[0])/2+math.sqrt(3)/6*dy,(P1[1]+P2[1])/2-math.sqrt(3)/6*dx),(P1[0]+dx*2/3,P1[1]+dy*2/3),stopien-1)

def dywanSierpinskiegoKwadrat(okno,x1,y1,dl,stopien):
    jednaTrzecia = dl//3
    dwieTrzecie = 2*jednaTrzecia
    if stopien == 0:
        pygame.draw.rect(okno,'black',((x1,y1),(dl,dl)))
    elif stopien == 1:
        pygame.draw.rect(okno, 'black', ((x1,y1),(dl,dl)))
        pygame.draw.rect(okno, 'white', ((x1+jednaTrzecia,y1+jednaTrzecia), (jednaTrzecia,jednaTrzecia)))
    else:
        pygame.draw.rect(okno, 'black', ((x1, y1), (dl, dl)))
        pygame.draw.rect(okno, 'white', ((x1 + jednaTrzecia, y1 + jednaTrzecia), (jednaTrzecia, jednaTrzecia)))
        dywanSierpinskiegoKwadrat(okno,x1,y1,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1+jednaTrzecia,y1,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1+dwieTrzecie,y1,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1,y1+jednaTrzecia,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1+dwieTrzecie,y1+jednaTrzecia,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1,y1+dwieTrzecie,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1+jednaTrzecia,y1+dwieTrzecie,jednaTrzecia,stopien-1)
        dywanSierpinskiegoKwadrat(okno,x1+dwieTrzecie,y1+dwieTrzecie,jednaTrzecia,stopien-1)

def dywanSierpinskiegoTrojkat(okno,P1,P2,P3,stopien):
    a = P2[0] - P1[0]

    if stopien==0:
        pygame.draw.polygon(okno,"black",(P1,P2,P3))
    if stopien==1:
        pygame.draw.polygon(okno, "black", (P1, P2, P3))
        pygame.draw.polygon(okno, "white", ((P1[0]+a//4,P1[1]-(((a//2)*math.sqrt(3))//2)), (P3[0],P1[1]), (P2[0]-a//4,P2[1]-(((a//2)*math.sqrt(3))//2))))
    if stopien > 1:
        dywanSierpinskiegoTrojkat(okno,P1,(P1[0]+a//2,P1[1]),(P1[0]+a//4,P1[1]-(((a//2)*math.sqrt(3))//2)),stopien-1)
        dywanSierpinskiegoTrojkat(okno,(P1[0]+a//4,P1[1]-(((a//2)*math.sqrt(3))//2)),(P2[0]-a//4,P2[1]-(((a//2)*math.sqrt(3))//2)),P3,stopien-1)
        dywanSierpinskiegoTrojkat(okno,(P1[0]+a//2,P1[1]),P2,(P2[0]-a//4,P2[1]-(((a//2)*math.sqrt(3))//2)),stopien-1)

def smok(n):
    oknoKopia = pygame.Surface((700, 550))
    oknoKopia.fill('white')
    X = [1]
    Y = [1]

    for i in range(1, n):
        if random.randint(1, 2) == 1:
            X.append(-0.4 * X[i - 1] - 1)
            Y.append(-0.4 * Y[i - 1] + 0.1)
        else:
            X.append(0.76 * X[i - 1] - 0.4 * Y[i - 1])
            Y.append(0.4 * X[i - 1] + 0.76 * Y[i - 1])

    for i in range(1, n):
        X[i] = (X[i] * -400) + 200
        Y[i] = (Y[i] * -300) + 200

    for i in range(10, n):
        pygame.draw.circle(oknoKopia, 'blue', (X[i], Y[i]), 2)

    return oknoKopia


while run:
    timer.tick(FPS)
    okno.fill('azure3')
    klawisze = pygame.key.get_pressed()
    myszPozycja = pygame.mouse.get_pos()
    myszKlik = pygame.mouse.get_pressed()


    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            run = False

    if klawisze[pygame.K_ESCAPE]: run = False
    if TRYB == 0:
        stopien = 0
        okno.blit(fontDUZA.render("Wizualizacja prostych fraktali", True, 'black'),(100,20))
        okno.blit(fontMALUTKA.render("Informatyka rozszerzona                  Zespół Szkół Energetycznych w Rzeszowie                Paweł Łapiński", True, 'black'),(10,680))

        krzywaKochaB.render(okno,180,100,310,50)
        platekKochaB.render(okno,180,170,310,50)
        dywanKwadratB.render(okno,180,240,310,50)
        dywanTrojkatB.render(okno, 180, 310, 310, 50)
        smokB.render(okno,180,380,310,50)
        koniecB.render(okno,180,510,310,50)


        if krzywaKochaB.clik():
            TRYB = 1
            stopien = 0
            P1 = [50, 50]
            P2 = [630, 630]
            K1 = [100, 495]
            K2 = [600, 495]
            K3 = [350, 62]

        if platekKochaB.clik():
            TRYB = 2
            stopien = 0
            P1 = [50, 50]
            P2 = [630, 630]
            K1 = [100, 495]
            K2 = [600, 495]
            K3 = [350, 62]
        if dywanKwadratB.clik():
            TRYB = 3
            stopien = 0
            x1 = 70
            y1 = 50
            dl = 550

        if dywanTrojkatB.clik():
            TRYB = 4
            stopien = 0
            P1 = [50, 570]
            P2 = [650, 570]
            P3 = [350, 50]


        if smokB.clik():
            n = 3000
            oknoKopia = smok(n)
            TRYB = 5

        if koniecB.clik():
            run = False

    if TRYB in (1,2,3,4,5):
        okno.fill('white')
        menuB.render(okno,490,640,200,50)
        if menuB.clik():
            TRYB = 0

    if TRYB in (1, 2):
        pass




    if TRYB == 1:
        okno.blit(fontMALA.render("KRZYWA KOCHA", True, 'black'), (250, 10))

        krzywaKocha(okno,P1,P2,stopien)
        if stopienUPB.clik():
            stopien+=1
        if stopienDOWNB.clik() and stopien > 0:
            stopien-=1
        stopienUPB.render(okno, 10, 580, 150, 50)
        stopienDOWNB.render(okno, 10, 640, 150, 50)
        okno.blit(fontMALA.render("STOPIEŃ: " + str(stopien), True, 'black'), (180, 600))
        okno.blit(fontMALA.render("Liczba odcinków: " + str((4 ** stopien)), True, 'black'), (180, 630))
        if stopien == 0:
            dl = round(obliczOdleglosc(P1, P2), 0)
        else:
            dl = round(obliczOdleglosc(P1, P2), 0)
            dl = round(dl * (4 / 3) ** stopien, 0)
        dl = int(dl)
        okno.blit(fontMALA.render("Długość krzywej: " + str(dl), True, 'black'), (180, 660))

    if TRYB == 2:
        okno.blit(fontMALA.render("PŁATEK KOCHA", True, 'black'), (250, 10))

        krzywaKocha(okno, K2, K1, stopien)
        krzywaKocha(okno, K1, K3, stopien)
        krzywaKocha(okno, K3, K2, stopien)
        if stopienUPB.clik():
            stopien += 1
        if stopienDOWNB.clik() and stopien > 0:
            stopien -= 1
        stopienUPB.render(okno, 10, 580, 150, 50)
        stopienDOWNB.render(okno, 10, 640, 150, 50)
        okno.blit(fontMALA.render("STOPIEŃ: " + str(stopien), True, 'black'), (15, 540))
        okno.blit(fontMALA.render("Liczba odcinków: " + str((4 ** stopien)*3), True, 'black'), (180, 630))
        if stopien == 0:
            dl = round(obliczOdleglosc(K1, K2), 0)
        else:
            dl = round(obliczOdleglosc(K1, K2), 0)
            dl = round(dl * (4 / 3) ** stopien, 0)
        dl = int(dl*3)
        okno.blit(fontMALA.render("Obwód figury: " + str(dl), True, 'black'), (180, 660))

    if TRYB == 3:
        okno.blit(fontMALA.render("KWADRATOWY DYWAN SIERPIŃSKIEGO", True, 'black'), (100, 10))
        dywanSierpinskiegoKwadrat(okno,x1,y1,dl,stopien)
        if stopienUPB.clik():
            stopien += 1
        if stopienDOWNB.clik() and stopien > 0:
            stopien -= 1
        stopienUPB.render(okno, 10, 640, 150, 50)
        stopienDOWNB.render(okno, 165, 640, 150, 50)
        okno.blit(fontMALA.render("STOPIEŃ: " + str(stopien), True, 'black'), (330, 650))

    if TRYB == 4:
        okno.blit(fontMALA.render("TROJKĄTNY DYWAN SIERPIŃSKIEGO", True, 'black'), (150, 10))
        dywanSierpinskiegoTrojkat(okno,P1,P2,P3,stopien)
        if stopienUPB.clik():
           stopien += 1
        if stopienDOWNB.clik() and stopien > 0:
           stopien -= 1
        stopienUPB.render(okno, 10, 640, 150, 50)
        stopienDOWNB.render(okno, 165, 640, 150, 50)
        okno.blit(fontMALA.render("STOPIEŃ: " + str(stopien), True, 'black'), (330, 650))

    if TRYB == 5:
        okno.blit(fontMALA.render("Smok Heighwaya".upper(), True, 'black'), (250, 10))
        punktyUPB.render(okno, 10, 640, 180, 50)
        punktyDOWNB.render(okno, 200, 640, 180, 50)
        if punktyDOWNB.clik() and n != 1000:
            n-=1000
            oknoKopia = smok(n)
        if punktyUPB.clik():
            n+=1000
            oknoKopia = smok(n)
        okno.blit(fontMALA.render("Ilość punktów: " + str(n), True, 'black'), (10, 600))


        okno.blit(oknoKopia,(0,43))

    pygame.display.update()

pygame.quit()