from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections                                                                   
from mininet.node import Controller, RemoteController, OVSController, CPULimitedHost
from mininet.cli import CLI
from mininet.link import TCIntf, TCLink
from mininet.log import setLogLevel                          
import sys
import os

class nSwitchTopo(Topo):
    def build(self, nHost, nSwitch):
        for i in range(nSwitch):
            switch = self.addSwitch('s'+str(i+1))
            for j in range(i):
                self.addLink('s'+str(i+1), 's'+str(j+1))
        nh = 1
        nhostperSwitch = nHost/nSwitch
        remaining = nHost - nhostperSwitch*nSwitch
        print remaining, "remaining"
        for i in range(nSwitch):
            for j in range(nhostperSwitch):
                host = self.addHost('h%s' % (nh), ip = "10.0."+str((nh)%2)+"."+str(nh)+"/24")
                self.addLink(host, 's%s' % (i+1))
                nh += 1

        for i in range(remaining):
            host = self.addHost('h%s' % (nHost-remaining+i+1))
            self.addLink(host, 's%s' % (i+1))

        

def simpleTest():
    if len(sys.argv) != 3:
        print "Usage: sudo python topology.py no.ofHosts no.ofSwitches"
        exit()
    nHost = int(sys.argv[1])
    nSwitch = int(sys.argv[2])
    
    topo = nSwitchTopo(nHost=nHost, nSwitch=nSwitch)

    net = Mininet(topo, link=TCLink, controller=RemoteController)
    net.start()
    net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity----Press Enter"
    x = raw_input()
    #CLI(net)
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()


