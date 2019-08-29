from imageai.Detection import VideoObjectDetection
import os
import threading

import eventlet
import socketio

from vid_cap import VideoCap


# url = 'redis://hostname:port/0'
# sio = socketio.Server(client_manager=socketio.RedisManager(url))

eventlet.sleep()
eventlet.monkey_patch()

# sio = socketio.Server(ping_timeout=10, binary=True)

sio = socketio.Server(async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
# sio = SocketIO(app, async_mode='threading')


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
    print("Detecting frame: "+ str(frame_number))
    sio.emit('reply', returned_frame, namespace='/chat')
    eventlet.sleep(5)

def detecting():
    video_path = video_detector.detectObjectsFromVideo(camera_input=camera, save_detected_video = False,
        frames_per_second=20, log_progress=True, minimum_percentage_probability=30, per_frame_function=forFrame,
        return_detected_frame=True)

def init_socket():
    print("Starting socket...")
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
    # app.run(threaded=True)
    # sio.run(app, '', 8080, debug=True)

def sender():
    print("Starting detection")
    # eventlet.monkey_patch()
    # sio.start_background_task(detecting)
    sio.start_background_task(target=detecting, app=app)

video_detector = VideoObjectDetection()
video_detector.setModelTypeAsRetinaNet()
video_detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1_4.h5"))
# video_detector.setModelPath(os.path.join(execution_path, "v2.h5"))
video_detector.loadModel()

vidcap = VideoCap()
camera = vidcap.camera()

# init_socket()
# sender()

# Create new threads
threadInit = myThread(1)
threadSender = myThread(2)

# # sio.start_background_task(detecting)

# # # Start new Threads
threadInit.start()
# # sio.run()
threadSender.start()
# sio.run()

# detecting()
