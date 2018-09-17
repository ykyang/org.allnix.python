import sys
import random

from PySide2.QtCore import Qt, QObject, Signal, Slot
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide2.QtWidgets import QDialog, QLineEdit, QMainWindow
from PySide2.QtWidgets import QSizePolicy
from PySide2.QtCharts import QtCharts

from PySide2.QtCore import qApp, QPointF, Qt
from PySide2.QtGui import QColor, QPainter, QPalette
from random import random, uniform

import allnix.qt.ui_themewidget

class MyWidget(QWidget):
    """
    http://blog.qt.io/blog/2018/05/04/hello-qt-for-python/
    """
    layout: QVBoxLayout
    text: QLabel
    hello: list
    button: QPushButton

    def __init__(self):
        QWidget.__init__(self)

        self.hello = ['Hallo welt!', 'Ciao mondo!', 'Hei maailma!', 'Hola mundo!',
                      'Hei verden!', '你好，世界', 'Привет мир']

        self.button= QPushButton('Click me!')
        self.text = QLabel('Hello World')
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.magic)

        #print(type(self.button.clicked))

    def magic(self):
        self.text.setText(random.choice(self.hello))

class MyForm(QDialog):
    """
    https://wiki.qt.io/Qt_for_Python_Tutorial_SimpleDialog
    """
    button: QPushButton
    edit: QLineEdit

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")
        self.edit = QLineEdit('Write my name here')
        self.button = QPushButton('Show Greetings')
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print('Hello {}'.format(self.edit.text()))

class MyCommunicate(QObject):
    """
    https://wiki.qt.io/Qt_for_Python_Signals_and_Slots
    """
    signal_number = Signal(int)
    signal_word = Signal(str)
    signal_multiplex = Signal((int,), (str,))



    @Slot(int)
    @Slot(str)
    def say_something(self, words):
        print(words)


class MyMainWindow(QMainWindow):
    """
    miniconda3/envs/py37/lib/python3.7/site-packages/
    PySide2/examples/charts/percentbarchart.py
    """
    def __init__(self):
        QMainWindow.__init__(self)

        set0 = QtCharts.QBarSet("Jane")
        set1 = QtCharts.QBarSet("John")
        set2 = QtCharts.QBarSet("Axel")
        set3 = QtCharts.QBarSet("Mary")
        set4 = QtCharts.QBarSet("Samantha")

        set0.append([1, 2, 3,  4, 5, 6])
        set1.append([5, 0, 0,  4, 0, 7])
        set2.append([3, 5, 8, 13, 8, 5])
        set3.append([5, 6, 7,  3, 4, 5])
        set4.append([9, 7, 5,  3, 1, 2])

        series = QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Simple percentbarchart example")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)


