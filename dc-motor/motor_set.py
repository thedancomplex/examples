import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "0.0"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


#Server
UDP_IP2   = "127.0.0.1"
UDP_PORT2 = 5006

sock2 = socket.socket(socket.AF_INET, # Internet
                                     socket.SOCK_DGRAM) # UDP
sock2.bind((UDP_IP2, UDP_PORT2))
sock2.settimeout(0.2)

vout = 0.0

def get():
  global vout
  return vout
def set(v):
    global vout
    sock.sendto(str(v), (UDP_IP, UDP_PORT))
    try:
      s_vout, addr = sock2.recvfrom(1024)
      vout = float(s_vout)
    except:
      vout = vout
