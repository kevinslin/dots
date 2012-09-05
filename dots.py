#!/usr/bin/env python2.7
"""
Script to install dotfiles
Copyright 2012 Kevin S Lin

Basic Usage:
    ./install.py
"""
import argparse
import sys
import os

from settings import *
from utils import get_symlinks

__version__ = '0.0.1'

def warn():
    resp = raw_input("about to install modules, continue?: [y]es, [n]o: ")
    if (resp.lower() == 'n'):
        sys.exit()


def get_response(fname):
    prompt = "%s exists. [s]kip, [S]kip All, [o]verwrite: " % fname
    resp = ''
    while (resp not in ['s', 'S', 'o']):
        resp = raw_input(prompt)
    return resp


def get_confirm():
    resp = ''
    while (resp not in ["y", "n"]):
        resp = raw_input("do you want to create %s? [y]es, [n]o: " % fname)
    return resp

def parse_args():
    """
    Parse arguments for dots
    """
    p = argparse.ArgumentParser(description="dotfiles installer",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('-c', '--confirm', default = False, action = 'store_true',
            help="ask for confirmation before linking")
    p.add_argument('-t', '--target', default = TARGET,
            help="Specify target directory")
    p.add_argument('--skip_all', default = SKIP_ALL, action = 'store_true',
            help = "Don't overwrite any local files")
    p.add_argument('--dry_run', default = False, action = 'store_true',
            help = "Only print results")
    return p.parse_args(sys.argv[1:])



def install(args=None):
    """
    Install dotfiles in computer
    """

    print (args)
    print ("dest: %s" % args.target)
    symlinks = get_symlinks()
    warn()

    for path, links in symlinks:
        for link in links:
            # Create link to new file
            fname = "." + link.rsplit(".symlink")[0]
            fpath_old = os.path.join(path, link)
            fpath = os.path.join(args.target, fname)

            # handle file collisions
            flag_create = True
            resp = None
            if (os.path.exists(fpath)):
                # skip all on, then skip file
                if (args.skip_all):
                    flag_create = False
                else:
                    resp = get_response(fname)
                    if (resp == 's'):
                        flag_create = False
                    elif (resp == 'S'):
                        args.skip_all = True
                        flag_create = False
                    elif (resp.lower() == 'o'):
                        print ("overwriting...")
                        os.remove(fpath)
                    else:
                        # code should not get here
                        assert(false)
            # If resp is set, assume user already made up mind on fate of file
            if (args.confirm) and (resp is not None):
                resp = get_confirm()
                if (resp == 'n'):
                    flag_create = False

            # Create hard link to dot file
            if (flag_create):
                print("linking %s to %s" % (fname, fpath))
                if not args.dry_run: os.link(fpath_old, fpath)
            else:
                print("skipping %s" % fname)
    print("done :)")

def main():
    args = parse_args()
    install(args)


#Rename files to proper names
#symlinks = map(lambda x: '.' + x.rstrip('.symlink'), symlinks)
if __name__ == "__main__":
    main()

