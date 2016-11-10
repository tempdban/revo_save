#! /usr/bin/env python

import struct, sys, os
from os.path import getsize



def flashtorevo(path, size):
    print 'Vba flash format found!'
    s = struct.Struct(str(size)+'s')
    tail = s.pack('\xff'*size)

    with open(path, 'rb') as file:
        sav = file.read()

    with open(path+'.out', 'wb') as file:
        file.write(sav)
        file.write(tail)

def eeprom(path, size):
    print 'Eeprom format found!'
    s = struct.Struct(str(size)+'s')
    head = s.pack('\xff'*size)

    with open(path, 'rb') as file:
        sav = file.read()

    with open(path+'.out', 'wb') as file:
        file.write(head)
        file.write(sav)


def revo(path, size):
    print 'Revo format found!'

    with open(path, 'rb') as file:
        flash = file.read(131072)
        eeprom = file.read(8192)
    with open(path+'.flash', 'wb') as file:
        file.write(flash)
    with open(path+'.eeprom', 'wb') as file:
        file.write(eeprom)

mapper = {
    'flash' : [flashtorevo, 32*1024, 64*1024, 128*1024],
    'eeprom' : [eeprom, 8*1024],
    'revo' : [revo, (128+8)*1024]
    }

FILESIZE = 139264

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except Exception, e:
        sys.exit(-1)
    size = getsize(path)
    for savformat in mapper.values():
        if size in savformat:
            savformat[0](path, FILESIZE-size)
            sys.exit(0)
    print 'Not a valid save format.'
    sys.exit(-1)
