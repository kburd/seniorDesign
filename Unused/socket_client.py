import socket, time

image = open('my_image.jpg', 'rb')
image_data = image.read()
image.close()

ADDRESS = '128.4.143.206'
PORT = 8080
socketData = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketData.connect((ADDRESS,PORT))
start = time.time()
socketData.sendall(image_data)
end = time.time()
print('time elapsed',start-end)
