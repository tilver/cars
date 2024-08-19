#!/usr/bin/python
from scapy.all import *
from scapy.layers.can import *                                                              
from scapy.contrib.cansocket import *
                                              
import time
                                              
# Function to send UDS DiagnosticSessionControl request to a specific CAN ID

def make_uds_request(can_id):
    # UDS request for DiagnosticSessionControl (SID 0x10)
    uds_request = Raw(b'\x02\x10\x01')  # 02 = Length, 10 = SID, 01 = Default Session
    can_frame = CAN(identifier=can_id, data=uds_request.load)
    
    # Return CAN frame
    return can_frame    

# Function to scan for UDS enabled devices
def scan_uds_devices(start_id=0x7E0, end_id=0x7EF):
    print(f"Scanning CAN IDs from {hex(start_id)} to {hex(end_id)} for UDS services...")
    
    uds_enabled_devices = []

    sock = CANSocket(channel='vcan0')
    
    for can_id in range(start_id, end_id + 1):
        # Send UDS request
        packet = make_uds_request(can_id)
        response = sock.sr1(packet, timeout=1)
        response.show()
        
        if response:
            print(f"UDS service found on CAN ID: {hex(can_id)}")
            uds_enabled_devices.append(hex(can_id))
        else:
            print(f"No response from CAN ID: {hex(can_id)}")
        
        time.sleep(0.1)  # Small delay between requests
    
    if uds_enabled_devices:
        print("UDS enabled devices found on the following CAN IDs:")
        for device in uds_enabled_devices:
            print(device)
    else:
        print("No UDS enabled devices found.")
    
    return uds_enabled_devices

# Start the scan
uds_devices = scan_uds_devices()
