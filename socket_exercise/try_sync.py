import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.on('chat message', namespace='/chat')
def print_message(sid, data):
    # print("server received message!", data)
    sio.emit('reply', 'aku python', namespace='/chat')

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)