from PyQt5.QtWidgets import QLabel


class Score(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.score = 0
        prozor = QLabel("Score: ")
        prozor.setGeometry(430, 10, 500, 50)
        prozor.setStyleSheet("color: orange")

    def print_results(self):
        self.score += 1
        text = ('''<p>{}</p>'''.format(self.score))
        return text
