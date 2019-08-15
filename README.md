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

1. Install ImageAI:

   ```
   pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.3/imageai-2.0.3-py3-none-any.whl
   ```

1. Install python-socketio:

   ```
   conda install -c conda-forge python-socketio
   ```

1. Install eventlet module for the socket:

   ```
   conda install -c conda-forge eventlet
   ```

1. Install express (for NodeJS purpose):

   ```
   npm -i -S express
   ```


### Detecting the vehicles

The trial can use webcam (or video file, change the detection.py or detection-thread.py, read: https://imageai.readthedocs.io/en/latest/video/index.html).
File detection-thread.py is a version of detection.py which uses threading for the socket communication (important).

1. Go to the root folder.

1. Run the detection-thread.py.

   ```
   python detection-thread.py
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

