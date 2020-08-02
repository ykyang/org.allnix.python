# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgets.html

# https://www.blog.pythonlibrary.org/2018/04/18/getting-started-with-qt-for-python/

import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    app = QApplication([])
    label = QLabel("<font color=red size=40>Qt for Python!</font>")
    label.show()
    sys.exit(app.exec_())