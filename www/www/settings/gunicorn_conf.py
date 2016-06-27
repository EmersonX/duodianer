# -*- coding:utf-8 -*-
import multiprocessing

bind = '0.0.0.0:8000'
backlog = 128
workers = 4
workers_class = 'sync'
timeout = 60