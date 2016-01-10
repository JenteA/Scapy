#!/usr/bin/python
from scapy.all import *

def ping(ip, delay, nr):
  TIMEOUT = 2
  rep=[]
  conf.verb = 0
  packet = IP(dst=ip, ttl=20)/ICMP()
  ans, unans = srloop(packet, timeout=TIMEOUT, count=nr, inter=delay)
  for num in range(nr):
      reply = packet[IP].dst, "packet is send"	
      rep.append(reply)
  return rep