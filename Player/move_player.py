from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import time


class MovePlayer(QObject):
    key_pressed_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.is_done = False
        self.keys_pressed = []
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__work__)

    def start(self) -> None:
        self.is_done = False
        self.thread.start()

    def add_key_pressed(self, key) -> None:
        self.keys_pressed.append(key)

    def remove_key_pressed(self, key) -> None:
        try:
            self.keys_pressed.remove(key)
        except ValueError:
            self.keys_pressed.clear()

    def die(self) -> None:
        self.is_done = True
        self.keys_pressed.clear()
        self.thread.quit()

    @pyqtSlot()
    def __work__(self) -> None:
        while not self.is_done:
            for key in self.keys_pressed:
                self.key_pressed_signal.emit(key)
            time.sleep(0.05)
