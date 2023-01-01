#!/usr/bin/evn python

import scapy.all as scapy
#import pprint

def scan(ip):
  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_request_broadcast = broadcast/arp_request
  answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
  print("IP\t\t\tMAC Address\n-----------------------------------")
  clients_list = []
  for element in answered_list:
    client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
    clien_list.append(client_dict)
    #print(element[1].show())
    print(element[1].psrc + "\t\t" + element[1].hwsrc)
  print(clien_list)      
    #print(element[1].hwsrc)
    #print("--------------------------------------------------------")
  #answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
  #print(answered_list.summary())
  #print(unanswered.summary())
  

scan("10.0.2.0/24")