#!/usr/bin/python
from time import sleep
from scapy.all import *
def arp(ip, delay, nr):
  TIMEOUT = 2
  conf.verb = 0
  rep=''
  for num in range(0, nr):
       packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
       reply, unreply = srp(packet, timeout=TIMEOUT, iface="eth0")
       if len(reply) > 0:
          rep[num] reply[0][0].getlayer(ARP).pdst, "is online"
       else:
          rep[num] "Timeout waiting for %s" % packet[ARP].pdst
  sleep(delay) 
  return rep