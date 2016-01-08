#!/usr/bin/python
from scapy.all import *
def arp(ip, delay, nr):
  TIMEOUT = 2
  conf.verb = 0
  rep=[]
  packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
  ans, unans = srploop(packet, timeout=TIMEOUT, iface="eth0", count=nr, inter=delay)
  for num in range(nr):
      reply = packet[ARP].pdst, "is send"
      rep.append(reply)   
  return rep
