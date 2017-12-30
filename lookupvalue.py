#!/usr/bin/env python3
from pow.fullnode import *

m = Fullnode()
m.load_addr('C_addr.json')
m.load_latest_block()
print(m.get_addr_value(m.addr))
