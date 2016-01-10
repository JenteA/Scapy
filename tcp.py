#!/usr/bin/python
from scapy.all import *
def tcpping(ip, port, delay, nr):
  TIMEOUT = 2
  rep=[]
  conf.verb = 0
  for num in range(nr):
      packet = IP(dst=ip, ttl=20)/TCP(dport=port)
      ans, unans = srloop(packet, timeout=TIMEOUT, count=nr, inter=delay)
      for num in range(nr):
         reply = packet[IP].dst, "is send"
         rep.append(reply)
      return rep
