__author__ = 'Syn'
from UID import UID_Arch
from descriptors import Dreamer_Arch, output_handler

import dreamscape
import miniboa
import types
import log_system


logger = log_system.init_logging()


def init_archs():
    d = Dreamer_Arch()
    u = UID_Arch()
    u.load_uid()
    dreamscape.arch_structs['Dreamers'] = d
    logger.boot('Dream catcher initialized.')
    dreamscape.arch_structs['UID'] = u
    logger.boot('UID initialized. Current UID is {}'.format(str(u)))


def init_descriptor(socket):
    socket.send('Welcome to Broken Dreams!')
    socket.active = True
    socket.original = None
    socket.id = dreamscape.arch_structs['UID'].obtain_uid()
    logger.info('Adding descriptor {}'.format(socket.id))
    dreamscape.arch_structs['Dreamers'].add_socket(socket)
    socket.miniboa_send = socket.socket_send
    socket.socket_send = types.MethodType(output_handler, socket)
    socket.request_terminal_type()
    socket.request_naws()


def init_server():
    server = miniboa.TelnetServer(port=dreamscape.port, timeout=dreamscape.timeout)
    logger.boot('Broken Dreams is ready to rock on port {}!'.format(dreamscape.port))
    server.on_connect = init_descriptor
