# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
from PyQt5.QtWidgets import QFileDialog
import threading
import sys
import pytube.exceptions

# from PyQt5.QtWidgets import QFileDialog
# import QF


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.yt=None
        self.video=None
        self.MaxFileSize=0
        MainWindow.setObjectName("YoutubeDOwnloader")
        MainWindow.resize(594, 497)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.download = QtWidgets.QPushButton(self.centralWidget)
        self.download.setGeometry(QtCore.QRect(170, 340, 251, 71))
        self.download.setObjectName("download")
        self.download.clicked.connect(self.downloadvideo)
        self.urllabel = QtWidgets.QLabel(self.centralWidget)
        self.urllabel.setGeometry(QtCore.QRect(50, 30, 61, 51))
        self.urllabel.setToolTip("")
        self.urllabel.setObjectName("urllabel")
        self.urlBox = QtWidgets.QTextEdit(self.centralWidget)
        self.urlBox.setGeometry(QtCore.QRect(180, 40, 381, 41))
        self.urlBox.setObjectName("urlBox")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 141, 61))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 280, 401, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.valuesForQuality = QtWidgets.QComboBox(self.centralWidget)
        self.valuesForQuality.setGeometry(QtCore.QRect(200, 170, 311, 25))
        self.valuesForQuality.setObjectName("valuesForQuality")
        self.valuesForQuality.addItem("")
        self.valuesForQuality.addItem("")
        self.valuesForQuality.addItem("")
        self.valuesForQuality.addItem("")
        self.valuesForQuality.addItem("")
        self.valuesForQuality.addItem("")
        self.valuesForQuality.setItemText(5, "")
        self.selectQuality = QtWidgets.QLabel(self.centralWidget)
        self.selectQuality.setGeometry(QtCore.QRect(40, 160, 121, 61))
        self.selectQuality.setObjectName("selectQuality")
        self.filePicker = QtWidgets.QPushButton(self.centralWidget)
        self.filePicker.setGeometry(QtCore.QRect(190, 120, 351, 25))
        self.filePicker.setObjectName("filePicker")
        self.filePicker.clicked.connect(
            lambda: self.showFilePicker(self.centralWidget))
        self.caption = QtWidgets.QLabel(self.centralWidget)
        self.caption.setGeometry(QtCore.QRect(110, 240, 401, 20))
        self.caption.setObjectName("caption")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 594, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuYoutube_Downloader = QtWidgets.QMenu(self.menuBar)
        self.menuYoutube_Downloader.setObjectName("menuYoutube_Downloader")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuYoutube_Downloader.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "YoutubeDownloader", "YoutubeDownloader"))
        self.download.setText(_translate("MainWindow", "Download"))
        self.urllabel.setText(_translate("MainWindow", "Enter URL"))
        self.urlBox.setPlaceholderText(_translate(
            "MainWindow", "Enter Youtube Video URL"))
        self.label.setText(_translate("MainWindow", "Select Destination"))
        self.valuesForQuality.setItemText(0, _translate("MainWindow", "240p"))
        self.valuesForQuality.setItemText(1, _translate("MainWindow", "360p"))
        self.valuesForQuality.setItemText(2, _translate("MainWindow", "480p"))
        self.valuesForQuality.setItemText(3, _translate("MainWindow", "720p"))
        self.valuesForQuality.setItemText(4, _translate("MainWindow", "1080p"))
        self.selectQuality.setText(_translate("MainWindow", "Select Quality"))
        self.filePicker.setText(_translate("MainWindow", "Select Folder"))
        self.caption.setText(_translate(
            "MainWindow", "Video Caption Shows Here"))
        self.menuYoutube_Downloader.setTitle(
            _translate("MainWindow", "Youtube Downloader"))

    def downloadvideo(self):
        # print("Hello")
        # global video
        url = self.urlBox.toPlainText()
    # url="https://www.youtube.com/watch?v=fNxTxqrWwxM&list=PL692C2B3DBB28A15C&index=3&t=0s"
        self.yt = YouTube(url)
        video_type = self.yt.streams.first()

    # file size of a file
        self.MaxfileSize = video_type.filesize
        print(threading.Thread(target=self.yt.register_on_progress_callback(self.progress_function)).start())
        print(threading.Thread(target=self.downloadFile).start())
        
        # self.video=self.yt.streams.first().download()   
        
        # self.yt.register_on_progress_callback(self)
        # self.progressBar.setValue(50)
        
        # video=yt.streams.first().download(self.filePicker.text())
        
    def downloadFile(self):
        test=self.yt.streams.first().download()
        self.video = test
        self.caption.setText(self.yt.title)



    def showFilePicker(self, centralWidget):
        fileName = QFileDialog.getExistingDirectory(
            centralWidget, "Select Folder")
        if fileName:
            print(fileName)
            self.filePicker.setText(fileName)

    def progress_function(self,stream, chunk,file_handle, bytes_remaining):
        # if(self.MaxFileSize>0):/

        percent=str(int(100-(100*bytes_remaining/self.MaxFileSize)))

        self.progressBar.setValue(int(percent))
        # self.loadingPercent.config(text=str(int(100 - (100*(bytes_remaining/self.MaxfileSize)))))
        # try:
        #     # size = self.video.filesizeself.video=self.yt.streams.first().download()   
        #     size=self.video.filesize
        #     self.caption.setText(self.yt.title)
        #     p = 0
        #     print("Called")
        #     while p <= 100:
        #         progress = p
        #         print("Inside")
        #         print (str(p)+'%')
        #         p = self.percent(bytes_remaining, size)
        #         self.progressBar.setValue(progress)
        # except  pytube.exceptions.PytubeError as perror:
        #     print(perror)
        
    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc
            
        # progress = (float(abs(bytes_remaining-size)/size))*float(100)
        # self.progressBar.setValue(progress)
        # text=urlEntry.get()
        # yt=YouTube(text,on_progress_callback=progress_function)
        # global video
        # video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        # # progress_function(video)/

        # if not pathofVideo.strip():
        #         pass
        #         yt.streams.first().download()
        #         # messagebox.showinfo("Error", "Please select a path to save video")
        # else:
        #         yt.streams.first().download(pathofVideo)
        # u = urlopen(yt.thumbnail_url)
        # raw_data = u.read()
        # u.close()
        # im = Image.open(io.BytesIO(raw_data))
        # image = ImageTk.PhotoImage(im)

        # label = Label(top,image=image)
        # label.grid(row=2)
        # label.place(relx=0.5, rely=0.5, anchor=CENTER)
        # label.grid_columnconfigure(1,weight=1)
        # title=Text(top,height=2,width=30)
        # title.grid(row=2,column=2,padx=10,pady=10,ipadx=10,ipady=10,sticky="w")
        # title.insert(END,yt.title)
        # # bar()
        # top.mainloop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
