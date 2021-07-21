'''
面向对象程序设计的一个实例
'''
import pygame,random
from pygame.locals import *
class HeroPlane():
    def __init__(self,screen):
        self.x_hero=150
        self.y_hero=360
        self.screen=screen
        self.image = pygame.image.load(".//Resources//hero.png")

    bulletList=[]
    def moveLeft(self):
        self.x_hero-=2
        pass
    def moveRight(self):
        self.x_hero += 2
        pass
    def display(self):
        self.screen.blit(self.image,(self.x_hero,self.y_hero))
        for item in self.bulletList:
            if item.judge()== 1:
                self.bulletList.remove(item)
        for item in self.bulletList:
            item.display()
            item.move()
        pass
    def callBullet(self):
        newBullet=Bullet(self.screen,self.x_hero,self.y_hero,0)
        self.bulletList.append(newBullet)
    def attack(self):
        for bul in Enemy.BulletList:
            if bul.By==1:
                if self.x_hero<bul.x_bullet and bul.x_bullet<self.x_hero+72:
                    if self.y_hero<bul.y_bullet and bul.y_bullet<self.y_hero+72:
                        print("User is attacked")
                        Enemy.BulletList.remove(bul)
                        pygame.mixer.Sound(".//Resources//explosion.mp3").play()
class Bullet():
    def __init__(self,screen,x_bullet,y_bullet,By):
        if By==0:
            self.x_bullet=x_bullet+36
        elif By==1:
            self.x_bullet=x_bullet+20
        self.y_bullet=y_bullet
        self.screen=screen
        self.By=By
        if self.By==0:
            self.image=pygame.image.load(".//Resources//bullet-3.png")
        elif self.By==1:
            self.image = pygame.image.load(".//Resources//bullet-1.png")
    def display(self):
        self.screen.blit(self.image,(self.x_bullet,self.y_bullet))
        pass
    def move(self):

        if self.By==0:
            self.y_bullet-=3
        elif self.By==1:
            self.y_bullet+=2
        pass
    def judge(self):
        if self.y_bullet<0 or self.y_bullet>500:
            return 1
        else:
            return 0
class Enemy:
    def __init__(self,screen):
        self.y_enemy=0
        self.x_enemy=random.randint(0,350)
        print('生成敌军于%.2f'%self.x_enemy)
        self.image=pygame.image.load(".//Resources//enemy-1.png")
        self.screen=screen
        self.now=1
    BulletList=[]#类变量存储BulletList
    def move(self):
        if self.x_enemy<0:
            self.now=1
        elif self.x_enemy>350:
            self.now=-1
        self.x_enemy+=self.now
        #print('%.2f'%self.x_enemy)
    def callBullet(self):
        newBullet=Bullet(self.screen,self.x_enemy,self.y_enemy,1)
        self.BulletList.append(newBullet)
    def display(self):
        self.screen.blit(self.image,(self.x_enemy,self.y_enemy))
        for item in self.BulletList:
            if item.judge()==1:
                self.BulletList.remove(item)
        for item in self.BulletList:
            item.display()
            item.move()
        self.move()
        self.attack()
        if random.randint(0,1000)>990:
            self.callBullet()
    def attack(self):
        for bul in HeroPlane.bulletList:
            if bul.By==0:
                if self.x_enemy<bul.x_bullet and bul.x_bullet<self.x_enemy+72:
                    if self.y_enemy<bul.y_bullet and bul.y_bullet<self.y_enemy+72:
                        print("Enemy is attacked")
                        pygame.mixer.Sound(".//Resources//explosion.mp3").play()
                        HeroPlane.bulletList.remove(bul)
def key_control1(heroobj):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("退出")
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("退出")
                exit()
                pass
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                heroobj.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                heroobj.moveRight()
            elif event.key == K_SPACE:
                print("攻击")
                heroobj.callBullet()
    pass


def key_control(heroobj):
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == QUIT:
            print("退出")
            exit()
            pass
    B=pygame.key.get_pressed()
    if B[pygame.K_ESCAPE]:
        print("退出")
        exit()
        pass
    if B[pygame.K_a] or B[pygame.K_LEFT]:
        print("left")
        heroobj.moveLeft()
    if B[pygame.K_d] or B[pygame.K_RIGHT]:
        print("right")
        heroobj.moveRight()
    if B[pygame.K_SPACE]:
        print("攻击")
        heroobj.callBullet()
        pygame.mixer.Sound(".//Resources//shoot.mp3").play()
def main():
    screen=pygame.display.set_mode((350,500))#设置窗口
    background=pygame.image.load(".//Resources//bg_01.png")#加载背景
    pygame.display.set_caption("main")
    pygame.mixer.init()
    pygame.mixer.music.load(".//Resources//main.mp3")
    pygame.mixer.music.set_volume(0.22)
    pygame.mixer.music.play(-1)
    hero=HeroPlane(screen)
    enemy=Enemy(screen)
    while True:
        screen.blit(background, (0, 0))  # 设置背景
        hero.display()
        key_control(hero)
        hero.attack()
        enemy.display()
        pygame.display.update()  # 刷新界面
if __name__=="__main__":
    main()
