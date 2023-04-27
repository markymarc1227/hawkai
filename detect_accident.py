from multiprocessing import Process

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

import cv2
import numpy as np
from pathlib import Path
from skimage.transform import resize 


from openvino.runtime import Core
from keras.applications.inception_v3 import preprocess_input

class Worker(QThread):
    ImageUpdate = Signal(QImage)
    PredictionUpdate = Signal(str)
    
    def __init__(self, video_file):
        super().__init__()
        self.video_file = video_file
        
    ir_path = Path("accident_detection_model/InceptionV3_Combined_Model.xml")
    ie = Core()
    model = ie.read_model(ir_path)
    compiled_model = ie.compile_model(model=model, device_name="CPU")
    input_key = compiled_model.input(0)
    output_key = compiled_model.output(0)
    #print(input_key.shape)

    def run(self):
        self.ThreadActive = True
        #video_file_path = "C:\\Users\\krist\\repos\\convlstm_testing\\rollingaverage_accident-detect\\accident-testing\\test3.mp4"
        frame_array = []
        frame_counter = 0
        alert = False
        if len(self.video_file) == 1:
            self.video_file = int(self.video_file)

        Capture = cv2.VideoCapture(self.video_file)
        while self.ThreadActive:
            ret, frame = Capture.read()

            if not ret:
                print('Loop video')
                Capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            if frame_counter % 30 == 0:
                resized_frame = resize(frame, preserve_range=True, output_shape=(224,224)).astype(int)
                frame_array.append(resized_frame)
                frame_array = np.array(frame_array)
                frame_array = preprocess_input(frame_array, data_format=None)
                predictions = self.compiled_model(frame_array)[self.output_key] 
                frame_array = []

                
                
            Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #FlippedImage = cv2.flip(Image, 1)
            ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
            Pic = ConvertToQtFormat.scaled(240, 180) #Qt.KeepAspectRatio
            self.ImageUpdate.emit(Pic)
            cv2.waitKey(10)

            frame_counter += 1

            # accident_predict_score1 = round(predictions[0][0],4)
            # accident_predict_score2 = round(predictions[0][1],4)

            if predictions[0][0]<predictions[0][1]:
                prediction = "No Accident"
                self.PredictionUpdate.emit(prediction)
            elif predictions[0][0]>0.80: #and predictions[0][0]-predictions[0][1] > 0.80:
                prediction = "Accident"
                self.PredictionUpdate.emit(prediction)
            else:
                prediction = "No Accident"
                self.PredictionUpdate.emit(prediction)

            if prediction == "Accident" and alert == False:
                alert = True
                print("Accident Notif!")
            elif prediction == "No Accident":
                alert = False

    def stop(self):
        self.ThreadActive = False
        self.quit()