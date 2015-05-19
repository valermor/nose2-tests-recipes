NOSE2 Test recipes
==================

Collections of examples on how to use advanced features of nose2.


# Filtering tests using attrib plugin

This makes use of the [attrib](http://nose2.readthedocs.org/en/latest/plugins/attrib.html) plugin.

The groups decorator sets the attributes _group_ or _groups_ in the tests that is decorated.
When the tests are run, the attrib plugin will look for those attributes in the tests methods.

Examples are in the scripts:
```
    run_multiple_group_tests.sh
```

```
    run_single_group_tests.sh
```

# License
The code in this project is distributed under the provision of the Apache License 2.0.
