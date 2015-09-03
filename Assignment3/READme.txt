#################################
   
   Assignment to build a topology and configure it
   according to the mentioned terms in the assignment
   
#################################
COMMANDS TO RUN THE CODE
###############################
I have mininet in Downloads folder
  
cd Downloads/pox/
./pox.py forwarding.l2_learning openflow.discovery --eat-early-packets openflow.spanning_tree --no-flood --hold-down
  
filename = meshtopology.py | ringtopology.py
on a new terminal run the code :
 
sudo python filename.py no.ofHosts no.ofSwitches
                                                                                                                                                                                                         
##################################                                  