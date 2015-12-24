#!/usr/bin/python
from scapy.all import *
def tcpping(ip, port):
  TIMEOUT = 2
  conf.verb = 0
  #port=23
  #ip = "192.168.1.222"
  #for ip in range(140, 256):
  packet = IP(dst=ip, ttl=20)/TCP(dport=port)
  reply = sr1(packet, timeout=TIMEOUT)
  if not (reply is None):
       return reply.src, "is listening to", port
  else:
       return "Timeout waiting for %s" % packet[IP].dst
