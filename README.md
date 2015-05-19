NOSE2 Test recipes
==================

Collections of examples on how to use advanced features of nose2.


# Filtering tests using attrib plugin

This makes use of the [attrib](http://nose2.readthedocs.org/en/latest/plugins/attrib.html) plugin.

The groups decorator sets the attributes _group_ or _groups_ in the tests that is decorated.
When the tests are run, the attrib plugin will look for those attributes in the tests methods.

### Examples
```
    run_multiple_group_tests.sh
```

```
    run_single_group_tests.sh
```

# Running tests concurrently

This makes use of the [multiprocess](http://nose2.readthedocs.org/en/latest/plugins/mp.html) plugin.
The concurrency level is set either in the N flag passed to nose2 command or in the nose2 config file.

_Beware of this issue_: if the extent of the concurrency is greater than the number of tests, your tests will hang. E.g. N=5 but there are only 4 tests, your
test run will never exit.

_Beware of this issue_: if there is any import error you will not be able to see it when mp is on: logging gets swallowed. You need to disable the plugin for debugging. 

### Example
```
    run_concurrent_tests.sh
```

# License
The code in this project is distributed under the provision of the Apache License 2.0.
