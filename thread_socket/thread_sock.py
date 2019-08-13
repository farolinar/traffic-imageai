import threading
import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

class myThread (threading.Thread):
    def __init__(self, category):
        threading.Thread.__init__(self)
        self.category = category
        if self.category == 1:
            self.name = "InitSocket"
        elif self.category == 2:
            self.name = "Sender"
        else:
            print("Wrong thread category")

    def run(self):
        print("Starting " + self.name)
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

def init_socket():
    print("Starting socket...")
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)

def sender():
    # for sending image
    image_data = 'No image'
    with open('my_image_file.jpg', 'rb') as f:
        print('Image exist')
        image_data = f.read()
    print(type(image_data))
    while True:
        sio.emit('reply', image_data, namespace='/chat')
        # sio.emit('reply', 'aku python', namespace='/chat')

# threadLock = threading.Lock()
# threads = []

# Create new threads
threadInit = myThread(1)
threadSender = myThread(2)

# Start new Threads
threadInit.start()
threadSender.start()

# # Add threads to thread list
# threads.append(threadInit)
# threads.append(threadSender)

# # Wait for all threads to complete
# for t in threads:
#     t.join()
print("Exiting Main Thread")