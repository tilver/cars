#!/usr/bin/python

from scapy.layers.can import *
from scapy.contrib.automotive.uds import *
from scapy.contrib.isotp import *
#from scapy.contrib.cansocket import *

#socket = CANSocket(channel='vcan0')
conf.contribs['ISOTP'] = {'use-can-isotp-kernel-module': True}
sock = ISOTPNativeSocket(iface="vcan0", tx_id=0x7E0, rx_id=0x7e8, basecls=UDS)

uds_request = UDS()/UDS_ER(resetType=0x1)
sock.sr1(uds_request,verbose=False)

uds_request = UDS()/UDS_TP()
ans = sock.sr1(uds_request,verbose=False,timeout=5)
if ans:
    ans.show()
else:
    print("No Answer")
  
uds_request = UDS()/UDS_RDBI(identifiers=[0x1000])
ans = sock.sr1(uds_request,verbose=False)
if ans:
    ans.show()
else:
    print("No Answer")

uds_request = UDS()/UDS_RDBI(identifiers=[0x1001])
ans = sock.sr1(uds_request,verbose=False)
if ans:
    ans.show()
else:
    print("No Answer")
