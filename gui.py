from PyQt6 import QtWidgets

contador = 67
def llamada():
    print(f"presionaste el boton {contador} veces")

app = QtWidgets.QApplication([])

#Logina inicio
#un widget es la base de todo
widget = QtWidgets.QWidget()
caja = QtWidgets.QHBoxLayout(widget)
#caja horizontal
#caja = QtWidgets.QWidget()
grid = QtWidgets.QGridLayout ( )



widget.setFixedSize(400, 300)


# mostrar widget
widget.show()

#logica fin

app.exec()