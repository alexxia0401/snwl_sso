A simple guide on CentOS 6.x

```bash
cd /usr
yum install glibc.i686
wget http://10.74.128.89/Software/jre-8u131-linux-i586.tar.gz
tar -zxvf jre-8u131-linux-i586.tar.gz
# make sure /usr/jre1.8.0_131 exits.
wget http://10.74.55.77/new-hire/cnr_7_1_3-linux5.gtar.gz
gtar -zxpf cnr_7_1_3-linux5.gtar.gz
cd /usr/cnr_7_1_3/Linux5
./install_cnr
```

http://<your_ip>:8080  
admin / changeme
