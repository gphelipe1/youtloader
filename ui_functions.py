import youtloader as yt
import pathDownload
import sys
import youtube_dl

#-------- Globals
app = yt.QtWidgets.QApplication(sys.argv)
Youtloader = yt.QtWidgets.QMainWindow()
ui = yt.Ui_Youtloader()
ui.setupUi(Youtloader)

def startDownload():
    ydl_opts={}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ui.inputURL.text()])


ui.downloadButton.clicked.connect(startDownload)


Youtloader.show()
sys.exit(app.exec_())