class MyThemeWidget(QWidget):
    """
    Generate ui_themewidget.py with
        pyside2-uic themewidget.ui -o ui_themewidget.py
    """
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.charts = []

        self.ui = allnix.qt.ui_themewidget.Ui_ThemeWidgetForm() #ui()
        self.list_count = 3
        self.value_max = 10
        self.value_count = 7
        self.data_table = self.generate_random_data(self.list_count,
            self.value_max, self.value_count)

        self.ui.setupUi(self)
        self.populate_themebox()
        self.populate_animationbox()
        self.populate_legendbox()

        # Area Chart
        chart_view =  QtCharts.QChartView(self.create_areachart())
        self.ui.gridLayout.addWidget(chart_view, 1, 0)
        self.charts.append(chart_view)

        # Pie Chart
        chart_view =  QtCharts.QChartView(self.createPieChart())
        chart_view.setSizePolicy(QSizePolicy.Ignored,
            QSizePolicy.Ignored)
        self.ui.gridLayout.addWidget(chart_view, 1, 1)
        self.charts.append(chart_view)

        # Line Chart
        chart_view =  QtCharts.QChartView(self.createLineChart())
        self.ui.gridLayout.addWidget(chart_view, 1, 2)
        self.charts.append(chart_view)

        # Bar Chart
        chart_view =  QtCharts.QChartView(self.createBarChart())
        self.ui.gridLayout.addWidget(chart_view, 2, 0)
        self.charts.append(chart_view)

        # Spline Chart
        chart_view =  QtCharts.QChartView(self.createSplineChart())
        self.ui.gridLayout.addWidget(chart_view, 2, 1)
        self.charts.append(chart_view)

        # Scatter Chart
        chart_view =  QtCharts.QChartView(self.create_scatterchart())
        self.ui.gridLayout.addWidget(chart_view, 2, 2)
        self.charts.append(chart_view)

        # Set defaults
        self.ui.antialiasCheckBox.setChecked(True)

        # Set the colors from the light theme as default ones
        pal = qApp.palette()
        pal.setColor(QPalette.Window, QColor(0xf0f0f0))
        pal.setColor(QPalette.WindowText, QColor(0x404044))
        qApp.setPalette(pal)

        self.updateUI()


    def generate_random_data(self, list_count, value_max, value_count):
        data_table = []
        for i in range(list_count):
            data_list = []
            y_value = 0
            for j in range(value_count):
                constant = value_max / float(value_count)
                y_value += uniform(0, constant)
                x_value = (j + random()) * constant
                value = QPointF(x_value, y_value)
                label = "Slice {}: {}".format(i, j)
                data_list.append((value, label))
            data_table.append(data_list)

        return data_table

    def populate_themebox(self):
        theme = self.ui.themeComboBox
        qchart = QtCharts.QChart

        theme.addItem("Light", qchart.ChartThemeLight)
        theme.addItem("Blue Cerulean", qchart.ChartThemeBlueCerulean)
        theme.addItem("Dark", qchart.ChartThemeDark)
        theme.addItem("Brown Sand", qchart.ChartThemeBrownSand)
        theme.addItem("Blue NCS", qchart.ChartThemeBlueNcs)
        theme.addItem("High Contrast", qchart.ChartThemeHighContrast)
        theme.addItem("Blue Icy", qchart.ChartThemeBlueIcy)
        theme.addItem("Qt", qchart.ChartThemeQt)

    def populate_animationbox(self):
        animated = self.ui.animatedComboBox
        qchart = QtCharts.QChart

        animated.addItem("No Animations", qchart.NoAnimation)
        animated.addItem("GridAxis Animations", qchart.GridAxisAnimations)
        animated.addItem("Series Animations", qchart.SeriesAnimations)
        animated.addItem("All Animations", qchart.AllAnimations)

    def populate_legendbox(self):
        legend = self.ui.legendComboBox

        legend.addItem("No Legend ", 0)
        legend.addItem("Legend Top", Qt.AlignTop)
        legend.addItem("Legend Bottom", Qt.AlignBottom)
        legend.addItem("Legend Left", Qt.AlignLeft)
        legend.addItem("Legend Right", Qt.AlignRight)

    def create_areachart(self):
        chart = QtCharts.QChart()
        chart.setTitle("Area Chart")

        # The lower series initialized to zero values
        lower_series = None
        name = "Series "
        for i in range(len(self.data_table)):
            upper_series = QtCharts.QLineSeries(chart)
            for j in range(len(self.data_table[i])):
                data = self.data_table[i][j]
                if lower_series:
                    points = lower_series.pointsVector()
                    y_value = points[i].y() + data[0].y()
                    upper_series.append(QPointF(j, y_value))
                else:
                    upper_series.append(QPointF(j, data[0].y()))
            area = QtCharts.QAreaSeries(upper_series, lower_series)
            area.setName("{}{}".format(name, i))
            chart.addSeries(area)
            lower_series = upper_series

        chart.createDefaultAxes()
        chart.axisX().setRange(0, self.value_count - 1)
        chart.axisY().setRange(0, self.value_max)
        # Add space to label to add space between labels and axis
        chart.axisY().setLabelFormat("%.1f  ")

        return chart

    def createBarChart(self):
        chart = QtCharts.QChart()
        chart.setTitle("Bar chart")

        series = QtCharts.QStackedBarSeries(chart)
        for i in range(len(self.data_table)):
            barset = QtCharts.QBarSet("Bar set {}".format(i))
            for data in self.data_table[i]:
                barset.append(data[0].y())
            series.append(barset)

        chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisY().setRange(0, self.value_max * 2)
        # Add space to label to add space between labels and axis
        chart.axisY().setLabelFormat("%.1f  ")

        return chart

    def createLineChart(self):
        chart = QtCharts.QChart()
        chart.setTitle("Line chart")

        name = "Series "
        for i, lst in enumerate(self.data_table):
            series = QtCharts.QLineSeries(chart)
            for data in lst:
                series.append(data[0])
            series.setName("{}{}".format(name, i))
            chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisX().setRange(0, self.value_max)
        chart.axisY().setRange(0, self.value_count)
        # Add space to label to add space between labels and axis
        chart.axisY().setLabelFormat("%.1f  ")

        return chart

    def createPieChart(self):
        chart = QtCharts.QChart()
        chart.setTitle("Pie chart")

        series = QtCharts.QPieSeries(chart)
        for data in self.data_table[0]:
            slc = series.append(data[1], data[0].y())
            if data == self.data_table[0][0]:
                # Show the first slice exploded with label
                slc.setLabelVisible()
                slc.setExploded()
                slc.setExplodeDistanceFactor(0.5)

        series.setPieSize(0.4)
        chart.addSeries(series)

        return chart

    def createSplineChart(self):
        chart = QtCharts.QChart()
        chart.setTitle("Spline chart")
        name = "Series "
        for i, lst in enumerate(self.data_table):
            series = QtCharts.QSplineSeries(chart)
            for data in lst:
                series.append(data[0])
            series.setName("{}{}".format(name, i))
            chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisX().setRange(0, self.value_max)
        chart.axisY().setRange(0, self.value_count)
        # Add space to label to add space between labels and axis
        chart.axisY().setLabelFormat("%.1f  ")

        return chart

    def create_scatterchart(self):
        chart = QtCharts.QChart()
        chart.setTitle("Scatter chart")
        name = "Series "
        for i, lst in enumerate(self.data_table):
            series = QtCharts.QScatterSeries(chart)
            for data in lst:
                series.append(data[0])
            series.setName("{}{}".format(name, i))
            chart.addSeries(series)

        chart.createDefaultAxes()
        chart.axisX().setRange(0, self.value_max)
        chart.axisY().setRange(0, self.value_count)
        # Add space to label to add space between labels and axis
        chart.axisY().setLabelFormat("%.1f  ")

        return chart

    def updateUI(self):
        def set_colors(window_color, text_color):
            pal = self.window().palette()
            pal.setColor(QPalette.Window, window_color)
            pal.setColor(QPalette.WindowText, text_color)
            self.window().setPalette(pal)

        idx = self.ui.themeComboBox.currentIndex()
        theme = self.ui.themeComboBox.itemData(idx)
        qchart = QtCharts.QChart

        if len(self.charts):
            chart_theme = self.charts[0].chart().theme()
            if chart_theme != theme:
                for chart_view in self.charts:
                    if theme == 0:
                        theme_name = qchart.ChartThemeLight
                    elif theme == 1:
                        theme_name = qchart.ChartThemeBlueCerulean
                    elif theme == 2:
                        theme_name = qchart.ChartThemeDark
                    elif theme == 3:
                        theme_name = qchart.ChartThemeBrownSand
                    elif theme == 4:
                        theme_name = qchart.ChartThemeBlueNcs
                    elif theme == 5:
                        theme_name = qchart.ChartThemeHighContrast
                    elif theme == 6:
                        theme_name = qchart.ChartThemeBlueIcy
                    elif theme == 7:
                        theme_name = qchart.ChartThemeQt
                    else:
                        theme_name = qchart.ChartThemeLight

                    chart_view.chart().setTheme(theme_name)

                # Set palette colors based on selected theme
                if theme == qchart.ChartThemeLight:
                    set_colors(QColor(0xf0f0f0), QColor(0x404044))
                elif theme == qchart.ChartThemeDark:
                    set_colors(QColor(0x121218), QColor(0xd6d6d6))
                elif theme == qchart.ChartThemeBlueCerulean:
                    set_colors(QColor(0x40434a), QColor(0xd6d6d6))
                elif theme == qchart.ChartThemeBrownSand:
                    set_colors(QColor(0x9e8965), QColor(0x404044))
                elif theme == qchart.ChartThemeBlueNcs:
                    set_colors(QColor(0x018bba), QColor(0x404044))
                elif theme == qchart.ChartThemeHighContrast:
                    set_colors(QColor(0xffab03), QColor(0x181818))
                elif theme == qchart.ChartThemeBlueIcy:
                    set_colors(QColor(0xcee7f0), QColor(0x404044))
                else:
                    set_colors(QColor(0xf0f0f0), QColor(0x404044))


        # Update antialiasing
        checked = self.ui.antialiasCheckBox.isChecked()
        for chart in self.charts:
            chart.setRenderHint(QPainter.Antialiasing, checked)

        # Update animation options
        idx = self.ui.animatedComboBox.currentIndex()
        options = self.ui.animatedComboBox.itemData(idx)

        if len(self.charts):
            chart = self.charts[0].chart()
            animation_options = chart.animationOptions()
            if animation_options != options:
                for chart_view in self.charts:
                    chart_view.chart().setAnimationOptions(options)

        # Update legend alignment
        idx = self.ui.legendComboBox.currentIndex()
        alignment = self.ui.legendComboBox.itemData(idx)

        if not alignment:
            for chart_view in self.charts:
                chart_view.chart().legend().hide()
        else:
            for chart_view in self.charts:
                chart_view.chart().legend().setAlignment(alignment)
                chart_view.chart().legend().show()