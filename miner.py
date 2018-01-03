#!/usr/bin/env python3
from pow.fullnode import *

m = Fullnode()
m.start_listening(10086)
m.load_addr('C_addr.json')
m.load_latest_block()
m.start_mining()
