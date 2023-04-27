from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QImage

class Worker(QObject):
    ImageUpdate = Signal(QImage)
    #PredictionUpdate = Signal(str)
    Finish = Signal()
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
    
    def stop(self):
        self.ThreadActive = False

           