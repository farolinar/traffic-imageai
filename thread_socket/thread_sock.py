import threading
import eventlet
import socketio
import random

import os
import sys
import time

from datetime import datetime

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

class myThread (threading.Thread):
    def __init__(self, category):
        threading.Thread.__init__(self)
        self.category = category
        self._is_running = True
        if self.category == 1:
            self.name = "InitSocket"
        elif self.category == 2:
            self.name = "Sender"
        else:
            print("Wrong thread category")

    def run(self):
        # while(self._is_running):
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

    def stop(self):
        self._is_running = False



def init_socket():
    print("Starting socket...")
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)

def sender():
    # for sending image
    image_data = 'No image'
    images = []
    
    for filename in os.listdir('.'):
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            with open(filename, 'rb') as f:
                print('Image exists')
                image_data = f.read()
                images.append(image_data)
    print(type(image_data))

    while True:
        # image_data = random.choice(list(enumerate(images)))
        # print('Sending image ' + str(image_data[0]))
        image_data = random.choice(images)
        # time.sleep(10)
        sio.emit('reply', image_data, namespace='/chat')
        print('Image sent')
        # eventlet.sleep(5)
        # time.sleep(1)
        # sio.sleep(5)
        # sio.emit('reply', 'aku python', namespace='/chat')

# threadLock = threading.Lock()
# threads = []

# Create new threads
threadInit = myThread(1)
threadSender = myThread(2)

# def exitfunc():
#     threadInit.stop()
#     threadSender.stop()
#     print("Exit Time ", datetime.now())
#     print("Exiting Main Thread")
#     # sys.exit(0)

# threading.Timer(300, exitfunc).start() # exit in 5 minutes

# Start new Threads
threadInit.start()
threadSender.start()

# # Add threads to thread list
# threads.append(threadInit)
# threads.append(threadSender)

# # Wait for all threads to complete
# for t in threads:
#     t.join()
