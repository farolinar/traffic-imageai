# Traffic Detection System (TDS)

TDS is a traffic detaction system that detects all the vehicles in a video stream from CCTV.
The code uses ImageAI (https://github.com/OlafenwaMoses/ImageAI).

## How to Use

### Preparing the project

1. Clone this repository

   ```
   git clone https://github.com/farolinar/traffic-imageai.git
   ```
   
1. [Download](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5) the RetinaNet model file that will be used for object detection.

### Preparing the environment

Use the terminal or an Anaconda Prompt for the following steps:

1. Create the conda environment from the environment.yml file:

   ```
   conda env create -f environment.yml
   ```

1. Create the conda environment from the environment.yml file:

   ```
   conda activate traffic
   ```


### Detecting the vehicles

The trial can use webcam (or video file, change the vid-cap.py or vid-cap-thread.py, read: https://imageai.readthedocs.io/en/latest/video/index.html).
File vid-cap-thread.py is a version of vid-cap.py which uses threading for the socket communication (important).

1. Go to the root folder.

1. Run the vid-cap-thread.py.

   ```
   python vid-cap-thread.py
   ```

1. Open another terminal and run the NodeJS.

   ```
   node index.js
   ```

1. Go to localhost:3000/client.


## Problem
   ```
   Received a broken close frame containing invalid UTF-8.
   ```

