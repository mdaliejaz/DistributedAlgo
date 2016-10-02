#!/usr/bin/env python3
import queue

class Cache(object):
    def __init__(self):
        self.timestampQueue = {}
        # Tentative Maps

    def addTimestampToQueue(subjectId, timestamp):
        if subjectId not in timestampQueue:
            timestampQueue[subjectId] = queue.Queue()

        timestampQueue[subjectId].put(timestamp)

    def getTimestampFromQueue(subjectId):
        return timestampQueue[subjectId]

    def life(self):
        return 42

cache = Cache()