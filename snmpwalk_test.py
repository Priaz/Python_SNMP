#!/usr/bin/env python
# -*- coding: utf-8 -*-


import netsnmp
import subprocess
from DataSnmp import DataSnmp


oid_snmp_description_int ='.1.3.6.1.2.1.17.7.1.2.2.1.2'
#oid_snmp_description_int ='.1.3.6.1.2.1.2.2.1.2.1'

#адреса стэков, выбор
address = '192.168.99.1'
COMMUNITY = 'public'

#удаляем последний символ с oid для перебора
snmp_description = oid_snmp_description_int[0:-1]


"""SNMP запросы 
в чистом виде 
без вводных данных
"""
#vivod opisaniya interfeisa
#print ('Port Name:',snmp_description +i)
#result_description_int = str (netsnmp.snmpget(snmp_description +i, Version = 2, DestHost=address, Community=COMMUNITY)[0])
#print ('Port Name:',result_description_int)


#proc = subprocess.Popen("ping -c2 %s" % address, shell=True, stdout=subprocess.PIPE)
#out = proc.stdout.readlines()
#daem comandu snmpwalk
snmp_mac_address_table = subprocess.Popen("snmpwalk -v2c -c public 192.168.99.1 .1.3.6.1.2.1.17.7.1.2.2.1.2", shell=True, stdout=subprocess.PIPE)
out_snmp_mac_address = snmp_mac_address_table.stdout.readlines()
print (out_snmp_mac_address[0])

#vivod mac_adress za portom
dic = {}
for dt in out_snmp_mac_address:
    test = DataSnmp (dt)
    dic[str(test.port)]=test.mac
    test.testring()

print (dic)
print(dic['2'])
