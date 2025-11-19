#echo server py
import socket
# this is the module of socket. which is provides low-level networking interfaces
#for tcp\ip communication


HOST = "127.0.0.1"
# this is the loopback address meaning the server will only accept
#connections from the same machine

PORT = 65432
#this is the port number the server listens on. you can choose any unused port
#above 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET means ipv4
    #SOCK STEAM means tcp reliable connection based
    # with ensures the socket is automatically closed when done
    s.bind((HOST, PORT))
    #binds the socket to the specified IP and port so it can listen for incoming
    #connections
    s.listen()
    #starts listening for incoming connections. By deefault it allows one connection in the
    #queue. you can pass a number like s.listen to allow more
    conn, addr = s.accept()
    #accepts a connection from a client
    # conn is a new socket object used to communicate with the client
    #addr is the client's address (IP and port)

    with conn:
        print(f"Connected by: {addr}")
        #pritns the clients address to confirm a successfull connection
        while True:
            # starts an infinite loop to keep receiving and
            # echoing data until the client disconnect
            data = conn.recv(1024)
            # this receives up to 1024 bytes of data from the client
            # if the client sends nothing data will be empty
            if not data:
                #breaks data if no data is received meaning the client disconnected
                break
            conn.sendall(data)
            #sends the received data back to the client this is the "echo" part