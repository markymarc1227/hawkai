# HawkAI

This project aims to detect car crash accidents simultaneously in four monitoring streams using a modified VGG19 model, OpenVino, and PySide6.

How to run:

1. Clone this repository.
2. Setup/import a Conda environment using the environment.yml file.  
   Use command: "conda env create -n ENVNAME --file environment.yml"  
3. Activate the imported Conda environment.  
   Use command: "conda activate ENVNAME"  
4. Download the model at: https://drive.google.com/file/d/1MK0Iw11rXr25a_D_9xUUVJ-10vv5shpx/view?usp=share_link  
   Unzip and place it in the project folder. Make sure to name the model folder as "accident_detection_model".
5. Download the accident videos for testing at: https://drive.google.com/drive/folders/15-MJ6Eg1X29B8TRHo5NxePgNB06cLX3h?usp=share_link  
6. CD into the project folder.
7. Run the command "python main.py".

--OR--
1. Download ZIP file at: https://drive.google.com/file/d/193ncL7Rr8dI7x45qfcjqYG3UpWR6RN5T/view?usp=share_link
2. Extract the file.
3. In the extracted folder, go to the dist folder and run HawkAI.exe application.
