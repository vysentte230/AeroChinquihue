import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
    QSlider,
    QRadioButton,
)


class VentanaFormulario(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario")
        grid = QGridLayout()

        grid.addWidget(QLabel("Nombre:"), 0, 0)
        grid.addWidget(QLineEdit(), 0, 1)

        grid.addWidget(QLabel("Apellido:"), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        grid.addWidget(QLabel("Correo:"), 2, 0)
        grid.addWidget(QLineEdit(), 2, 1)

        grid.addWidget(QCheckBox("joder o eso osito fredy fas bear"),3, 0)
        grid.addWidget(QLineEdit(), 2, 1)

        grid.addWidget(QRadioButton(),4, 0)
        

        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaFormulario()
    ventana.show()
    sys.exit(app.exec())