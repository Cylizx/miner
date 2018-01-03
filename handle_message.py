#!/usr/bin/env python3
from messages import *
import os,time, json

def handle_message(obj):
    # TODO: jas0n1ee
    # receive an message object
    # return an object as a response
    if isinstance(obj,TxMessage):
        while True:
            if os.path.exists('transaction/new.json'):
                time.sleep(1)
            else:
                with open('transaction/new.json','w') as f:
                    json.dump(obj.tx,f)
                print('get new message!!!')
                break

    return None
