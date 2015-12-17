#!/usr/bin/python
from scapy.all import *

def ping();
  TIMEOUT = 2
  conf.verb = 0
  ip = "192.168.1.125"
  #for ip in range(140, 256):
  	packet = IP(dst=ip, ttl=20)/ICMP()
	reply = sr1(packet, timeout=TIMEOUT)
	if not (reply is None):
     		print reply.src, "is online"
	else:
     		print "Timeout waiting for %s" % packet[IP].dst
return;

ping
