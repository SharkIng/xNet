#!/usr/bin/env python
##
# Copyright (c) 2017 Shacas Studio && TheMaple Network Inc.
# All rights reserved.
#
# File: xnet.py
# Created Date: Mon Feb 06 2017
# Author: SharkIng <SharkIng#Shacas.com>
#
# You should have received a copy of the MIT License
# along with this program. If not see http://www.opensource.org/licenses/MIT
###

import optparse

class xNetwork(object):
  def __init__(self):
    self.__version__ = '0.1.0'
    self.__hosts = {}
    self.__servers = {}

  def load(self, lock):
    if lock:
      return True
    else:
      return False

  def release(self):
    return True

  def show_status(self):
    pass

def interact(edit=False):
  # Load an existing network object, interact with it, then save changes
  print 'loading...'
  xNet = xNetwork()
  xnet = xNet
  xnet.show_status()
  import code
  try:
    code.interact(
      'xNet Console\n' +
      '-----------------\n' +
      ('%s mode\n' % ('EDIT' if edit else 'READ-ONLY',)) +
      'Interact with the \'xNet\' or \'xnet\' object...\n',
      local=locals())
  except SystemExit as e:
    raise e

def view():
  interact(False)

def edit():
  interact(True)

if __name__ == "__main__":
  option_parser = optparse.OptionParser('usage: %prog [options]')
  option_parser.add_option('-r', '--read-only', dest='readonly', action='store_true',
                           help='Read only access to database')
  (options, _) = option_parser.parse_args()

  if options.readonly:
    view()
  else:
    edit()
