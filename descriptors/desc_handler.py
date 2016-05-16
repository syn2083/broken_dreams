import dreamscape
import log_system
__author__ = 'Syn'


logger = log_system.init_logging()


# Testing the water with a simple anon chat setup..
def input_handler():
    msg = []
    for d in dreamscape.arch_structs['Dreamers'].sockets().values():
        d.active = True
        if d.command_list:
            msg.append(d.get_command())
            d.send('You say: {}\n'.format(msg[0]))
        if msg:
            send_list = [t for t in dreamscape.arch_structs['Dreamers'].sockets().values() if t is not d]
            for t in send_list:
                t.send('Someone says: {}\n'.format(msg[0]))
            msg = []


# Send whatever we get!
def output_handler(self):
    if self.send_buffer:
        self.send('\n')
        self.miniboa_send()
