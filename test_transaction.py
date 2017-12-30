#!/usr/bin/env python3

from pow.pow import *
from pow.fullnode import *

m=Fullnode()
m.load_key('C.json')
tr = m.create_transaction('e3ff25f55f612fb2299e494e668580292cd729617f6190571f09897a3227c58b',10)
m.transaction_list.append(tr)
m.start_mining()
