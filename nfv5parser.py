#!/usr/bin/python
import sys
import socket
import struct
from unpacker import Unpacker
"""
BYTES	CONTENTS	DESCRIPTION
0-3		srcaddr	Source IP address
4-7		dstaddr	Destination IP address
8-11	nexthop	IP address of next hop router
12-13	input	SNMP index of input interface
14-15	output	SNMP index of output interface
16-19	dPkts	Packets in the flow
20-23	dOctets	Total number of Layer 3 bytes in the packets of the flow
24-27	first	SysUptime at start of flow
28-31	last	SysUptime at the time the last packet of the flow was received
32-33	srcport	TCP/UDP source port number or equivalent
34-35	dstport	TCP/UDP destination port number or equivalent
36		pad1	Unused (zero) bytes
37		tcp_flags	Cumulative OR of TCP flags
38		prot	IP protocol type (for example, TCP = 6; UDP = 17)
39		tos	IP type of service (ToS)
40-41	src_as	Autonomous system number of the source, either origin or peer
42-43	dst_as	Autonomous system number of the destination, either origin or peer
44		src_mask	Source address prefix mask bits
45		dst_mask	Destination address prefix mask bits
46-47	pad2	Unused (zero) bytes

"""


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.bind(('127.0.0.1', 2055))
unpck = Unpacker.Unpacker()
while True:
    try:
        print('listening..')
        (packetbuf, addr) = sock.recvfrom(65535)
        version = unpck.unpackbufferint(packetbuf, 0, 2)
        print(str(version))
        # totalrecord = unpck.unpackbufferint(packetbuf, 2, 2)
        # # as per the Netflow version 5 Standard..
        # if totalrecord < 1 or totalrecord > 30:
        #     raise Exception("Invalid Record Count!!!")
        # print "Netflow Version: %i" % version
        # print "Total number of records: %i" % totalrecord

        # for recordcounter in range(0, totalrecord):
        #     # Adjusts the pointer to the appropriate record after the header .. header size  = 24, record size = 48
        #     recordpointer = 24 + (recordcounter * 48)
        #     print "==================\n"
        #     print "Record: %i" % recordcounter
        #     srcaddr = socket.inet_ntoa(
        #         packetbuf[recordpointer:recordpointer + 4])
        #     print "Source address: %s" % srcaddr
        #     dstaddr = socket.inet_ntoa(
        #         packetbuf[recordpointer + 4:recordpointer + 8])
        #     print "Destination address: %s" % dstaddr
        #     nxthp = socket.inet_ntoa(
        #         packetbuf[recordpointer + 8:recordpointer + 12])
        #     print "nexthop: %s" % nxthp
        #     # pointer has been adjusted to read the appropriate field in the netflow record
        #     dPkts = unpck.unpackbufferint(packetbuf, recordpointer + 16, 4)
        #     print "Total packets: %i" % dPkts
        #     dOctets = unpck.unpackbufferint(packetbuf, recordpointer + 20, 4)
        #     print "Total Bytes: %i" % dOctets
        #     startflow = unpck.unpackbufferint(packetbuf, recordpointer + 24, 4)
        #     endflow = unpck.unpackbufferint(packetbuf, recordpointer + 28, 4)
        #     print "Starttime in miliseconds: %i" % startflow
        #     print "endtime in miliseconds %i" % endflow
        #     srcport = unpck.unpackbufferint(packetbuf, recordpointer + 32, 2)
        #     dstport = unpck.unpackbufferint(packetbuf, recordpointer + 34, 2)
        #     print "Source Port: %i" % srcport
        #     print "Destination Port: %i" % dstport
        #     l4protocol = unpck.unpackbufferint(
        #         packetbuf, recordpointer + 38, 1)
        #     if l4protocol == 6:
        #         l4proto = 'TCP'

        #     elif l4protocol == 17:
        #         l4proto = 'UDP'

        #     else:
        #         l4proto = 'Other'
        #     print "L4 protocol: %s" % l4proto
        #     print "==================="
    except Exception as e:
        print(e)
        break
