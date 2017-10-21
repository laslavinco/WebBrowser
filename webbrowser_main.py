import os
import sys
import PyQt4
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import QUrl, QString
from PyQt4.QtGui import QIcon
from PyQt4.QtWebKit import *
class MyWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MyWindow,self).__init__()
		uiPath = os.getcwd()+"\webBrowser_UI.ui"
		uic.loadUi(uiPath,self)
		self.show()
		self.pushButton_5.setIcon(QIcon('ic_autorenew_black_18dp.png'))
		self.pushButton_2.setIcon(QIcon('ic_home_black_18dp.png'))
		self.pushButton.setIcon(QIcon('ic_arrow_back_black_18dp.png'))
		self.pushButton_3.setIcon(QIcon('ic_arrow_forward_black_18dp.png'))
		self.pushButton_6.setIcon(QIcon('ic_bookmark_border_black_18dp'))
		self.dockWidget.setWindowTitle('Bookmarks')
		self.tabWidget.removeTab(1)
		self.progressBar.hide()
		self.dockWidget.hide()
		self.webView.loadStarted.connect(self.progressBar.show)
		self.webView.loadStarted.connect(lambda: self.pushButton_5.setIcon(QIcon('ic_highlight_off_black_18dp')))
		self.webView.loadFinished.connect(lambda:self.pushButton_5.setIcon(QIcon('ic_autorenew_black_18dp.png')))
		self.webView.loadFinished.connect(lambda:self.pushButton_5.setChecked(False))
		self.pushButton_5.clicked.connect(self.reloadBtn)
		self.lineEdit.returnPressed.connect(self.loadUrl)
		self.webView.loadFinished.connect(lambda: self.progressBar.hide())
		self.webView.loadFinished.connect(lambda: self.lineEdit.setText(str(self.webView.url().toString())))
		self.pushButton.clicked.connect(lambda: self.webView.back())
		self.pushButton_3.clicked.connect(lambda: self.webView.	forward())
		self.webView.loadProgress.connect(self.progressBar.setValue)
		self.pushButton_6.clicked.connect(lambda: self.dockWidget.show())
		self.lineEdit.setFocus()
		self.pushButton_4.clicked.connect(self.addTabs)
		self.tabWidget.tabCloseRequested.connect(lambda: self.tabWidget.removeTab(self.tabWidget.currentIndex()))


	def writeHistory(self):
		url = str(self.lineEdit.text())
		with open(os.getcwd()+'/userLinks.log','a') as writer:
			toWrite = ('{link} /n').format(link = url)
			writer.write(toWrite)



	def loadUrl(self):
		url = str(self.lineEdit.text())
		self.writeHistory()
		if not url.startswith('http'):
			url = 'http://'+url
		else:
			url = url
		self.webView.load(QUrl(url))
		self.pushButton_5.setChecked(False)
		

	def reloadBtn(self):
		if  self.pushButton_5.isChecked():
			self.webView.reload()
		else:
			self.webView.stop()

	def addTabs(self):
		self.tabWidget.addTab(QtGui.QWidget(),QString('New Tab'))
		self.newWeb = PyQt4.QtWebKit.QWebView()
		gridObject = QtGui.QGridLayout(self.tabWidget.widget(self.tabWidget.count()-1))
		gridObject.addWidget(self.newWeb)
		self.newWeb.load(QUrl('http://google.com'))







if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())
