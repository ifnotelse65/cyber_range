# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import math
sys.path.append('/home/seed/Desktop/cyber_range/seed-emulator')
import random
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
    #router.joinNetwork('ix101')
    for i in range(0,host_num):
        name = 'host_{}'.format(i)
        AS.createHost(name).joinNetwork('net0')
    for i in range(0,web_num):
        name = str(asnumber)+'_web_'+str(i)
        AS.createHost(name).joinNetwork('net0')
        vnodename='web'+str(120+i)
        web.install(vnodename)
        emu.addBinding(Binding(vnodename, filter=Filter(asn=asnumber, nodeName=name)))

def sampletwo(list,num):
    length=len(list)
    ret1=[]
    sum=length*(length-1)/2
    trans=[]
    for i in range(0,sum):
        trans.append(i)
    for i in range(0,length):
        for j in length(i+1,length):
            ret1.append(list[i])
            ret1.append(list[j])
    ret2=random.sample(trans,num)
    return ret1,ret2


#def as_2():
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
    #n=3
    #list=[0,1,1,0,0,0,1,0,0]
    list=[]
    with open('data.txt') as f:
        for line in f:
            list.extend([int (i) for i in line.split()])
    print(list)
    n=math.sqrt(len(list))
    print(n)
    n=int(n)
    AS = []
    IX = []
    for i in range(0,n):
        AS.append(base.createAutonomousSystem(120 + i))
        web_num=random.randint(1,2)
        host_num=random.randint(2,4)
        as_1(AS[i], 120 + i, host_num, web_num)
    sum=0
    for i in range(0,n):
        for j in range(i+1,n):
            trans1=list[i*n+j]
            trans2=list[j*n+i]
            if(trans1==1 or trans2 == 1):
                IX.append(base.createInternetExchange(50+sum))
                IX[sum].getPeeringLan().setDisplayName('NYC-50'+str(sum))
                AS[i].getRouter('router0').joinNetwork('ix'+str(50+sum))
                AS[j].getRouter('router0').joinNetwork('ix'+str(50+sum))
                if(trans1==1 and trans2 ==0):
                    ebgp.addPrivatePeerings(50+sum,[120+i],[120+j],PeerRelationship.Provider)
                if (trans1 == 0 and trans2 == 1):
                    ebgp.addPrivatePeerings(50 + sum, [120 + j], [120 + i], PeerRelationship.Provider)
                if (trans1 == 1 and trans2 == 1):
                    ebgp.addRsPeers(50+sum, [120+i, 120+j])
                sum = sum + 1
    '''IE_sum=[]
    for i in range(0,sum):
        IE_sum.append(50+sum)
    edge=sum*(sum-1)/2/2
    tr_asn_num=edge/2
    ret1,ret2=sampletwo(IE,tr_as_num)
    for i in range(0,tr_asn_num):
        Makers.makeTransitAs(base, i, IE_sum,[ret1[2*i],ret1[2*i+1]])'''





    '''ix101 = base.createInternetExchange(101)
    ix101.getPeeringLan().setDisplayName('russia-101')
    as_num=5
    AS=[]
    for i in range(0,as_num):
        AS.append(base.createAutonomousSystem(120+i))
        as_1(AS[i],120+i,2,1)
    as_trans=[]
    for i in range(120,120+i):
        as_trans.append(i)
    ebgp.addRsPeers(101, as_trans)'''



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
        ix.append(base.createInternetExchange(50+i))'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
