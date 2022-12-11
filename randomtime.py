import time
from random import randint

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)

def compra():
    date = random_date('2020/01/01', '2022/12/14')
    pessoa = randint(1,100)
    proqt = randint(1,15)
    prod = []
    for i in range(proqt):
        prod.append(randint(1, 200))
    return prod