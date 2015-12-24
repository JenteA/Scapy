#!/usr/bin/python
from scapy.all import *
def arp(ip):
  TIMEOUT = 2
  conf.verb = 0
  #ip = "192.168.1.222"
  #for ip in range(140, 256):
  packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
  reply, unreply = srp(packet, timeout=TIMEOUT, iface="eth0")
  if len(reply) > 0:
       return reply[0][0].getlayer(ARP).pdst, "is online"
  else:
       return "Timeout waiting for %s" % packet[ARP].pdst
