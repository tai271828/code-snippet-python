import time
import logging

from daemons.prefab import run


logger = logging.getLogger(__name__)


class SleepyDaemon(run.RunDaemon):

    def run(self):
        cnt = 0
        while True:
            logger.info("{} sec passed".format(cnt))
            time.sleep(1)
            cnt += 1
