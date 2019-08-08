from aiohttp import web
import socketio
import time

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
# @sio.on('python-message')
# async def print_message(sid, message):
#     # When we receive a new event of type
#     # 'message' through a socket.io connection
#     # we print the socket ID and the message
#     print("Socket ID: " , sid)
#     print('fayeeeeeeeeeeeeeeeeeeeeeeeeee')
#     print(message)
#     # sio.emit('python-message', 'aku python') # gpp

# @sio.on('connection')
# async def print_message():
#     # When we receive a new event of type
#     # 'message' through a socket.io connection
#     # we print the socket ID and the message
#     print("Sending...")
#     await sio.emit('python-message', 'aku python') # gpp






# @sio.on('python-message')
# async def print_message():
#     # When we receive a new event of type
#     # 'message' through a socket.io connection
#     # we print the socket ID and the message
#     # print("Socket ID: " , sid)
#     # print('fayeeeeeeeeeeeeeeeeeeeeeeeeee')
#     # print(message)
#     sio.emit('python-message', 'aku python') # gpp



# def send_message():
#     print("Masuk send_message")
#     sio.emit('python-message', 'aku python') # gpp


#BERHASIL
# @sio.on('chat message', namespace='/chat')
# async def print_message(sid, data):
#     # print("server received message!", data)
#     await sio.emit('reply', 'aku python', namespace='/chat')

# @sio.on('chat message', namespace='/chat')
async def send_message():
    print("Masuk send_message")
    # print("server received message!", data)
    await sio.emit('reply', 'aku python', namespace='/chat')
    time.sleep(5)

def repeat_message():
    while True:
        print("Masuk repeat_message")
        send_message()
        time.sleep(5)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)
    # print_message()
    repeat_message()