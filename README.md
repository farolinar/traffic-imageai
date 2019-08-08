# Traffic Detection System

TMS is a traffic management system that maps all the vehicles to the map.
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

1. Go to the root folder.

1. Run the vid-cap-thread.py.

   ```
   python vid-cap-thread.py
   ```
 
