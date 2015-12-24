#!/usr/bin/python
from scapy.all import *

def ping(ip):

  TIMEOUT = 2
  conf.verb = 0
  #ip = "192.168.1.125"
  #for ip in range(140, 256):
  packet = IP(dst=ip, ttl=20)/ICMP()
  reply = sr1(packet, timeout=TIMEOUT)
  if not (reply is None):
  	return reply.src, "is online"
  else:
  	return "Timeout waiting for %s" % packet[IP].dst

