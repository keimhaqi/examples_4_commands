#!/usr/bin/python
# -*- coding: UTF-8 -*-

def partial(function, *args, **kwargs):
    def ret(*iargs, **ikwargs):
        print locals()
        return function(*(args+iargs), **dict(ikwargs, **kwargs))
    return ret

def add(x,y):
    return x+y

add5 = partial(add, 5)
print add5(6)