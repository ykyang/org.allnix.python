import PySide2.QtWidgets as Qw
import PySide2.QtQuick as Qq
import PySide2.QtCore as Qc

app = Qw.QApplication([])
view = Qq.QQuickView()
url = Qc.QUrl('view.qml')

# Expand green rectangle with the View
view.setResizeMode(Qq.QQuickView.SizeRootObjectToView) 

view.setSource(url)
view.show()
app.exec_()


