__author__ = 'Syn'
import os
import log_system

logger = log_system.init_logging()

current_location = os.getcwd()
uid_file = 'bd_uid'

target_location = os.path.join(current_location, 'uid\\' + uid_file)


class UID_Arch:
    def __init__(self):
        self._current_uid = None
        self._file_uid = None

    def load_uid(self):
        if not os.path.exists(target_location):
            logger.boot('Creating UID file')
            with open(target_location, 'w') as uid_init:
                uid_init.write('1')
                self._current_uid = 1
                self._file_uid = 1

        else:
            with open(target_location, 'r') as uid_resume:
                logger.boot('Loading UID File')
                self._current_uid = int(uid_resume.read())
                self._file_uid = self._current_uid

    def obtain_uid(self):
        logger.info('Current UID {}'.format(self._current_uid))
        if self._current_uid:
            self._current_uid += 1
            logger.info('Incrementing UID {}'.format(self._current_uid))
        else:
            self.load_uid()
            self._current_uid += 1
        return self._current_uid

    def save_uid(self):
        if self._current_uid > self._file_uid:
            with open(target_location, 'w') as uid_update:
                logger.info('Writing UID File {}'.format(self._current_uid))
                uid_update.write(str(self._current_uid))
                self._file_uid = self._current_uid

    def __str__(self):
        return 'Current UID is {}'.format(self._current_uid)
