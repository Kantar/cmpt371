#import socket module
from socket import * 

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
# Create a socket object
mySocket = socket(AF_INET, SOCK_STREAM) 

# Create a port for the socket
# Random port number to avoid having a conflict with other default ports 
myPort = 9999

# Hide myPort from the public
# Using '' is good for any addresses 
mySocket.bind(('',myPort))

# Start socket listening with only 1 connect request as required in the question
mySocket.listen(1)

while True:
  #Establish the connection
  print 'Ready to serve...'
  connectionSocket, addr = mySocket.accept() 
 
  try:
    # Get the request from a client
    message = connectionSocket.recv(1024)  
    filename = message.split()[1] 
    f = open(filename[1:]) 
    # Use the function to read the data by calling the object f
    outputdata = f.read() 
    # Send one HTTP header line into socket
    # Since it is tcp, we use http 1.1 here
    connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n") 
    # Send the content of the requested file to the client
    for i in range(0, len(outputdata)): 
      connectionSocket.send(outputdata[i])
    connectionSocket.close()
  except IOError:
    # Send response message for file not found
    connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n")
    # To satisfy (vi) requirement
    connectionSocket.send("<html><head></head><body><h1>404 NOT FOUND</h1></body></html>\r\n")
    # Close client socket
    connectionSocket.close()

serverSocket.close()
