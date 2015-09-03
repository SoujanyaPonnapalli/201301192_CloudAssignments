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
            if i !=0:
                self.addLink('s'+str(i+1), 's'+str(i))

        self.addLink('s'+str(nSwitch), 's1')
        self.addLink('s'+str(nSwitch),'s1')
        nhostperSwitch = nHost/nSwitch
        remaining = nHost - nhostperSwitch*nSwitch
        print remaining, "remaining"
        for i in range(nSwitch):
            for j in range(nhostperSwitch):
                nh = i+j+1;
                if(nh%2) :
                    bwidth = 1
                else :
                    bwidth = 2
                host = self.addHost('h%s' % (i+j+1), ip = "10.0."+str((nh)%2)+"."+str(nh)+"/24")
                self.addLink(host, 's%s' % (i+1), bw=bwidth)

        for i in range(remaining):
            nh = nHost-remaining+i+1
            host = self.addHost('h%s' % (nHost-remaining+i+1), ip = "10.0."+str((nh)%2)+"."+str(nh)+"/24")
            self.addLink(host, 's%s' % (i+1))

        

def simpleTest():
    if len(sys.argv) != 3:
        print "Usage: sudo python topology.py no.ofHosts no.ofSwitches"
        exit()
    nHost = sys.argv[1]
    nSwitch = sys.argv[2]
    
    topo = nSwitchTopo(nHost=int(nHost), nSwitch=int(nSwitch))

    net = Mininet(topo, link=TCLink, controller=RemoteController)
    net.start()
    net.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity, press enter"
    x = raw_input()
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()


