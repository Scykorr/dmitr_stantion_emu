from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from graphic_arrow import Ui_MainWindow


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.speedSlider.valueChanged.connect(self.valuechange)

        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.pixmap = QPixmap("Arrow.png")
        self.arrow = scene.addPixmap(self.pixmap)

        graphicsView = QGraphicsView(scene, self.ui.centralwidget)
        graphicsView.setStyleSheet("background-image:url(Central1.png);\n"
                                   "background-repeat:no-repeat;\n"
                                   "background-position: center;\n"
                                   "\n"
                                   "border:none;")
        self.ui.gridLayout.addWidget(graphicsView)

    def valuechange(self):
        angel = self.ui.speedSlider.value()
        xform = QTransform()
        xform.rotate(angel)
        xformed_pixmap = self.pixmap.transformed(xform, Qt.SmoothTransformation)
        self.arrow.setPixmap(xformed_pixmap)

        # print(self.arrow.sceneBoundingRect())
