# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from seedemu.layers import Base, Routing, Ebgp, Ibgp, Ospf, PeerRelationship, Dnssec
from seedemu.services import WebService, DomainNameService, DomainNameCachingService
from seedemu.services import CymruIpOriginService, ReverseDomainNameService, BgpLookingGlassService
from seedemu.compiler import Docker, Graphviz
from seedemu.hooks import ResolvConfHook
from seedemu.core import Emulator, Service, Binding, Filter
from seedemu.layers import Router
from seedemu.raps import OpenVpnRemoteAccessProvider
from seedemu.utilities import Makers

from typing import List, Tuple, Dict


def as_1(AS,asnumber,host_num,web_num):
    AS.createNetwork('net0')
    router = AS.createRouter('router0')
    router.joinNetwork('net0')
    router.joinNetwork('ix101')
    for i in range(0,host_num):
        name = 'host_{}'.format(i)
        AS.createHost(name).joinNetwork('net0')
    for i in range(0,web_num):
        name = str(asnumber)+'_web_'+str(i)
        AS.createHost(name).joinNetwork('net0')
        vnodename='web'+str(120+i)
        web.install(vnodename)
        emu.addBinding(Binding(vnodename, filter=Filter(asn=asnumber, nodeName=name)))
    '''
    
    host_num=5
    host_name=[]
    for i in range(0,host_num):
        host_name.append("web"+str(i))
    AS.createNetwork('net0')
    AS.createRouter('router0').joinNetwork('net0').joinNetwork('ix101')
    web.install('virweb')
    for i in range(0,host_num):
        AS.createHost(host_name[i]).joinNetwork('net0')
        emu.addBinding(Binding('virweb', filter=Filter(nodeName=host_name[i], asn=asnumber)))

    :param AS: 
    :param asnumber: 
    :return: 
    '''

#def as_2(asn):



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #russian_city=['a','c','cd','gf','gsd','dgfb']
    #ukraine_city=['esd','sgrdf','asfd','sgfd','sgrd']
    emu = Emulator()
    base = Base()
    routing = Routing()
    ebgp = Ebgp()
    ibgp = Ibgp()
    web = WebService()
    ix101 = base.createInternetExchange(101)
    ix101.getPeeringLan().setDisplayName('russia-101')
    as_num=5
    AS=[]
    for i in range(0,as_num):
        AS.append(base.createAutonomousSystem(120+i))
        as_1(AS[i],120+i,2,1)
    as_trans=[]
    for i in range(120,120+i):
        as_trans.append(i)
    ebgp.addRsPeers(101, as_trans)
    emu.addLayer(base)
    emu.addLayer(routing)
    emu.addLayer(ebgp)
    emu.addLayer(ibgp)
    emu.addLayer(Ospf())
    emu.addLayer(web)

    emu.render()

    emu.compile(Docker(selfManagedNetwork=True, clientEnabled=True), './output')

    '''ix_number=10
    ix=[]
    for i in range(0,ix_number):
        ix.append(base.createInternetExchange(100+i))'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
