#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DataSnmp(object):
    def __init__(self, data_snmp):
        self.data_snmp = data_snmp
        self.port = 0
        self.mac_hex = '12.34.56.78.90.12'
        self.mac = '00.00.00.00.00.00'
        self.ip = 'No_Ip'
        self.parse()
    def testring(self):   
        print (self.data_snmp)
        print (self.port)
        print (self.mac_hex)
        print (self.mac)
        print (self.ip)
    def int_to_hex(self, int_str):
        #print (int_str)
        s0 = (hex(int(int_str)).split('x')[1])
        if len(s0)==1:
            return '0' + s0
        return s0
    def parse (self):
        self.port = self.data_snmp.split('INTEGER: ')[1]
        self.port = self.port.split('\n')[0]
        s1 = self.data_snmp.split('mib-')[1]
        s2 = s1.split(' = INTEGER:')[0]
        s3 = s2.split('.')
        self.mac_hex = s3[-6] + '.' + s3[-5] + '.' + s3[-4] + '.' + s3[-3]+ '.' + s3[-2]+ '.'  + s3[-1]
        self.mac = self.int_to_hex(s3[-6]) + ':' + self.int_to_hex(s3[-5]) + ':' + self.int_to_hex(s3[-4]) + ':' + self.int_to_hex(s3[-3])+ ':' + self.int_to_hex(s3[-2])+ ':'  + self.int_to_hex(s3[-1])
        return