#coding=utf-8

def argsAsDict(args):
    argsdict = {}
    for key, value in args:
        if value is not None:
            argsdict[key] = value
    return argsdict