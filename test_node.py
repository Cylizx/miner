#!/usr/bin/env python3
from pow.fullnode import *
import network,_thread,time
from messages import *

_thread.start_new_thread(network.init,(10083,))

def get_next_header():
    old = ""
    with open('block/head.json','r') as f:
        old = json.load(f)[0]
    while True:
        time.sleep(1)
        with open('block/head.json','r') as f:
             curr = json.load(f)[0]
             if old != curr:
                 return curr

def get_addr_value(addr):
    m = Fullnode()
    m.load_latest_block()
    return m.get_addr_value(addr)

def send_transaction(src_addr,dst_addr,value,key):
    tr={};
    tr['src_addr']=src_addr
    tr['dst_addr']=dst_addr
    tr['value']=10
    tr['timestamp']=time.time()
    time.sleep(1)
    network.broadcast_message(TxMessage(tr))



if __name__ == '__main__' :
    wallet={}
    for p in ['A','B','C','D','E','F']:
        with open (p+'_addr.json','r') as f:
            wallet[p] = json.load(f)[0]
        print(p+': '+str(get_addr_value(wallet[p])))

    for p in ['A','B','D','E','F']:
        send_transaction(wallet['C'],wallet[p],10,'')
    print(get_next_header())

    for p in ['A','B','C','D','E','F']:
        with open (p+'_addr.json','r') as f:
            wallet[p] = json.load(f)[0]
        print(p+': '+str(get_addr_value(wallet[p])))

        

