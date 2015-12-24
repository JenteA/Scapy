#!/usr/bin/python
from scapy.all import *
def arp(ip):
  TIMEOUT = 2
  conf.verb = 0
  #ip = "192.168.1.222"
  #for ip in range(140, 256):
  packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
  reply = sr1(packet, timeout=TIMEOUT)
  if not (reply is None):
       return reply.src, "is online"
  else:
       return "Timeout waiting for %s" % packet[IP].dst