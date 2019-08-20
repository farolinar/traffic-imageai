from imageai.Detection import VideoObjectDetection
import os
import threading

import eventlet
import socketio

from matplotlib import pyplot as plt

from vid_cap import VideoCap


# url = 'redis://hostname:port/0'
# sio = socketio.Server(client_manager=socketio.RedisManager(url))

# sio = socketio.Server(ping_timeout=10, binary=True)
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

execution_path = os.getcwd()

color_index = {'bus': 'red', 'handbag': 'steelblue', 'giraffe': 'orange', 'spoon': 'gray', 'cup': 'yellow', 'chair': 'green', 'elephant': 'pink', 'truck': 'indigo', 'motorcycle': 'azure', 'refrigerator': 'gold', 'keyboard': 'violet', 'cow': 'magenta', 'mouse': 'crimson', 'sports ball': 'raspberry', 'horse': 'maroon', 'cat': 'orchid', 'boat': 'slateblue', 'hot dog': 'navy', 'apple': 'cobalt', 'parking meter': 'aliceblue', 'sandwich': 'skyblue', 'skis': 'deepskyblue', 'microwave': 'peacock', 'knife': 'cadetblue', 'baseball bat': 'cyan', 'oven': 'lightcyan', 'carrot': 'coldgrey', 'scissors': 'seagreen', 'sheep': 'deepgreen', 'toothbrush': 'cobaltgreen', 'fire hydrant': 'limegreen', 'remote': 'forestgreen', 'bicycle': 'olivedrab', 'toilet': 'ivory', 'tv': 'khaki', 'skateboard': 'palegoldenrod', 'train': 'cornsilk', 'zebra': 'wheat', 'tie': 'burlywood', 'orange': 'melon', 'bird': 'bisque', 'dining table': 'chocolate', 'hair drier': 'sandybrown', 'cell phone': 'sienna', 'sink': 'coral', 'bench': 'salmon', 'bottle': 'brown', 'car': 'silver', 'bowl': 'maroon', 'tennis racket': 'palevilotered', 'airplane': 'lavenderblush', 'pizza': 'hotpink', 'umbrella': 'deeppink', 'bear': 'plum', 'fork': 'purple', 'laptop': 'indigo', 'vase': 'mediumpurple', 'baseball glove': 'slateblue', 'traffic light': 'mediumblue', 'bed': 'navy', 'broccoli': 'royalblue', 'backpack': 'slategray', 'snowboard': 'skyblue', 'kite': 'cadetblue', 'teddy bear': 'peacock', 'clock': 'lightcyan', 'wine glass': 'teal', 'frisbee': 'aquamarine', 'donut': 'mincream', 'suitcase': 'seagreen', 'dog': 'springgreen', 'banana': 'emeraldgreen', 'person': 'honeydew', 'surfboard': 'palegreen', 'cake': 'sapgreen', 'book': 'lawngreen', 'potted plant': 'greenyellow', 'toaster': 'ivory', 'stop sign': 'beige', 'couch': 'khaki'}


resized = False

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080       # Port to listen on (non-privileged ports are > 1023)


class myThread (threading.Thread):
    def __init__(self, category):
        threading.Thread.__init__(self)
        self.category = category
        if self.category == 1:
            self.name = "InitSocket"
        elif self.category == 2:
            self.name = "Sender"
        else:
            print("Wrong category")

    def run(self):
        print("Starting thread " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        if self.category == 1:
            init_socket()
        elif self.category == 2:
            sender()
        else:
            print("Wrong thread category")
        # Free lock to release next thread
        # threadLock.release()

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
def forFrame(frame_number, output_array, output_count, returned_frame):
    # print("forFrame "+ str(frame_number))
    # sio.emit('reply', 'aku python', namespace='/chat')
    plt.clf()

    this_colors = []
    labels = []
    sizes = []

    counter = 0

    for eachItem in output_count:
        counter += 1
        labels.append(eachItem + " = " + str(output_count[eachItem]))
        sizes.append(output_count[eachItem])
        this_colors.append(color_index[eachItem])

    global resized

    if (resized == False):
        manager = plt.get_current_fig_manager()
        manager.resize(width=1000, height=500)
        resized = True

    plt.subplot(1, 2, 1)
    plt.title("Frame : " + str(frame_number))
    plt.axis("off")
    plt.imshow(returned_frame, interpolation="none")

    plt.subplot(1, 2, 2)
    plt.title("Analysis: " + str(frame_number))
    plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%1.1f%%")

    plt.pause(0.01)


def init_socket():
    print("Starting socket...")
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)

def sender():
    print("Starting detection")
    # eventlet.monkey_patch()
    # sio.start_background_task(detecting)
    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsRetinaNet()
    video_detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1_4.h5"))
    # video_detector.setModelPath(os.path.join(execution_path, "v2.h5"))
    video_detector.loadModel()

    vidcap = VideoCap()
    camera = vidcap.camera()
    video_path = video_detector.detectObjectsFromVideo(camera_input=camera, save_detected_video = False,
        frames_per_second=20, log_progress=True, minimum_percentage_probability=30, per_frame_function=forFrame,
        return_detected_frame=True)


# Create new threads
threadInit = myThread(1)
threadSender = myThread(2)

# sio.start_background_task(detecting)

# # Start new Threads
threadInit.start()
# sio.run()
threadSender.start()
# # sio.run()

# detecting()