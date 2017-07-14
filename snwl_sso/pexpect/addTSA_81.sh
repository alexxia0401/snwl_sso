#!/bin/bash

# ./addTSA_9800.py 10.7.70.93 1.1.1.1 123456

WANIP='10.0.0.68'
KEY='123456'

repeat()
{
    for((j=1;j<63;++j))
    do
        ./addTSA_9800.py $WANIP 192.168.$1.$j $KEY
    done
}

#for((x=82;x<=88;++x))
#do
#    repeat $x
#done

for((j=1;j<=16;++j))
do
    ./addTSA_9800.py $WANIP 192.168.89.$j $KEY
done
