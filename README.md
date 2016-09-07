Gauze
=======
Weave a patch into your libraries

Use
---

```
import gauze
import module_to_patch

replacement = (
    ('    return True', '    return False')
)
module_to_patch.function_to_patch = gauze.patch(module_to_patch.function_to_patch, replacement)
```

`#TODO`
----
Add a function attribute to patched function?
Avoid duplication of function name pointer?
Test it works for complex functions
Catch errors from exec?
Logging
Warning about monkey patched function when debugging or just generally?
Python 2 + 3 checks


FAQs
----
# So, what exactly does this do?
It lets you monkey patch any function using a patch like syntax

# Why wouldn't I just monkey patch it the old fashioned way?
This way you can avoid copying the whole function and having no one in your team (or indeed you in a few months time) 
knowing what you changed!

# Couldn't I just add some comments to the function?
If your team actually reads comments... sure.

# Anyway, so how does this actually work?
It uses the inspect module to get the source code of a compiled function...

# But isn't it recommended to not use that module in production code?
It's mainly for performance reasons and as it's only used at import time it doesn't affect performance substantially.

# So anything else I should know about?
It uses `exec`.

# Whoa, wait, that's pretty awful
It's fine, namedtuple uses it

# So do you use this in production?
Hell no!

# So what do you do?
Fork the project, make a PR and use the fork until the PR is merged.
