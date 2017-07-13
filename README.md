### Public network                                                                 
                                                                                   
IP: 10.74.128.87 ~ 10.74.128.89                                                    
netmask: 255.255.255.0                                                             
gateway: 10.74.128.254                                                             
VLAN: 70                                                                           
                                                                                   
| IP             | device          | type    |                                     
| ---            | ---             | ---     |                                     
| 10.74.128.87   | switch          | static  |                                     
| 10.74.128.88   | desktop PC      | static  |                                     
| 10.74.128.89   | CentOS          | static  |                                     
                                                                                   
### Lab network                                                                    
                                                                                   
IP: 100.101.0.128                                                                  
netmask: 255.255.255.224                                                           
gateway: 100.101.0.129                                                             
VLAN: 166                                                                          
                                                                                   
| IP             | device          | type    |                                     
| ---            | ---             | ---     |                                     
| 100.101.0.130  | CentOS          | static  |                                     
| 100.101.0.131  | TBD             | DHCP    |                                     
| 100.101.0.158  | TBD             | DHCP    |  
