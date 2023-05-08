from PySide6.QtCore import Signal, QThread

class PredictionWorker(QThread):
    PredictionUpdate = Signal(int)
    def __init__(self, pred_queue):
        super(PredictionWorker, self).__init__()
        self.pred_queue = pred_queue
        self.ThreadActive = True

    def run(self):
        while self.ThreadActive:
            self.pred_queue.wait()
            prediction = self.pred_queue.get()
            self.PredictionUpdate.emit(prediction)
        print("from prediction update worker")

    def stop(self):
        self.ThreadActive = False
        self.quit()

           