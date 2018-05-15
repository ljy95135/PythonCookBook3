import pdb

pdb.pm()

import traceback
import sys

try:
    func(arg)
except Exception:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)
