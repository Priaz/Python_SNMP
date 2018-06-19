#!/usr/bin/env python
# -*- coding: utf-8 -*-


import netsnmp
import subprocess
from utils import getport
from sys import stdin
from DataSnmp import DataSnmp
import os, sys

oid_snmp_description_int ='.1.3.6.1.2.1.31.1.1.1.1.1'
#oid_snmp_description_int ='.1.3.6.1.2.1.2.2.1.2.1'
oid_snmp_status_int='.1.3.6.1.2.1.2.2.1.8.1'
oid_snmp_speed_int ='.1.3.6.1.2.1.2.2.1.5.1'
#oid_snmp_mac_int ='.1.3.6.1.2.1.2.2.1.6.1'
oid_snmp_mac_int ='.1.3.6.1.2.1.17.7.1.2.2.1.2'
oid_snmp_arp_ip ='1.3.6.1.2.1.4.22.1.2'
COMMUNITY = 'public'


#адреса стэков, выбор
address_stack_1 = '192.168.99.1'
address_stack_2 = '192.168.99.2'

#удаляем последний символ с oid для перебора
snmp_description = oid_snmp_description_int[0:-1]
snmp_status = oid_snmp_status_int[0:-1]
snmp_speed = oid_snmp_speed_int[0:-1]
snmp_mac = oid_snmp_mac_int[0:-1]

# vibor stack
#print ('Vvedite nomer STACK:')
#s=str(input());
debug = True

if debug:
    s = "1"
    if s == '1':
        address=address_stack_1
    else:
        address=address_stack_2

    # vibor  porta
    #print ('Vvedite port:')
    eth = "1/0/2"

    eth=str(eth)
    i=getport(eth)
    i=str(i)
else:
    print ('Vvedite nomer STACK:')
    s=str(input());
    if s == '1':
        address=address_stack_1
    else:
        address=address_stack_2

    # vibor  porta
    print ('Vvedite port:')

    eth=str(raw_input())
    i=getport(eth)
    i=str(i)


"""SNMP запросы 
в чистом виде 
без вводных данных
"""
#vivod opisaniya interfeisa
#result_description_int = str (netsnmp.snmpget(oid_snmp_description_int, Version = 2, DestHost=address, Community=COMMUNITY)[0])
#print ('Port Name:',result_description_int)

#vivod statusa interfeisa
#result_status_int = str (netsnmp.snmpget(oid_snmp_status_int, Version = 2, DestHost=address, Community=COMMUNITY)[0])
#if result_status_int == 1:
#    print (result_description_int, 'UP')
#else:
#    print (result_description_int, 'DOWN')

#vivod speed interfeis
#result_speed_int = str (netsnmp.snmpget(oid_snmp_speed_int, Version = 2, DestHost=address, Community=COMMUNITY)[0])

#if result_speed_int == '1000000000':
#    print('Port Speed: 1 Gb/s')
#elif result_speed_int == '100000000':
#    print ('Port Speed: 100 Mb/s')
#elif result_speed_int == '10000000':
#    print ('Port Speed: 10 Mb/s')
#else:
#    print('Port Speed: 0 Mb/s')

#vivod mac-address interfeis
#result_mac_int = str (netsnmp.snmpget(oid_snmp_mac_int, Version = 2, DestHost=address, Community=COMMUNITY)[0])
'''
#выводится строка в виде кода символов
#print (result_mac_int)
#выводим строку в виде символов
print("%r" % result_mac_int) 
#ord берет строчку (в данном случае 1 символ) и возвращает ее код (число),%02x означает "распечатать как hex, если меньше 2 знаков, то добить нулями спереди
for symvol in result_mac_int:
    print("%02x" % ord(symvol))
#объединяем вывод через "-"
print("-".join("%02x" % ord(symvol) for symvol in result_mac_int))
'''
#преобразование и вывод в привычном виде MAC.
#print('MAC - Address interface:', "-".join("%02x" % ord(symvol) for symvol in result_mac_int))


"""SNMP запросы с
вводными данными
"""

#vivod opisaniya interfeisa po vvodu peremennoy s
result_snmp_description_int = str (netsnmp.snmpget(snmp_description +i, Version = 2, DestHost=address, Community=COMMUNITY)[0])
if result_snmp_description_int == '':
    print 'No that port'
    sys.exit(0)
print 'Port Name : ', str.upper(result_snmp_description_int)
#print('Port Name:', 'eth'+eth)

#vivod statusa interfeisa
result_snmp_status_int = str (netsnmp.snmpget(snmp_status +i, Version = 2, DestHost=address, Community=COMMUNITY)[0])
if int(result_snmp_status_int) == 1:
    print 'eth'+eth+ " : ", 'UP'
else:
    print 'eth'+eth+ " : " , 'DOWN'


#vivod speed interfeis
result_snmp_speed_int = str (netsnmp.snmpget(snmp_speed +i, Version = 2, DestHost=address, Community=COMMUNITY)[0])

if result_snmp_speed_int == '1000000000':
    print('Port Speed:  1 Gb/s')
elif result_snmp_speed_int == '100000000':
    print ('Port Speed:  100 Mb/s')
elif result_snmp_speed_int == '10000000':
    print ('Port Speed:  10 Mb/s')
else:
    print('Port Speed:  0 Mb/s')

#vivod mac-address interfeis
result_snmp_mac_int = str (netsnmp.snmpget(snmp_mac +i, Version = 2, DestHost=address, Community=COMMUNITY)[0])
#преобразование и вывод в привычном виде MAC.
#print('MAC - Address interface:', "-".join("%02x" % ord(symvol) for symvol in result_snmp_mac_int))

#vivod mac_adress za portom v vide tablici
snmp_mac_address_table = subprocess.Popen("snmpwalk -v2c -c public " +address +" "+ oid_snmp_mac_int, shell=True, stdout=subprocess.PIPE)
out_snmp_mac_address = snmp_mac_address_table.stdout.readlines()
#print ('erfswfewfrewfew', out_snmp_mac_address[0])

#slovar mac-address table
dic_mac = {}
for mac_dt in out_snmp_mac_address:
    element = DataSnmp (mac_dt)
    dic_mac[str(element.port)]=element
    #test.testring()

print "Mac_addr  : ", str.upper(dic_mac[i].mac)

#vivod ARP tablici
snmp_ip_address_table = subprocess.Popen("snmpwalk -v2c -c public " +address +" "+ oid_snmp_arp_ip, shell=True, stdout=subprocess.PIPE)
out_snmp_ip_address_table = snmp_ip_address_table.stdout.readlines()

for ip_dt in out_snmp_ip_address_table:
    mac = ip_dt.split('= STRING: ')[1]
    mac = mac.split('\n')[0]
    
    ip = ip_dt.split('ipNetToMediaPhysAddress.')[1]
    ip = ip.split('= STRING: ')[0]
    ip = ip.split('.')    
    ip = ip[1] + '.' + ip[2] + '.' + ip[3] + '.' + ip[4] 
    element = None

    for key in dic_mac:
        el = dic_mac [key]
        if el.mac == mac:
            element = el 
            break
    if element != None:
        element.ip = ip

print "IP_addr  : ", str.upper(dic_mac[i].ip)