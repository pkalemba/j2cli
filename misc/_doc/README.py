#! /usr/bin/env python

import json
import inspect
from exdoc import doc, getmembers

import j2cmd
import j2cmd.context
import j2cmd.extras.filters


README = {
    'formats': {
        name: doc(f)
        for name, f in j2cmd.context.FORMATS.items()
    },
    'extras': {
        'filters': {k: doc(v)
                    for k, v in getmembers(j2cmd.extras.filters)
                    if inspect.isfunction(v) and inspect.getmodule(v) is j2cmd.extras.filters}
    }
}

assert 'yaml' in README['formats'], 'Looks like the YAML library is not installed!'

print(json.dumps(README))
