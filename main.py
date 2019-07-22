import pygame as pg
import sys, math
import random
import time

Screen = (720, 720)
FPS = 60
space_type = 0
missile_type = 0
stage = 1
missilesize = (30, 30)
spacesize = (50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def image_load(path, size, isAlpha = False, color_key = (255, 255, 255)) :
    image = pg.transform.scale(pg.image.load(path), size)

    if isAlpha :
        image = image.convert()
        image.set_colorkey(color_key)
        image.set_colorkey(WHITE)
    return image

missleW_img = image_load('./m1.png', missilesize)
missleB_img = image_load('./m2.png', missilesize)
spaceW_img = image_load('./s1.png', spacesize)
spaceB_img = image_load('./s2.png', spacesize)

class missileW(pg.sprite.Sprite) :
    def __init__(self, angle, stage) :
        global missile_type
        missile_type = 1
        pg.sprite.Sprite.__init__(self)
        self.image = missleW_img
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        if stage == 1 :
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = 5 * math.cos(math.radians(self.angle))
            self.speedy = 5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery


        elif stage == 2 :
            self.rect.center = (720, 720)
            self.angle = angle
            self.speedx = 4 * math.cos(math.radians(self.angle))
            self.speedy = 4 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 3 :
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = 5 * math.cos(math.radians(self.angle))
            self.speedy = 5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 4 :
            self.rect.center = (360, 360)
            self.angle = angle
            self.speedx = 2.5 * math.cos(math.radians(self.angle))
            self.speedy = 2.5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 5 :
            self.rect.center = (int(random.random()*721), 0)
            self.speedx = 0
            self.speedy = random.randint(3, 10)
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 6 :
            self.rect.center = (int(random.random()*721), 10)
            self.angle = angle
            self.speedx = 5 * math.cos(math.radians(self.angle))
            self.speedy = 5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 7 :
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = random.randint(1, 5) * math.cos(math.radians(self.angle))
            self.speedy = random.randint(1, 5) * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 8 :
            self.rect.center = (720, int(random.random()*721))
            self.angle = angle
            self.speedx = random.randint(1, 5) * math.cos(math.radians(self.angle))
            self.speedy = random.randint(1, 5) * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 9 :
            self.rect.center = (int(random.random() * 721), int(random.random() * 721))
            self.angle = angle
            self.speedx = 0
            self.speedy = 0
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 10:
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = random.randint(5, 10) * math.cos(math.radians(self.angle))
            self.speedy = random.randint(5, 10) * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

    def update(self) :
        self.posx += self.speedx
        self.posy += self.speedy
        self.rect.center = (self.posx, self.posy)

        if self.rect.centery > Screen[1] or self.rect.centery < 0 :
            self.kill()
        if self.rect.centerx > Screen[0] or self.rect.centerx < 0 :
            self.kill()


class missileB(pg.sprite.Sprite) :
    def __init__(self, angle, stage) :
        global missile_type
        missile_type = 0
        pg.sprite.Sprite.__init__(self)
        self.image = missleB_img
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        if stage == 1 :
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = 5 * math.cos(math.radians(self.angle))
            self.speedy = 5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 2:
            self.rect.center = (0, 0)
            self.angle = angle
            self.speedx = 4 * math.cos(math.radians(self.angle))
            self.speedy = 4 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 3 :
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = 5 * math.cos(math.radians(self.angle))
            self.speedy = 5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 4 :
            self.rect.center = (360, 360)
            self.angle = angle
            self.speedx = 2.5 * math.cos(math.radians(self.angle))
            self.speedy = 2.5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 5 :
            self.rect.center = (int(random.random()*721), 0)
            self.speedx = 0
            self.speedy = random.randint(3, 10)
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 6 :
            self.rect.center = (int(random.random()*721), 10)
            self.angle = angle
            self.speedx = 5 * math.cos(math.radians(self.angle))
            self.speedy = 5 * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 7 :
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = random.randint(1, 5) * math.cos(math.radians(self.angle))
            self.speedy = random.randint(1, 5) * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 8 :
            self.rect.center = (0, int(random.random()*721))
            self.angle = angle
            self.speedx = random.randint(1, 5) * math.cos(math.radians(self.angle))
            self.speedy = random.randint(1, 5) * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 9 :
            self.rect.center = (int(random.random() * 721), int(random.random() * 721))
            self.angle = angle
            self.speedx = 0
            self.speedy = 0
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

        elif stage == 10:
            self.rect.center = (360, 90)
            self.angle = angle
            self.speedx = random.randint(5, 10) * math.cos(math.radians(self.angle))
            self.speedy = random.randint(5, 10) * math.sin(math.radians(self.angle))
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

    def update(self) :
        self.posx += self.speedx
        self.posy += self.speedy
        self.rect.center = (self.posx, self.posy)

        if self.rect.centery > Screen[1] or self.rect.centery < 0 :
            self.kill()
        if self.rect.centerx > Screen[0] or self.rect.centerx < 0 :
            self.kill()

class space(pg.sprite.Sprite) :
    def __init__(self) :
        global space_type
        pg.sprite.Sprite.__init__(self)
        self.image = image_load('./s1.png', spacesize)
        space_type = 1
        self.rect = self.image.get_rect()
        self.rect.center = (Screen[0] / 2, Screen[1] * (3 / 4))
        self.x_position = self.rect.x
        self.y_position = self.rect.y
        self.mask = pg.mask.from_surface(self.image)
        self.last_change = 0

    def update(self) :
        global space_type

        key = pg.key.get_pressed()
        key_press = False

        if key[pg.K_SPACE] :
            key_press = True

        now = int(time.time() * 1000.0)

        if key_press and space_type == 0 and (now - self.last_change) >= 700 :
            space_type = 1
            self.image = spaceW_img
            self.rect = self.image.get_rect()
            self.mask = pg.mask.from_surface(self.image)
            self.last_change = now

        elif key_press and space_type == 1 and (now - self.last_change) >= 700 :
            space_type = 0
            self.image = spaceB_img
            self.rect = self.image.get_rect()
            self.mask = pg.mask.from_surface(self.image)
            self.last_change = now

        if key[pg.K_LEFT] :
            self.x_position -= 5
        if key[pg.K_RIGHT] :
            self.x_position += 5
        if key[pg.K_UP] :
            self.y_position -= 5
        if key[pg.K_DOWN] :
            self.y_position += 5
        self.rect.x = self.x_position
        self.rect.y = self.y_position

        if self.rect.centerx < 0 or self.rect.centerx > Screen[0]\
                or self.rect.centery < 0 or self.rect.centery > Screen[1]:
            self.kill()
            pg.quit()
            sys.exit()

pg.init()
pg.font.init()
window = pg.display.set_mode(Screen)
game_font = pg.font.SysFont('Consolas', 24)
count = 0
start1_text_surface = game_font.render('The Nightmare', True, WHITE)
start2_text_surface = game_font.render('Press any key to start', True, WHITE)
score_text_surface = game_font.render('Score : ' + str(count), True, WHITE)
stage_text_surface = game_font.render('Stage : ' + str(stage), True, WHITE)
final1_text_surface = game_font.render('Congratulations !!', True, WHITE)
final2_text_surface = game_font.render('Press any key to exit', True, WHITE)
score_text_rect = score_text_surface.get_rect()
stage_text_rect = stage_text_surface.get_rect()
final1_text_rect = final1_text_surface.get_rect()
final2_text_rect = final2_text_surface.get_rect()
start1_text_rect = start1_text_surface.get_rect()
start2_text_rect = start2_text_surface.get_rect()
score_text_rect.center = (100, 30)
stage_text_rect.center = (620, 30)
final1_text_rect.center = (200, 300)
final2_text_rect.center = (180, 400)
start1_text_rect.center = (200, 300)
start2_text_rect.center = (180, 400)
clock = pg.time.Clock()
pg.time.set_timer(pg.USEREVENT + 1, 1000)
player_group = pg.sprite.Group()
player = space()
player_group.add(player)
enemy_groupB = pg.sprite.Group()
enemy_groupW = pg.sprite.Group()
pg.display.set_caption("The Nightmare")
gamemenu = False

while True :
    window.fill(BLACK)
    if gamemenu == True :
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                pg.quit()
                sys.exit()
                break

            if event.type == pg.USEREVENT + 1 :
                if count < 10 :
                    stage = 1
                    if count % 2 == 0 :
                        for i in range(60) :
                            enemy_groupB.add(missileB(i * 6 + count, stage))
                    else :
                        for i in range(60) :
                            enemy_groupW.add(missileW(i * 6 + count, stage))
                    count += 1

                elif count < 20 :
                    stage = 2
                    for i in range(30) :
                        enemy_groupB.add(missileB(i * 12 + count, stage))
                        enemy_groupW.add(missileW(360-(i * 12 + count), stage))
                    count += 1

                elif count < 30 :
                    stage = 3
                    if count % 2 == 0 :
                        for i in range(24) :
                            enemy_groupB.add(missileB(i * 15 + count, stage))
                            enemy_groupW.add(missileW(i * 15 + 7.5 + count, stage))
                    else :
                        for i in range(24) :
                            enemy_groupW.add(missileW(i * 15 + count, stage))
                            enemy_groupB.add(missileB(i * 15 + 7.5 + count, stage))
                    count += 1

                elif count < 40 :
                    stage = 4
                    if count % 2 == 0 :
                        for i in range(120) :
                            enemy_groupB.add(missileB(i * 3 + count, stage))
                    else :
                        for i in range(120) :
                            enemy_groupW.add(missileW(i * 3 + count, stage))
                    count += 1


                elif count < 50 :
                    stage = 5
                    for x in range(10) :
                        enemy_groupB.add(missileB(270, stage))
                        enemy_groupW.add(missileW(270, stage))
                    count += 1

                elif count < 60 :
                    stage = 6
                    for i in range(10) :
                        enemy_groupB.add(missileB(random.choice([60, 70, 80, 90, 100, 110, 120]), stage))
                        enemy_groupW.add(missileW(random.choice([60, 70, 80, 90, 100, 110, 120]), stage))
                    count += 1

                elif count < 70 :
                    stage = 7
                    if count % 2 == 0 :
                        for i in range(60) :
                            enemy_groupB.add(missileB(i * 6 + count, stage))
                    else :
                        for i in range(60) :
                            enemy_groupW.add(missileW(i * 6 + count, stage))
                    count += 1

                elif count < 80 :
                    stage = 8
                    if count % 2 == 0 :
                        for i in range(60) :
                            enemy_groupB.add(missileB(i * 6 + count, stage))
                    else :
                        for i in range(60) :
                            enemy_groupW.add(missileW(i * 6 + count, stage))
                    count += 1

                elif count < 90 :
                    stage = 9
                    for i in range(5) :
                        enemy_groupB.add(missileB(0, stage))
                        enemy_groupW.add(missileW(0, stage))
                    count += 1

                elif count < 100 :
                    stage = 10
                    for i in range(60) :
                        enemy_groupB.add(missileB(i * 6 + count, stage))
                        enemy_groupW.add(missileW(i * 6 + count, stage))
                    count += 1

                if count == 100 :
                    for i in enemy_groupB :
                        i.kill()
                    for i in enemy_groupW :
                        i.kill()
                    while True :
                        final1_text_surface = game_font.render('Congratulations !!', True, WHITE)
                        final2_text_surface = game_font.render('Press any key to exit', True, WHITE)
                        window.blit(final1_text_surface, final1_text_rect)
                        window.blit(final2_text_surface, final2_text_rect)
                        for event in pg.event.get() :
                            if event.type == pg.KEYDOWN :
                                pg.quit()
                                sys.exit()



        score_text_surface = game_font.render('Score : ' + str(count), True, WHITE)
        stage_text_surface = game_font.render('Stage : ' + str(stage), True, WHITE)
        window.blit(score_text_surface, score_text_rect)
        window.blit(stage_text_surface, stage_text_rect)

        if space_type == 0 : # Black
            pg.sprite.groupcollide(player_group, enemy_groupW, True, True, pg.sprite.collide_mask)
    
        elif space_type == 1 : # White
            pg.sprite.groupcollide(player_group, enemy_groupB, True, True, pg.sprite.collide_mask)
    
        if not player.alive() :
            pg.quit()
            sys.exit()

        enemy_groupW.update()
        enemy_groupB.update()
        player_group.update()
        enemy_groupW.draw(window)
        enemy_groupB.draw(window)
        player_group.draw(window)

    else :
        start1_text_surface = game_font.render('The Nightmare', True, WHITE)
        start2_text_surface = game_font.render('Press any key to start', True, WHITE)
        window.blit(start1_text_surface, start1_text_rect)
        window.blit(start2_text_surface, start2_text_rect)
        for event in pg.event.get() :
             if event.type == pg.KEYDOWN :
                 gamemenu = True

    pg.display.flip()
    clock.tick(FPS)