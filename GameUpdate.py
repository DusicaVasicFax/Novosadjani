from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
import time


class GameUpdateThread(QObject):
    game_update_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_done = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)
        self.game_pause = False

    def start(self) -> None:
        self.is_done = False
        self.thread.start()

    def die(self) -> None:
        self.is_done = True
        self.thread.quit()

    @pyqtSlot()
    def __work__(self) -> None:
        while not self.is_done:
            if not self.game_pause:
                self.game_update_signal.emit()
            time.sleep(0.05)


class BulletUpdateThread(QObject):
    bullet_update_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_done = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self) -> None:
        self.is_done = False
        self.thread.start()

    def die(self) -> None:
        self.is_done = True
        self.thread.quit()

    @pyqtSlot()
    def __work__(self) -> None:
        while not self.is_done:
            self.bullet_update_signal.emit()
            time.sleep(0.015)


class EnemyBulletUpdateThread(QObject):
    enemy_bullet_update_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.is_done = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)
        self.speed = 0.019

    def start(self) -> None:
        self.is_done = False
        self.thread.start()

    def die(self) -> None:
        self.is_done = True
        self.thread.quit()

    def increment_speed(self) -> None:
        if self.speed - 0.0001 > 0:
            self.speed -= 0.0001

    def reset_speed(self) -> None:
        self.speed = 0.019

    @pyqtSlot()
    def __work__(self) -> None:
        while not self.is_done:
            self.enemy_bullet_update_signal.emit()
            time.sleep(self.speed)
