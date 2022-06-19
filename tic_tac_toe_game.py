import pygame
import sys
if __name__ == "__main__":
    scwidth = 545
    scheight = 545
    FPS = 40
    box_x=135
    box_y=118
    clock = pygame.time.Clock()
    caption = pygame.display.set_caption("TIC TAC TOE")
    window = pygame.display.set_mode((scwidth,scheight))
    mainbox = pygame.image.load("tic_tac_toe_boxeesch.jpg").convert_alpha()
    mainbox = pygame.transform.scale(mainbox,(scwidth,scheight))
    smallbox = pygame.image.load("box3.png").convert_alpha()
    smallbox = pygame.transform.scale(smallbox,(int(scwidth/6),int(scheight/6)))
    smallbox1 = pygame.image.load("redbox.jpeg").convert_alpha()
    smallbox1 = pygame.transform.scale(smallbox1,(int(scwidth/6),int(scheight/6)))
    smallbox_rect = smallbox.get_rect(center = (180,163))
    greenbox = pygame.image.load("greenbox.jpeg").convert_alpha()
    greenbox = pygame.transform.scale(greenbox,(int(scwidth/6),int(scheight/6)))
    o_1 = pygame.image.load("ovariablech.jpg").convert_alpha()
    o_1 = pygame.transform.scale(o_1,(68,68))
    x_1 = pygame.image.load("xvariablech2.jpg").convert_alpha()
    list_o = []
    list_x = []
    i = 0
    turn = 0
    sturn = 0
    gameo = [[[180,163],[273,163],[366,163]],[[180,258],[273,258],[366,258]],[[180,353],[273,353],[366,353]],[[180,163],[180,258],[180,353]],[[273,163],[273,258],[273,353]],[[366,163],[366,258],[366,353]],[[180,163],[273,258],[366,353]],[[180,353],[273,258],[366,163]]]
    def createo(o_list,x_list,x,y):
        for h in x_list:
            if h.centerx == x and h.centery == y:
                return o_list
        for o in o_list:
            if o.centerx == x and o.centery == y:
                return o_list
        o_1 = pygame.image.load("ovariablech.jpg").convert_alpha()
        o_1 = pygame.transform.scale(o_1,(68,68))
        o_1_rect1 = o_1.get_rect(center = (x,y))
        o_list.append(o_1_rect1)
        return o_list
    def createx(x_list,o_list,x,y):
        for o in o_list:
            if o.centerx == x and o.centery == y:
                return x_list
        for h in x_list:
            if h.centerx == x and h.centery == y:
                return x_list
        x_1 = pygame.image.load("xvariablech2.jpg").convert_alpha()
        x_1_rect1 = x_1.get_rect(center = (x,y))
        x_list.append(x_1_rect1)
        return x_list
    def gameover(list_x,list_o):
        listgame = []
        lastboxes = []
        gamefasak = False
        for e in list_x:
            for h in list_x:
                for d in list_x:
                    listgame = [[e.centerx,e.centery],[h.centerx,h.centery],[d.centerx,d.centery]]
                    if listgame in gameo:
                        gamefasak = True
                        lastboxes = listgame
        listgame = []
        for a in list_o:
            for b in list_o:
                for c in list_o:
                    listgame = [[a.centerx,a.centery],[b.centerx,b.centery],[c.centerx,c.centery]]
                    if listgame in gameo:
                        gamefasak = True
                        lastboxes = listgame
        if gamefasak:
            while(True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                window.blit(mainbox,(0,0))
                for point in lastboxes:
                    rect = greenbox.get_rect(center = (point[0],point[1]))
                    window.blit(greenbox,rect)
                for o in list_o:
                    window.blit(o_1,o)
                for x in list_x:
                    window.blit(x_1,x)   
                pygame.display.update()
                clock.tick(FPS)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if smallbox_rect.centerx<366 and smallbox_rect.centerx>=180:
                        smallbox_rect.centerx+=93
                if event.key == pygame.K_LEFT:
                    if smallbox_rect.centerx<=366 and smallbox_rect.centerx>180:
                        smallbox_rect.centerx-=93
                if event.key == pygame.K_DOWN:
                    if smallbox_rect.centery<353 and smallbox_rect.centery>=163:
                        smallbox_rect.centery+=95
                if event.key == pygame.K_UP:
                    if smallbox_rect.centery<=353 and smallbox_rect.centery>163:
                        smallbox_rect.centery-=95
                if event.key == pygame.K_SPACE:
                    if sturn == 0:
                        list_o = createo(list_o,list_x,smallbox_rect.centerx,smallbox_rect.centery)   
                        turn = 1
                    if sturn == 1:
                        list_x = createx(list_x,list_o,smallbox_rect.centerx,smallbox_rect.centery)
                        turn = 0
                    

                gameover(list_x,list_o)
                sturn = turn
        window.blit(mainbox,(0,0))
        if sturn==1:
            window.blit(smallbox,smallbox_rect)
        if sturn==0:
            window.blit(smallbox1,smallbox_rect)
        for o in list_o:
            window.blit(o_1,o)
        for x in list_x:
            window.blit(x_1,x)   
        pygame.display.update()
        clock.tick(FPS)

        
