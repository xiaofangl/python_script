#!/usr/bin/env python
# encoding: utf-8
# author: xiaofangliu
import os
import re

"""
    re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)"
"""


# find group add host
def add_host(file_name, host, group):
    res = {
        'status': True,
        'message': ''
    }
    host = '' if not host else host
    try:
        i = 1
        with open(file_name, 'r+') as f:
            line = f.readline()
            while line:
                if group in line:
                    host = host + "\n"
                    f.write(host)
                    break
                line = f.readline()
                i += 1
            else:
                return False, 'start null...'
        res['status'] = host(file_name)
        if res['status']:
            pass
        else:
            res['message'] = 'delect item false!!'
    except IOError:
        res['status'] = False
        res['message'] = 'file wirte false！'
    return res


# sed
def del_host(file_name, host, group):
    res = {
        'status': True,
        'message': ''
    }
    host = '' if not host else host
    try:
        i = 1
        with open(file_name, 'r') as f:
            line = f.readline()
            # print f.tell()
            while line:
                if group in line:
                    _this = f.tell()
                    break
                line = f.readline()
                i += 1
            else:
                _this = False

        i = i + 1
        with open(file_name, 'r') as f_r:
            lines = f_r.readlines()
            f_r.seek(_this, 0)
            line = f_r.readline()
            while line:
                if "[" in line:
                    _end = f_r.tell()
                    break
                if i == len(lines):
                    print i, lines
                    _end = f_r.tell()
                    print 'last line', _end
                line = f_r.readline()
                i += 1
            else:
                _end = False

        if _this == False:
            res['status'] = False
            res['message'] = 'start  false！'
        elif _end == False:
            res['status'] = False
            res['message'] = 'end  false！'
        elif _this == _end:
            res['status'] = False
            res['message'] = '_this == _end！'
        else:
            with open(file_name, 'r') as f_r:
                with open(file_name, 'r+') as f_w:
                    f_r.seek(_this, 0)
                    line = f_r.readline()
                    while line and f_r.tell() <= _end:
                        host = "192.168.100.44" if not host else host

                        if line.strip().replace('/n', '') == host:
                            host = f_r.tell()
                            print f_r.tell()
                            print 'host it..', line, i
                            f_w.seek(host, 0)
                            line = f_r.readline()
                            print 'i', i, line
                            next_line = f_r.readline()
                            print 'i--', i, next_line
                            # next_line = line
                            while next_line:
                                f_w.write(next_line)
                                next_line = f_r.readline()
                            # break
                            f_w.truncate()
                        line = f_r.readline()

    except Exception as e:
        pass
    return res


if __name__ == '__main__':
    print os.getcwd()
    # fr = open('./hosts', 'r')
    # c = fr.readline()
    # print 'c:: ', c
    del_host('./hosts', '192.168.99.250', 'vue_test')


