import socketio

sio = socketio.Client()
sio.connect('ws://192.168.50.200:7777')

@sio.on('snack_list')
def snack(data):
    print('snack', data)

@sio.on('response')
def response(data):
    print('response', data) 
