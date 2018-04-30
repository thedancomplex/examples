import matplotlib.pyplot as plt
import numpy
import time
import socket
import numpy as np
import matplotlib.animation as animation

UDP_IP   = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.01)



#Send
UDP_IP2 = "127.0.0.1"
UDP_PORT2 = 5006
MESSAGE = "0.0"

print "UDP target IP:", UDP_IP2
print "UDP target port:", UDP_PORT2
print "message:", MESSAGE

sock2 = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP






t00 = time.time()
t0 = time.time()
t1 = time.time()
i = 0.0
d_theta = 0.0
theta = 0.0
vin = 0.1

def f(t):
            return np.exp(-t) * np.cos(2*np.pi*t)

tt1 = np.arange(0.0, 5.0, 0.1)
tt2 = np.arange(0.0, 5.0, 0.02)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def getMotor(vin):
    global t0, t1, i, d_theta, theta
    b = 0.1
    J = 0.01
    K = 0.01
    L = 0.5
    R = 1
    t1 = time.time()
    dt = t1 - t0
    dd_theta = -b/J * d_theta +  K/J * i + 0.0 * vin
    d_i      = -K/L * d_theta + -R/L * i + 1/L * vin

    imax = 20.0
    d_theta_max = 100.0
    if(i > imax):
        i = imax
    if(i < -imax):
        i = -imax
    if(d_theta > d_theta_max):
        d_theta = d_theta_max
    if(d_theta < -d_theta_max):
        d_theta = - d_theta_max

    i = d_i * dt + i
    d_theta = dd_theta * dt + d_theta
    theta = theta + d_theta * dt
    return theta

i_udp_max = 300
xar = np.zeros(i_udp_max)
yar = np.zeros(i_udp_max)
i_udp = 0
FLAG_INI = False

def getUDP(i):
    global FLAG_INI, vin, t1, t0, t00, i_udp_max, xar, yar, i_udp, ax1
    try:
      s_vin, addr = sock.recvfrom(1024)
      vin = float(s_vin)
    except:
        vin = vin
    t1 = time.time()
    theta_out = getMotor(vin)
    t0 = t1
    xar[i_udp] = t1 - t00
    yar[i_udp] = theta_out
#    if(FLAG_INI == False):
#        for ii in range(i_udp,i_udp_max):
#            xar[ii] = xar[i_udp]
#            yar[ii] = yar[i_udp]
    if(i_udp < i_udp_max):
        i_udp = i_udp + 1
    if(i_udp >= i_udp_max):
        i_udp = 0
        FLAG_INT = True
    sock2.sendto(str(theta_out), (UDP_IP2, UDP_PORT2))
    ax1.clear()
    ax1.scatter(xar,yar)
    #ax1.scatter(xar,yar)
    #print "vin = " + str(vin) + " theta out = " + str(theta_out)

def init():
  ani = animation.FuncAnimation(fig, getUDP,frames=1000, interval=1)
  plt.show()


init()
