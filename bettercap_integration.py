# This module requires katana framework
# https://github.com/PowerScript/KatanaFramework
#
# For adding module: sudo python2 ktf.ktf --i-module path/to/file/without/file/extention
#

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from time import sleep
from core.Function import get_interfaces,checkDevice,get_monitors_mode,get_gateway
from scapy.all import *
# END LIBRARIES

# END LIBRARIES
def init():
	init.Author             ="Thomas TJ (TTJ)"
	init.Version            ="1.0"
	init.Description        ="Bettercap integration"
	init.CodeName           ="net/bettercap"
	init.DateCreation       ="13/11/2016"
	init.LastModification   ="13/11/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME       VALUE               RQ     DESCRIPTION
		'interface'  :[INTERFACE_ETHERNET,True ,'Interface'],
		'gateway'    :[get_gateway()    ,True,'Gateway address'],
		'sniffer'    :["y"              ,False,'Acitvate sniffer (y/n)'],
		'proxy'      :["y"              ,False,'Use proxy (y/n)'],
		'target'     :[""               ,False,'Target IPs'],
        'path'       :["/usr/bin/bettercap"               ,True,'Path to bettercap']
	}

	init.aux = """
 (filter) options
 -> taget: Single IP or separate with "," or subnet x\\24
 -> proxy: Downgrade HTTPS to HTTP for sniffing

 Devices Founds: """+str(get_interfaces())+"""
 Monitors Inter: """+str(get_monitors_mode())+"""
 Functions     : For Start Monitor Mode, type 'f::start_monitor(Interface)'
"""
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
    i = init.var['interface']
    if i:
        opt_com = '--interface ' + i + ' '

    g = init.var['gateway']
    if g:
        opt_com = opt_com + '--gateway ' + g + ' '

    s = init.var['sniffer']
    if s.lower() == 'y':
        opt_com += '--sniffer' + ' '

    p = init.var['proxy']
    if p.lower() == 'y':
        opt_com += '--proxy' + ' '

    t = init.var['target']
    if t:
        opt_com += '--target ' + t + ' '

    command = (init.var['path'] + ' ' + opt_com)

    print("")
    printAlert(0, "Loading     : Bettercap")
    printAlert(0, "Command     : " + command)
    printAlert(0, "Stop        : Ctrl + C (and wait)")
    printAlert(0, "Starting in : 3 seconds")

    n = 3
    while n > 0:
        printAlert(0, "\t" + str(n) + "..  ")
        n = n-1
        sleep(1)
    print("\n\n")

    os.system(command)
    print("\n\n")
