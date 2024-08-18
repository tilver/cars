#!/usr/bin/python

from scapy.layers.can import *
from scapy.contrib.automotive.uds import *
from scapy.contrib.isotp import *
#from scapy.contrib.cansocket import *

#socket = CANSocket(channel='vcan0')
conf.contribs['ISOTP'] = {'use-can-isotp-kernel-module': True}
sock = ISOTPNativeSocket(iface="vcan0", tx_id=0x610, rx_id=0x6f1, ext_address=0x10, rx_ext_address=0xf1, basecls=UDS)

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
