#!/usr/bin/env lua5.2
--
-- apt install lua5.2 lua-socket
--
local socket = require("socket")

udp = socket.udp()
udp:setsockname("*", 5005)
udp:settimeout(0)

while true do
    data, ip, port = udp:receivefrom()
    if data then
        print("Received: ", data, ip, port)
        udp:sendto(data, ip, port)
    end
    socket.sleep(0.01)
end
