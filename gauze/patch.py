from __future__ import print_function

import inspect


def patch(function_to_patch, lines):
    assert callable(function_to_patch)
    assert isinstance(lines, list) or isinstance(lines, tuple)

    function_source = inspect.getsourcelines(function_to_patch)[0]

    # We need to unindent the function source in case it's nested in another block (e.g. from a class)
    # TODO: Refactor this
    i = 0
    for chr in function_source[0]:
        if chr == ' ':
            i += 1
        else:
            break

    new_source = []
    for source_line in function_source:
        for line, replacement in lines:
            line_stripped = source_line.rstrip('\n')[i:]
            if line_stripped == line:
                if replacement:
                    new_source.append(replacement + '\n')
                break
        else:
            new_source.append(source_line[i:])

    new_source = "".join(new_source)

    exec(new_source, locals())

    # We just created a function in local scope so we need to return it
    return locals()[function_to_patch.__name__]
