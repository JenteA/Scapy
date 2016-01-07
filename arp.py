#!/usr/bin/python
from time import sleep
from scapy.all import *
def arp(ip, delay, nr):
  TIMEOUT = 2
  conf.verb = 0
  for num in range(0, nr):
      packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
      reply = sr1(packet, timeout=TIMEOUT)
      if not (reply is None):
         return reply.src, "is online"
      else:
         return "Timeout waiting for %s" % packet[IP].dst
      sleep(delay)
