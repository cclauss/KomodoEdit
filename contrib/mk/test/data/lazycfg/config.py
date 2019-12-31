#!/usr/bin/env python
# config.py -- project configuration
# Generated by "". Modifications will be lost.
# See " --help" for details.

from __future__ import print_function
_configure_opts = []

foo = 'bar'


#---- mainline
# Usage:
#   python config.py SUBSTRING...
# Prints the value of all config variables matching each substring.
#
def _main():
    import sys
    from pprint import pprint
    m = sys.modules[__name__]
    var_names = [k for k in m.__dict__.keys() if k != "_main"]
    for substring in sys.argv[1:]:
        substring_lower = substring.lower()
        for var_name in var_names:
            if substring_lower in var_name.lower():
                print("%s: %r" % (var_name, getattr(m, var_name)))
if __name__ == "__main__":
    _main()
