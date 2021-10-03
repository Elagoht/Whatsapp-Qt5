from PyQt5.QtCore import QUrl,QFileInfo,pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction,QApplication,QMainWindow,QMenu,QSystemTrayIcon,QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem,QWebEngineView,QWebEnginePage
from sys import argv,exit
class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        self.setWindowTitle("Whatsapp Web")
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(480,360)
        self.show()
        view=QWebEngineView()
        page=WhatsApp(view)
        view.setPage(page)
        view.load(QUrl("https://web.whatsapp.com"))
        self.setCentralWidget(view)
        self.tray=QSystemTrayIcon(self)
        self.tray.setIcon(QIcon("icon.png"))
        trayShow=QAction("Show/Hide",self)
        trayExit=QAction("Exit",self)
        trayShow.triggered.connect(lambda:self.show() if self.isHidden() else self.hide())
        trayExit.triggered.connect(app.quit)
        trayMenu=QMenu()
        trayMenu.addAction(trayShow)
        trayMenu.addAction(trayExit)
        self.tray.setContextMenu(trayMenu)
        self.tray.show()
    def closeEvent(self,event):
        event.ignore()
        self.hide()
class WhatsApp(QWebEnginePage):
    def __init__(self,*args,**kwargs):
        QWebEnginePage.__init__(self,*args,**kwargs)
        self.profile().downloadRequested.connect(self.download)
        self.profile().defaultProfile().setHttpUserAgent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.129 Safari/537.36")
        self.featurePermissionRequested.connect(self.permission)
    def permission(self,frame,feature):self.setFeaturePermission(frame,feature,QWebEnginePage.PermissionGrantedByUser)
    @pyqtSlot(QWebEngineDownloadItem)
    def download(self,download):
        old_path=download.path()
        suffix=QFileInfo(old_path).suffix()
        path=QFileDialog.getSaveFileName(self.view(),"Save File",old_path,"*."+suffix)[0]
        if path:
            download.setPath(path)
            download.accept()
app=QApplication(argv)
main=MainWin()
exit(app.exec_())