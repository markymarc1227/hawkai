#-------------------MULTIPROCESSING RELATED-------------------------#

from multiprocessing import Queue, Process, shared_memory, Event

def start_process(video_file, queue, pred_queue, process_id, event):
    ie = Core()
    sh_m = shared_memory.SharedMemory(name="shared_bytes_model")
    model_bytes = bytes(sh_m.buf[:sh_m.size])
    compiled_model = ie.import_model(model_stream= model_bytes, device_name="CPU")
    sh_m.close()

    # ProcessActive = True
    frame_array = []
    frame_counter = 0
    pred_counter = 0

    if len(video_file) == 1:
        video_file = int(video_file)
    Capture = cv2.VideoCapture(video_file)
    while True:
        ret, frame = Capture.read()
        if event.is_set():
            break
        if not ret:
            # print('Loop video')
            Capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        if frame_counter % 20 == 0:
            resized_frame = resize(frame, preserve_range=True, output_shape=(224,224)).astype(int)
            frame_array.append(resized_frame)
            frame_array = np.array(frame_array)
            frame_array = preprocess_input(frame_array, data_format=None)
            predictions = compiled_model(frame_array)[compiled_model.output(0)] 
            print("Stream ID =",process_id,*predictions)
            frame_array = []
            if predictions[0][0]>0.80:
                pred_counter += 1
            else:
                pred_counter = 0

        Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #FlippedImage = cv2.flip(Image, 1)
        queue.put(Image)
        cv2.waitKey(1)
        frame_counter += 1
        
        #print(pred_counter)
        
        if pred_counter == 3:
            print("Pred == 2!")
            pred_queue.put(process_id)
            pred_counter = 0

        predictions = [[0,0]]

    print("Process was stopped. (From Child Process)")

from openvino.runtime import Core
from keras.applications.inception_v3 import preprocess_input

import cv2
import numpy as np
from skimage.transform import resize 

import os
from pathlib import Path
#-------------------MULTIPROCESSING RELATED-------------------------#

#-------------------ARDUINO RELATED-------------------------#
import sys

import time
import serial

try:
    serialcomm = serial.Serial("COM3",9600)
    time.sleep(2)
except:
    pass
    # print("Already opened.")

def accident(info):
    print("Accident Detected!")
    serialcomm.write(info.encode('utf-8'))

def reset():
    print("Resetting..")
    serialcomm.write(b"0\r\n")
#-------------------ARDUINO RELATED-------------------------#

#-------------------PYSIDE6 RELATED-------------------------#

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QInputDialog, QLineEdit
from PySide6.QtCore import Qt, QTimer, QDateTime, QThread
from PySide6.QtGui import QPixmap, QImage

from SpoolingQueue import SpoolingQueue
from label_update import Worker
from ui_mainwidget import Ui_MainWidget
from prediction_update import PredictionWorker

