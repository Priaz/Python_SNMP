#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

def getport(switch_number):
	port=0
	sw = int(switch_number.split('/')[0])
	if sw == 1:
		port=0
	if sw == 2:
		port=64
	if sw == 3:
		port=128
	if sw == 4:
		port=192
	if sw == 5:
		port=256

	interface_port = int(switch_number.split('/')[2])
	port=port+interface_port
	return port

