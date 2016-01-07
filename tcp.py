#!/usr/bin/python
from time import sleep
from scapy.all import *
def tcpping(ip, port, delay = 1, nr = 1):
  TIMEOUT = 2
  conf.verb = 0
  for num in range(0, nr):
      packet = IP(dst=ip, ttl=20)/TCP(dport=port)
      reply = sr1(packet, timeout=TIMEOUT)
      if not (reply is None):
         return reply.src, "is online"
      else:
         return "Timeout waiting for %s" % packet[IP].dst
      sleep(delay)