from multiprocessing import shared_memory

from openvino.runtime import Core
from keras.applications.inception_v3 import preprocess_input

import cv2
import numpy as np
from skimage.transform import resize 

def start_process(video_file, queue, pred_queue, process_id):
    ie = Core()
    sh_m = shared_memory.SharedMemory(name="shared_bytes_model")
    model_bytes = bytes(sh_m.buf[:sh_m.size])
    compiled_model = ie.import_model(model_stream= model_bytes, device_name="CPU")
    sh_m.close()

    ProcessActive = True
    frame_array = []
    frame_counter = 0
    prev_prediction = 0
    pred_counter = 0

    if len(video_file) == 1:
        video_file = int(video_file)

    Capture = cv2.VideoCapture(video_file)
    while ProcessActive:
        ret, frame = Capture.read()
        
        if not ret:
            #print('Loop video')
            #Capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        if frame_counter % 30 == 0:
            resized_frame = resize(frame, preserve_range=True, output_shape=(224,224)).astype(int)
            frame_array.append(resized_frame)
            frame_array = np.array(frame_array)
            frame_array = preprocess_input(frame_array, data_format=None)
            predictions = compiled_model(frame_array)[compiled_model.output(0)] 
            # print(predictions)
            frame_array = []

        Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #FlippedImage = cv2.flip(Image, 1)
        queue.put(Image)
        
        cv2.waitKey(2)
        frame_counter += 1
        

        # if predictions[0][0]<predictions[0][1]:
        #     prediction = "No Accident"
        if predictions[0][0]>0.80: #and predictions[0][0]-predictions[0][1] > 0.80:
            prediction = 1
        else:
            prediction = 0

        prev_prediction = prediction

        if prev_prediction == 1:
            pred_counter += 1
        else:
            pred_counter = 0

        if pred_counter > 2:
            pred_queue.put(process_id)
            pred_counter = 0

        print(str(process_id))
        print(predictions)
        # else:
        #     prediction = "No Accident"

        # if prediction == "Accident" and alert == False:
        #     alert = True
        #     print("Accident Notif!")
        # elif prediction == "No Accident":
        #     alert = False

#def stop_process(process_num):

