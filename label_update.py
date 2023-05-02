from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

class Worker(QThread):
    ImageUpdate = Signal(QImage)
    #Finished = Signal()
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.queue = queue
        self.ThreadActive = True

    def run(self):
        while self.ThreadActive:
            self.queue.wait()
            Image = self.queue.get()
            ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            Pic = ConvertToQtFormat.scaled(240, 180) #Qt.KeepAspectRatio
            self.ImageUpdate.emit(Pic)
        #self.Finished.emit()
    
    def stop(self):
        self.ThreadActive = False
        self.quit()

           