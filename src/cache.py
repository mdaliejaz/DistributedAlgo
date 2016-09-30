#!/usr/bin/env python3
import queue

class Cache(object):
    def setup():
        self.timestampQueue = {}
        # Tentative Maps

    def addTimestampToQueue(subjectId, timestamp):
        if subjectId not in timestampQueue:
            timestampQueue[subjectId] = queue.Queue()

        timestampQueue[subjectId].put(timestamp)

    def getTimestampFromQueue(subjectId):
        return timestampQueue[subjectId]

    def hell():
        return -123

cache = Cache()