class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.current_stream = 0
        self.previous_stream = 0
        self.alarm_message = ""
        self.video_file_path = {}
        self.prediction_holder = ""
        self.alarm_status = False
        self.alarm_time = ""
        self.prediction_list = []
        self.workers = {}
        #self.threads = {}
        self.processes = {}
        self.locations = {}
        self.responders = {}
        self.video_frames = {
            0: self.video_frame_0,
            1: self.video_frame_1,
            2: self.video_frame_2,
            3: self.video_frame_3
        }
        self.image_update_slots = {
            0: self.ImageUpdateSlot1,
            1: self.ImageUpdateSlot2,
            2: self.ImageUpdateSlot3,
            3: self.ImageUpdateSlot4
        }
        self.selection_labels = {
            0: self.selector_0,
            1: self.selector_1,
            2: self.selector_2,
            3: self.selector_3
        }
        self.prediction_queue = SpoolingQueue()
        self.video_queues = [SpoolingQueue() for _ in self.video_frames]
        self.events = [Event() for _ in self.video_frames]
        
        self.ir_path = Path("accident_detection_model/InceptionV3_Combined_ModelV2.xml")
        self.ie = Core()
        self.model = self.ie.read_model(self.ir_path)
        self.compiled_model = self.ie.compile_model(model=self.model, device_name="CPU")
        self.model_bytes = self.compiled_model.export_model()
        # with open('./bytes_model', 'wb') as f:
        #     f.write(self.model_bytes)

        self.shm = shared_memory.SharedMemory(name="shared_bytes_model", create=True, size=len(self.model_bytes))
        self.shm.buf[:len(self.model_bytes)] = self.model_bytes 
        
        # self.np_array = np.ndarray(self.model_bytes.shape, dtype=self.model_bytes.dtype, buffer=self.shm.buf)
        # self.np_array[:] = self.model_bytes[:]

        # self.shm.close()
        # self.shm.unlink()

        # Creates a timer to update the time label every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.UpdateDateTime)
        self.timer.start(1000)
        # Update the time label initially
        self.UpdateDateTime()
        self.UpdatePrediction(self.prediction_queue)

        for video_frame in self.video_frames:
            self.video_frames[video_frame].clicked.connect(self.HandleVideoClick)
        
        self.loc_0.returnPressed.connect(self.OnEnterLocation)
        self.loc_1.returnPressed.connect(self.OnEnterLocation)
        self.loc_2.returnPressed.connect(self.OnEnterLocation)
        self.loc_3.returnPressed.connect(self.OnEnterLocation)
        self.loc_0.doubleClicked.connect(self.OnDoubleClickLocation)
        self.loc_1.doubleClicked.connect(self.OnDoubleClickLocation)
        self.loc_2.doubleClicked.connect(self.OnDoubleClickLocation)
        self.loc_3.doubleClicked.connect(self.OnDoubleClickLocation)
        self.res_cnum0.returnPressed.connect(self.OnEnterResponders)
        self.res_cnum1.returnPressed.connect(self.OnEnterResponders)
        self.res_cnum0.textChanged.connect(self.CheckResponderNum)
        self.res_cnum1.textChanged.connect(self.CheckResponderNum)
        self.res_cnum0.doubleClicked.connect(self.OnDoubleClickLocation)
        self.res_cnum1.doubleClicked.connect(self.OnDoubleClickLocation)

        #self.stream_select.currentIndexChanged.connect(self.OnComboBoxChange)

        self.add_ip_cam.clicked.connect(self.AddIpStream)
        self.video_file_button.clicked.connect(self.SelectVideo)
        self.open_camera_button.clicked.connect(self.OpenCamera)
        self.stop_button.clicked.connect(self.StopFeed)
        self.start_button.clicked.connect(self.StartFeed)
        self.clear_predictions.clicked.connect(self.ClearPredictions)
        
    
    def StartFeed(self):
        #Starts worker thread for video feed
        try:
            if(len(self.video_file_path[self.current_stream]) != 0):
                print("Process started!")
                self.processes[self.current_stream] = Process(target=start_process,args=(self.video_file_path[self.current_stream], self.video_queues[self.current_stream], self.prediction_queue, self.current_stream, self.events[self.current_stream]))
                self.processes[self.current_stream].start()
                self.UpdateLabel(self.video_queues[self.current_stream])
                #self.Worker[self.current_stream].PredictionUpdate.connect(self.UpdatePredictionSlot)
            else:
                self.video_frames[self.current_stream].setText("No video file to process. \n Please select a video file or open camera.")   
        except:
            self.video_frames[self.current_stream].setText("Error Occurred. \n Please select a video file or open camera.")   
    
    def UpdateLabel(self, queue):
        self.workers[self.current_stream] = Worker(queue)
        self.workers[self.current_stream].ImageUpdate.connect(self.image_update_slots[self.current_stream])
        self.workers[self.current_stream].finished.connect(self.StopProcess)
        self.workers[self.current_stream].start()

    def UpdatePrediction(self, pred_queue):
        self.predictionthread = QThread()
        self.predictionWorker = PredictionWorker(pred_queue)
        self.predictionWorker.moveToThread(self.predictionthread)
        self.predictionthread.started.connect(self.predictionWorker.run)
        self.predictionWorker.PredictionUpdate.connect(self.Prediction_Update_Slot)
        self.predictionthread.start()
    
    def Prediction_Update_Slot(self, prediction):
        if prediction not in self.prediction_list:
            self.prediction_list.append(prediction)
            self.prediction_holder += "Cam" + str(self.prediction_list[-1]+1) + " " 
            self.prediction_label.setText(self.prediction_holder)
            # print(prediction)
            # print(self.locations)
            self.alarm_message = str(prediction+1)+self.responders[0]+self.responders[1]+self.alarm_time+self.locations[prediction]
            print("Accident Detected!")
            print(self.alarm_message)
            self.video_frames[prediction].setStyleSheet("border: 10px solid red;")
            # accident(self.alarm_message)

            # if self.alarm_status == False:
            #     accident(self.alarm_message)
            #     self.alarm_status = True
            # elif self.alarm_status == True:
            #     accident(self.alarm_message)
        #print("STREAM",prediction)
            
    def ClearPredictions(self):
        self.alarm_status = False
        self.prediction_holder = ""
        self.prediction_label.setText(self.prediction_holder)
        for item in self.prediction_list:
            self.video_frames[item].setStyleSheet("border: 2px solid black;")
        self.prediction_list.clear()
        reset()

    def StopProcess(self):
        self.events[self.current_stream].set()
        self.processes[self.current_stream].join()
        # self.processes[self.current_stream].terminate()
        print("Process was stopped.")
        # del self.processes[self.current_stream]
        self.events[self.current_stream].clear()
        print("Processes")
        print(self.processes)

    def StopFeed(self):
        self.workers[self.current_stream].stop()
        #self.threads[self.current_stream].quit()
        # self.threads[self.current_stream].wait()
        print("Thread was stopped.")
        # self.events[self.current_stream].clear()
        # self.threads[self.current_stream].quit()
        # self.threads[self.current_stream].wait()
        # print("Thread was stopped.")
        
        # del self.workers[self.current_stream]
        # del self.threads[self.current_stream]
        
        print("Worker Objects")
        print(self.workers)

    def ImageUpdateSlot1(self, Image):
        self.video_frame_0.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot2(self, Image):
        self.video_frame_1.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot3(self, Image):
        self.video_frame_2.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot4(self, Image):
        self.video_frame_3.setPixmap(QPixmap.fromImage(Image))

    def UpdateDateTime(self):
        current_datetime = QDateTime(QDateTime.currentDateTime())
        self.alarm_time = current_datetime.toString("hh:mmap")
        self.date_comp.setText(current_datetime.toString("MM/dd/yyyy"))
        self.time_comp.setText(current_datetime.toString("hh:mm:ss ap"))
        self.day_comp.setText(current_datetime.toString("dddd"))

    def SelectVideo(self):
        file_name,_ = QFileDialog.getOpenFileName(self, "Open File",
                                 os.getcwd(),
                                 "Videos (*.mp4 *.avi)")
        if((file_name == "")):
            return
        self.video_file_path[self.current_stream] = file_name
        file_base_name = os.path.basename(file_name)
        self.video_frames[self.current_stream].setText(file_base_name+" has been loaded. Press Start.") 

    def OpenCamera(self):
        self.video_file_path = "0"
        self.video_frames[self.current_stream].setText("Camera Loaded. Press Start.")

    def AddIpStream(self):
        text, ok = QInputDialog.getText(self, "Enter Camera IP Address",
                                "IP Address:", QLineEdit.Normal)
        if ok and text:
            self.video_file_path[self.current_stream] = text + "/video"
            self.video_frames[self.current_stream].setText("An IP Address was set, click Start.")

    def HandleVideoClick(self):
        self.previous_stream = self.current_stream
        self.current_stream = int(self.sender().objectName()[-1])
        print("current stream:",self.current_stream)
        self.selection_labels[self.previous_stream].setStyleSheet("")
        self.selection_labels[self.current_stream].setStyleSheet("background-color: green;")

    # def OnComboBoxChange(self, value):
    #     self.previous_stream = self.current_stream
    #     self.current_stream = value
    #     self.video_frames[self.previous_stream].setStyleSheet("border: 2px solid black;")
    #     self.video_frames[self.current_stream].setStyleSheet("border: 4px solid green;")

    # def CheckLocationLength(self):
    #     self.loc_num = sender().objectName()
    #     if len(self.loc_num.text()) > self.loc_num.maxLength():
    #         self.loc_num.setText(self.loc_num.text()[:-1])

    def OnEnterLocation(self):
        self.locations[int(self.sender().objectName()[-1])] = self.sender().text()
        self.sender().setEnabled(False)
        # print(self.locations)

    def OnEnterResponders(self):
        self.responders[int(self.sender().objectName()[-1])] = self.sender().text()
        self.sender().setEnabled(False)
        # print(self.responders)

    def OnDoubleClickLocation(self):
        self.sender().setEnabled(True)

    def CheckResponderNum(self, value):
        self.res_num = self.sender()
        try:
            value = int(value)
            self.res_num.setStyleSheet("")
            
        except:
            self.res_num.setText(self.res_num.text()[:-1])
            self.res_num.setStyleSheet("border: 2px solid red;")

    def UpdateAlarm(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWidget(app)
    window.show()

    app.exec()