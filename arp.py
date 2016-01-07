#!/usr/bin/python
from time import sleep
from scapy.all import *
def arp(ip, delay = 1, nr = 1):
  TIMEOUT = 2
  conf.verb = 0
<<<<<<< HEAD
  for num in range(0, nr):
      packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
      reply = sr1(packet, timeout=TIMEOUT)
      if not (reply is None):
         return reply.src, "is online"
      else:
         return "Timeout waiting for %s" % packet[IP].dst
      sleep(delay)
=======
  #ip = "192.168.1.222"
  #for ip in range(140, 256):
  packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
  reply, unreply = srp(packet, timeout=TIMEOUT, iface="eth0")
  if len(reply) > 0:
       return reply[0][0].getlayer(ARP).pdst, "is online"
  else:
       return "Timeout waiting for %s" % packet[ARP].pdst
>>>>>>> ea719aa6fca7627e6898794e9ad151b6b87da866
