#!/usr/bin/python
from time import sleep
from scapy.all import *
def tcpping(ip, port, delay, nr):
  TIMEOUT = 2
  rep=[]
  conf.verb = 0
  for num in range(nr):
      packet = IP(dst=ip, ttl=20)/TCP(dport=port)
      reply = sr1(packet, timeout=TIMEOUT)
      if not (reply is None):
         rep[num-1] reply.src, "is online"
      else:
         rep[num-1] "Timeout waiting for %s" % packet[IP].dst
      sleep(delay)
      return rep
