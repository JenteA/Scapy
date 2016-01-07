#!/usr/bin/python
from time import sleep
from scapy.all import *
def tcpping(ip, port, delay = 1, nr = 1):
  TIMEOUT = 2
  conf.verb = 0
<<<<<<< HEAD
  for num in range(0, nr):
      packet = IP(dst=ip, ttl=20)/TCP(dport=port)
      reply = sr1(packet, timeout=TIMEOUT)
      if not (reply is None):
         return reply.src, "is online"
      else:
         return "Timeout waiting for %s" % packet[IP].dst
      sleep(delay)
=======
  #port=23
  #ip = "192.168.1.222"
  #for ip in range(140, 256):
  packet = IP(dst=ip, ttl=20)/TCP(dport=port)
  reply = sr1(packet, timeout=TIMEOUT)
  if not (reply is None):
       return reply.src, "is listening to", port
  else:
       return "Timeout waiting for %s" % packet[IP].dst
>>>>>>> ea719aa6fca7627e6898794e9ad151b6b87da866
