#! /usr/bin/env python

""" j2cmd main file """
import pkg_resources

__author__ = "Mark Vartanyan"
__email__ = "kolypto@gmail.com"
__version__ = pkg_resources.get_distribution('j2cmd').version

from j2cmd.cli import main

if __name__ == '__main__':
    main()
