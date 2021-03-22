#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import logging
from logging import handlers


class Logger(object):

    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL

    }

    def __init__(self, logOutType, logPath, logFileName, logLevel, logMaxFileNum, logMaxFileSize):
        self.logOutType = logOutType
        self.logPath = logPath
        self.logFileName = logFileName
        self.logLevel = logLevel
        self.logMaxFileNum = logMaxFileNum
        self.logMaxFileSize = logMaxFileSize
        self.logger = logging.getLogger(self.logFileName)

    def getlogger(self):
        def_format = '%(asctime)s] [%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s'

        self.logger.setLevel(self.logLevel)

        logMaxFileSize = int(self.logMaxFileSize) * 1024 * 1024
        logMaxFileNum = int(self.logMaxFileNum)

        formater = logging.Formatter(def_format)

        if self.logOutType == 'file':
            th = handlers.TimedRotatingFileHandler(filename=self.logPath+self.logFileName,
                                                   backupCount=logMaxFileNum,
                                                   encoding='utf-8')
            th.setFormatter(formater)

            self.logger.addHandler(th)

        if self.logOutType == 'terminal':
            sh = logging.StreamHandler()
            sh.setFormatter(formater)

            self.logger.addHandler(sh)

        if self.logOutType == 'all':
            th = handlers.TimedRotatingFileHandler(filename=self.logPath+self.logFileName,
                                                   backupCount=logMaxFileNum,
                                                   encoding='utf-8')

            th.setFormatter(formater)

            sh = logging.StreamHandler()
            sh.setFormatter(formater)

            self.logger.addHandler(th)
            self.logger.addHandler(sh)
