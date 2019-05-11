#!/usr/bin/env python
import time
import logging

from daemons import daemonizer


logging.basicConfig(filename="/tmp/sleepy.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)


@daemonizer.run(pidfile="/tmp/sleepy.pid")
def sleepy(sleep_time):

    cnt = 0
    while True:
        logger.info("{} sec passed".format(cnt * sleep_time))
        time.sleep(sleep_time)
        cnt += 1

sleepy(20)  # Daemon started with 20 second sleep time.
