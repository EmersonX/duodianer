# -*- coding:utf-8 -*-
import multiprocessing

bind = '127.0.0.1:8000'
backlog = 64
workers = 2
workers_class = 'sync'
timeout = 60