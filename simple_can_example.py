#!/usr/bin/python

from scapy.layers.can import *
from scapy.contrib.cansocket import *


socket = CANSocket(channel='vcan0')
packet = CAN(identifier=0x123, data=b'01020304')

socket.send(packet)
rx_packet = socket.recv()

socket.sr1(packet, timeout=1)
