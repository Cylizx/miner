#!/usr/bin/env python3

import sys

import messages
import network
import client
from utils import get_local_ip

if 'network' not in sys.modules:
    import network

if 'client' not in sys.modules:
    import client


class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return self.ip + ':' + str(self.port)

    def __eq__(self, other):
        return self.ip == other.ip and self.port == other.port

    def __hash__(self):
        return self.ip.__hash__() * 65536 + self.port


known_peers = set()
known_peers.add(
    Peer('127.0.0.1', 10086)
)

local_peer = Peer(get_local_ip(), 10086)


def get_local_peer():
    return local_peer


def add_peer_to_known_peers(peer):
    print('add new peer: ' + str(peer))
    known_peers.add(peer)


def get_known_peers():
    return known_peers


def init_peers(port):
    global local_peer
    local_peer = Peer(get_local_ip(), port)
    add_peer_to_known_peers(local_peer)
    find_peer()
    network.broadcast_message(messages.PeersMessage(get_known_peers()))


def find_peer():
    global known_peers
    for peer in list(known_peers):
        if peer == get_local_peer():
            continue
        sender = client.Sender(peer)
        peers_message = sender.send_message(messages.GetPeersMessage())
        for new_peer in peers_message.peers:
            add_peer_to_known_peers(new_peer)


if __name__ == '__main__':
    exit()
