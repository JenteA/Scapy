#!/usr/bin/python
from scapy.all import *

TIMEOUT = 2
conf.verb = 0
for ip in range(140, 256):
    packet = IP(dst="172.16.219." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print reply.dst, "is online"
    else:
         print "Timeout waiting for %s" % packet[IP].dst