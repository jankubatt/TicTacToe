import pygame
 
pygame.init()
pygame.display.set_caption('TicTacToe') 
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
done = False
tictac = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
circle = True

font = pygame.font.Font('freesansbold.ttf', 32)


areaTM = pygame.Rect(width/3, 0, width/3, height/3)
areaTL = pygame.Rect(0, 0, width/3, height/3)
areaTR = pygame.Rect(width/3*2, 0, width/3, height/3)

areaMM = pygame.Rect(width/3, height/3, width/3, height/3)
areaML = pygame.Rect(0, height/3, width/3, height/3)
areaMR = pygame.Rect(width/3*2, height/3, width/3, height/3)

areaBM = pygame.Rect(width/3, height/3*2, width/3, height/3)
areaBL = pygame.Rect(0, height/3*2, width/3, height/3)
areaBR = pygame.Rect(width/3*2, height/3*2, width/3, height/3)

def drawGrid():
        pygame.draw.line(screen, (255, 255, 255), (width/3, 0), (width/3,height), 1)
        pygame.draw.line(screen, (255, 255, 255), (width/3*2, 0), (width/3*2,height), 1)
        pygame.draw.line(screen, (255, 255, 255), (0, height/3), (width,height/3), 1)
        pygame.draw.line(screen, (255, 255, 255), (0, height/3*2), (width,height/3*2), 1)

def drawAreas():
        pygame.draw.rect(screen, (100, 200, 70), areaTM)
        pygame.draw.rect(screen, (100, 200, 70), areaTR)
        pygame.draw.rect(screen, (100, 200, 70), areaTL)
        pygame.draw.rect(screen, (100, 200, 70), areaMM)
        pygame.draw.rect(screen, (100, 200, 70), areaMR)
        pygame.draw.rect(screen, (100, 200, 70), areaML)
        pygame.draw.rect(screen, (100, 200, 70), areaBM)
        pygame.draw.rect(screen, (100, 200, 70), areaBR)
        pygame.draw.rect(screen, (100, 200, 70), areaBL)

def checkWinner():
        for j in range(0, 3):
                tmp = ""
                for i in range(len(tictac)):
                        tmp += tictac[i][j]
                if (tmp == "OOO"):
                        return "O"
                if (tmp == "XXX"):
                        return "X"
        
        for i in range(len(tictac)):
                tmp = ""
                for j in range(len(tictac[i])):
                        tmp += tictac[i][j]
                if (tmp == "OOO"):
                        return "O"
                if (tmp == "XXX"):
                        return "X"

        if (tictac[0][0] + tictac[1][1] + tictac[2][2] == "XXX" or tictac[0][2] + tictac[1][1] + tictac[2][0] == "XXX") :
                return "X"
        if (tictac[0][0] + tictac[1][1] + tictac[2][2] == "OOO" or tictac[0][2] + tictac[1][1] + tictac[2][0] == "OOO") :
                return "O"
        if not any('-' in sublist for sublist in tictac):
                return "T"

        return ""

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                if areaTL.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[0][0] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[0][0] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*0.5), int(height/3*0.5)), 75, 1)
                                                else:
                                                        tictac[0][0] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*0.15, height/3*0.15), (width/3*0.85,height/3*0.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*0.85, height/3*0.15), (width/3*0.15,height/3*0.85), 1)            
                                
                                if areaTM.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[0][1] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[0][1] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*1.5), int(height/3*0.5)), 75, 1)
                                                else:
                                                        tictac[0][1] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*1.15, height/3*0.15), (width/3*1.85,height/3*0.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*1.85, height/3*0.15), (width/3*1.15,height/3*0.85), 1)

                                if areaTR.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[0][2] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[0][2] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*2.5), int(height/3*0.5)), 75, 1)
                                                else:
                                                        tictac[0][2] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*2.15, height/3*0.15), (width/3*2.85,height/3*0.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*2.85, height/3*0.15), (width/3*2.15,height/3*0.85), 1)

                                if areaML.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[1][0] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[1][0] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*0.5), int(height/3*1.5)), 75, 1)
                                                else:
                                                        tictac[1][0] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*0.15, height/3*1.15), (width/3*0.85,height/3*1.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*0.85, height/3*1.15), (width/3*0.15,height/3*1.85), 1)

                                if areaMM.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[1][1] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[1][1] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*1.5), int(height/3*1.5)), 75, 1)
                                                else:
                                                        tictac[1][1] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*1.15, height/3*1.15), (width/3*1.85,height/3*1.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*1.85, height/3*1.15), (width/3*1.15,height/3*1.85), 1)

                                if areaMR.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[1][2] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[1][2] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*2.5), int(height/3*1.5)), 75, 1)
                                                else:
                                                        tictac[1][2] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*2.15, height/3*1.15), (width/3*2.85,height/3*1.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*2.85, height/3*1.15), (width/3*2.15,height/3*1.85), 1)

                                if areaBL.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[2][0] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[2][0] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*0.5), int(height/3*2.5)), 75, 1)
                                                else:
                                                        tictac[2][0] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*0.15, height/3*2.15), (width/3*0.85,height/3*2.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*0.85, height/3*2.15), (width/3*0.15,height/3*2.85), 1)

                                if areaBM.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[2][1] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[2][1] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*1.5), int(height/3*2.5)), 75, 1)
                                                else:
                                                        tictac[2][1] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*1.15, height/3*2.15), (width/3*1.85,height/3*2.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*1.85, height/3*2.15), (width/3*1.15,height/3*2.85), 1)

                                if areaBR.collidepoint(pygame.mouse.get_pos()):
                                        while tictac[2][2] == "-":
                                                circle = not circle
                                                if circle:
                                                        tictac[2][2] = "O"
                                                        print(tictac)             
                                                        pygame.draw.circle(screen, (255,255,255), (int(width/3*2.5), int(height/3*2.5)), 75, 1)
                                                else:
                                                        tictac[2][2] = "X"
                                                        print(tictac)
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*2.15, height/3*2.15), (width/3*2.85,height/3*2.85), 1) 
                                                        pygame.draw.line(screen, (255, 255, 255), (width/3*2.85, height/3*2.15), (width/3*2.15,height/3*2.85), 1)
        #drawAreas()
        drawGrid()
        
        pygame.display.flip()
        
        if checkWinner() == "X":
                text = font.render('Player X Won', True, (255,255,255), (0,0,0)) 
                textRect = text.get_rect()
                screen.blit(text, textRect) 
                pygame.display.flip()
                pygame.time.delay(2000)
                tictac = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
                screen.fill((0,0,0))
        
        if checkWinner() == "O":
                text = font.render('Player O Won', True, (255,255,255), (0,0,0)) 
                textRect = text.get_rect()
                screen.blit(text, textRect) 
                pygame.display.flip()
                pygame.time.delay(2000)
                tictac = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
                screen.fill((0,0,0))
        
        if checkWinner() == "T":
                text = font.render('Tie it is', True, (255,255,255), (0,0,0)) 
                textRect = text.get_rect()
                screen.blit(text, textRect) 
                pygame.display.flip()
                pygame.time.delay(2000)
                tictac = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
                screen.fill((0,0,0))
