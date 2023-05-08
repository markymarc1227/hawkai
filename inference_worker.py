from PySide6.QtCore import Signal, QThread
from openvino.runtime import Core
from keras.applications.inception_v3 import preprocess_input
from pathlib import Path

class InferenceWorker(QThread):
    #InferenceUpdate = Signal(list)
    def __init__(self, inference_queue ,prediction_queue, pred_counter):
        super(InferenceWorker, self).__init__()
        self.inference_queue = inference_queue
        self.prediction_queue = prediction_queue
        self.pred_counter = pred_counter
        self.ThreadActive = True

        self.ir_path = Path("accident_detection_model/InceptionV3_Combined_ModelV2.xml")
        self.ie = Core()
        self.model = self.ie.read_model(self.ir_path)
        self.compiled_model = self.ie.compile_model(model=self.model, device_name="CPU")

    def run(self):
        while self.ThreadActive:
            self.inference_queue.wait()
            frame_array = self.inference_queue.get() #returns a list where: [Frame to process, Process_Number]
            predictions = self.compiled_model(frame_array[0])[self.compiled_model.output(0)]
            print("Stream ID =",frame_array[1],*predictions)
            if predictions[0][0]>0.80:
                self.pred_counter[frame_array[1]] += 1
            else:
                self.pred_counter[frame_array[1]] = 0

            if self.pred_counter[frame_array[1]] == 3:
                self.prediction_queue.put(frame_array[1])
                print("Pred == 3!")
                self.pred_counter[frame_array[1]] = 0
    
    def stop(self):
        self.ThreadActive = False
        self.quit()

           