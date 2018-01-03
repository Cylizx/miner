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

def send_transaction(dst_addr,value,key):
    m = Fullnode()
    m.load_key(key)
    tr = m.create_transaction(dst_addr,value)
    time.sleep(1)
    network.broadcast_message(TxMessage(tr))



if __name__ == '__main__' :
    wallet={}
    for p in ['A','B','C','D','E','F']:
        with open (p+'_addr.json','r') as f:
            wallet[p] = json.load(f)[0]
        print(p+': '+str(get_addr_value(wallet[p])))

    for p in ['A','B','D','E','F']:
        send_transaction(wallet[p],10,'C.json')
    print(get_next_header())

    for p in ['A','B','C','D','E','F']:
        with open (p+'_addr.json','r') as f:
            wallet[p] = json.load(f)[0]
        print(p+': '+str(get_addr_value(wallet[p])))

        

