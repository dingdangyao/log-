#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import configparser
import Logger
import os


def readconf():
    conf = configparser.ConfigParser()
    root_path = '../conf/mlog.conf'
    conf.read(root_path, encoding='utf-8')

    OutType = conf.get("mysql", "logOutType")
    Path = conf.get("mysql", "logPath")
    FileName = conf.get("mysql", "logFileName")
    Level = conf.get("mysql", "logLevel")
    MaxFileNum = conf.get("mysql", "logMaxFileNum")
    MaxFileSize = conf.get("mysql", "logMaxFileSize")

    print(OutType)
    print(Path)
    print(FileName)
    print(Level)
    print(MaxFileNum)
    print(MaxFileSize)

    return [OutType, Path, FileName, Level, MaxFileNum, MaxFileSize]


conf = readconf()
log = Logger.Logger(conf[0], conf[1], conf[2], conf[3], conf[4], conf[5])
log.getlogger()

log.logger.debug('debug')
log.logger.info('info')
log.logger.warning('警告')
log.logger.error('报错')
log.logger.critical('严重')