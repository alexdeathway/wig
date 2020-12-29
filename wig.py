#!/usr/bin/env python3
import os,sys
from wig.wig import Wig, parse_args
from wig.wizard import wizard, getresponse, WigSuccess, WigExit


# if called from the command line
if __name__ == '__main__':
    try:
        args = parse_args()
    except:
        
        if getresponse():
            os.system(wizard())
            WigSuccess("Process Complete.")
        else:
            WigExit("Exiting Wig")
    
    try:
        wig = Wig(args)
        wig.run()
    except KeyboardInterrupt:
        raise
