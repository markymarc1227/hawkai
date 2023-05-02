from PySide6.QtCore import QObject, Signal

class PredictionWorker(QObject):
    PredictionUpdate = Signal(int)
    #PredictionUpdate = Signal(str)
    Finish = Signal()
    def __init__(self, pred_queue):
        super(PredictionWorker, self).__init__()
        self.pred_queue = pred_queue

    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            self.pred_queue.wait()
            prediction = self.pred_queue.get()
            self.PredictionUpdate.emit(prediction)
    
    def stop(self):
        self.ThreadActive = False
        #self.quit()

           