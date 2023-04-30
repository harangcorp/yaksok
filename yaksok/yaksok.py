import copy
import os

from . import yacc
from . import bootbakyi


def run_code(code, file_name):
    code = yacc.compile_code(code, file_name=file_name)
    locals_dict = {}

    g = copy.deepcopy(yaksok_globals)
    locals_dict['____functions'] = g['____functions']

    exec(code, g, g)
    return g


bootbakyi.____run_code = run_code
bootbakyi.____libpath = os.path.join(os.path.split(__file__)[0], 'modules')


yaksok_globals = {k: getattr(bootbakyi, k) for k in dir(bootbakyi)}
