import pygame as pg, pygame_gui as pgui, sys
tile_size = 64

pg.init()
bg_color = (176, 247, 255)

screen_width, screen_height = 1200, 900

def main_menu(): 
    pg.display.set_caption('Hoppy Hands')
    screen = pg.display.set_mode((screen_width, screen_height))

    manager = pgui.UIManager((screen_width, screen_height), 'theme.json')
    top = (screen_width/10) * 3
    left = screen_height/5 + 60
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    u_layout_rect = pg.Rect(top-25, left+70, width+50, height)
    title = pgui.elements.UILabel( relative_rect=t_layout_rect, 
                                    text = ' Hoppy Hands',
                                    manager=manager )
    text = pgui.elements.UILabel( relative_rect=u_layout_rect, 
                                    text = ' Thumbs up to start!',
                                    manager=manager )
    frog = pg.image.load('assets\\frog.png')
    frog = pg.transform.rotozoom(frog, 0, 0.3)

    # b1_layout_rect = pg.Rect(top, left+height+20, width, height)
    # button1 = pgui.elements.UIButton(relative_rect=b1_layout_rect, text='Play Game', manager=manager)
    # b2_layout_rect = pg.Rect(top, left+height*2+20, width, height)
    # button2 = pgui.elements.UIButton(relative_rect=b2_layout_rect, text='Help', manager=manager)
    # b3_layout_rect = pg.Rect(top, left+height*3+20, width, height)
    # button3 = pgui.elements.UIButton(relative_rect=b3_layout_rect, text='Exit', manager=manager)

    running = True
    while running:
        screen.fill(bg_color)
        screen.blit(frog, (top + top/2, left-tile_size))
        manager.update(60/1000.0)
        manager.draw_ui(screen)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_k:
                    # level(screen);
                    pg.quit()
                    sys.exit()
            
            # if event.type == pgui.UI_BUTTON_PRESSED:
            #     if event.ui_element == button1:
            #         level_select(screen)
            #     if event.ui_element == button2:
            #         help(screen)
            #     if event.ui_element == button3:
            #         pg.quit()
            #         sys.exit()

            manager.process_events(event)
    

if __name__ == '__main__':
    main_menu()