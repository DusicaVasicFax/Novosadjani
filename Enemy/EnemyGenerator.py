from Novosadjani.Enemy.Enemy import Enemy

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
FRAME_TIME_MS = 16


class EnemyGenerator:
    def __init__(self):
        for i in range(10):
            self.enemy = Enemy()
            self.enemy.setPos((SCREEN_WIDTH-self.enemy.pixmap().width())/5+i*90,
                              (SCREEN_HEIGHT-self.enemy.pixmap().height())/2)
            self.enemy.alien1()
            self.addItem(self.enemy)

        for j in range(2):
            for i in range(10):
                self.enemy = Enemy()
                self.enemy.setPos((SCREEN_WIDTH - self.enemy.pixmap().width()) / 5 + i * 90,
                                 (SCREEN_HEIGHT+200 - self.enemy.pixmap().height()) / 2+j*80)
                self.enemy.alien2()
                self.addItem(self.enemy)

        for j in range(2):
            for i in range(10):
                self.enemy = Enemy()
                self.enemy.setPos((SCREEN_WIDTH - self.enemy.pixmap().width()) / 5 + i * 90,
                                 (SCREEN_HEIGHT+500 - self.enemy.pixmap().height()) / 2+j*80)
                self.enemy.alien3()
                self.addItem(self.enemy)