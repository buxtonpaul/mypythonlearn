# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:55:45 2017

@author: paulb
"""

import socket
import sys
import struct
import array
import binascii

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.0.34', 5987)
message = array.array('B', [0x20 ,0x00 ,0x00 ,0x00 ,0x16 ,0x02 ,0x62 ,0x3A ,0xD5, 0xED, 0xA3, 
           0x01, 0xAE, 0x08, 0x2D, 0x46, 0x61, 0x41, 0xA7, 0xF6, 0xDC, 0xAF, 0xD3, 0xE6, 0x00, 0x00, 0x1E])



commands={'on':[0x31,0x00,0x00,0x08,0x04,0x01,0x00,0x00,0x00],
          'off':[0x31,0x00,0x00,0x08,0x04,0x02,0x00,0x00,0x00],
          'nighton':[0x31,0x00,0x00,0x08,0x04,0x05,0x00,0x00,0x00],
          'whighton':[0x31,0x00,0x00,0x08,0x05,0x64,0x00,0x00,0x00],

          }

def getCommandPacketRGBW(sess1,sess2,command,zone,value=100,seq=0):
    # lets produce a packet based on these
    header=[0x80,00,00,00,11,sess1,sess2,0x00,seq]
    output = commands[command]+header
    print output
    
try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = sock.recvfrom(5987)
    print >>sys.stderr, 'received "%s"' % binascii.hexlify(data)

    MAC = binascii.hexlify(data[7:13])
    print>>sys.stderr, MAC
    
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()