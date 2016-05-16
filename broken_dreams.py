__author__ = 'Syn'
from descriptors import input_handler

import time
import sysutils
import db_core
import game_init
import log_system


logger = log_system.init_logging()


def broken_dreams():
    logger.boot('Broken Dreams MUDLib Initializing....')
    startup_snapshot = sysutils.ResourceSnapshot()
    logger.boot(startup_snapshot.log_data())
    db_core.init_db()
    from db_core import Session
    from option import Option
    session = Session()
    options = session.query(Option).first()
    logger.boot('Using database version %s, created on %s', options.version, options.date_created)
    from pulse import Pulse
    pulse = session.query(Pulse).first()
    game_init.init_archs()
    server = game_init.init_server()
    done = False
    while not done:
        top_of_loop = time.time()
        server.poll()
        pulse.perform_updates()
        input_handler()
        time_spent = time.time() - top_of_loop
        nap_time = 0.25 - time_spent
        if nap_time > 0.0:
            time.sleep(nap_time)
        else:
            logger.warn('Exceeded time slice by %.3f seconds!', abs(nap_time))

    logger.critical('System Halted!')


if __name__ == '__main__':
    broken_dreams()
