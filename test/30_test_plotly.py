# -*- coding: utf-8 -*-


import plotly
import plotly.offline as plt
import os
import sys
from qgis.PyQt import uic, QtCore, QtGui
try:
    from qgis.PyQt.QtGui import (QWidget,QDialog,QMainWindow, QApplication)
except ImportError:
    from qgis.PyQt.QtWidgets import (QWidget,QDialog,QMainWindow, QApplication)


class UserUI(QMainWindow):

    def __init__(self, parent=None):
        super(UserUI, self).__init__(parent=parent)
        uipath = os.path.join(os.path.dirname(__file__), '30_test_plotly', 'mainwin.ui')
        uic.loadUi(uipath, self)



if False:
    import plotly.plotly as py
    import plotly.graph_objs as go
    # Create random data with numpy
    import numpy as np

    N = 500
    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)


    # Create a trace
    trace = go.Scatter(
        x = random_x,
        y = random_y
    )

    data = [trace]

    print(data)

    py.iplot(data, filename='c://basic-line')

if True:
    import plotly.graph_objs as go

    if False:
        # create the initial html code
        raw_html = '<head><meta charset="utf-8" /></head>''<head><meta charset="utf-8" /><script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'




        raw_html += plotly.offline.plot({
                            "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
                            "layout": go.Layout(title="hello world")
                            },
                            # auto_open=True,
                             output_type='div',
                        # show_link=False,
                        # image='jpeg',
                        include_plotlyjs=False
                        #filename='c://test.html'
                         )


        # close the body and html tags
        raw_html += '</body></html>'


    if True:
        raw_html = plotly.offline.plot({
                            "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
                            "layout": go.Layout(title="hello world")
                            },
                            # auto_open=True,
                             output_type='div',
                        # show_link=False,
                        # image='jpeg',
                        # include_plotlyjs=False
                        #filename='c://test.html'
                         )

    print(raw_html)

    app = QtGui.QApplication(sys.argv)
    mainwin = UserUI()
    mainwin.webView.setHtml(raw_html)
    mainwin.webView.reload()
    mainwin.show()

    #print(mainwin.webView.)


    print('ok show')


    sys.exit(app.exec_())



    # mainwin.exec_()


    # plt.plot(fig, filename=testName + '__plot.html')



print('fin')
