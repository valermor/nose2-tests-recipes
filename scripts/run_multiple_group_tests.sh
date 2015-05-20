#!/usr/bin/env bash

############################################################################
# Copyright 2015 Valerio Morsella                                          #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License");          #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#    http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################

#This should parse the whole project looking for test classes and run only tests that are decorated with @groups and contain labels A_GROUP, ANOTHER_GROUP and do not
#contain label EXCLUDED_GROUPS
#The tests run in parallel and generate a junitxml report at the end of the execution.

echo nose2 --plugin nose2.plugins.attrib --config nose2.cfg -E'"A_GROUP" in groups and "ANOTHER_GROUP" in groups and not "EXCLUDED_GROUP" in groups'
nose2 --plugin nose2.plugins.attrib --config nose2.cfg -E'"A_GROUP" in groups and "ANOTHER_GROUP" in groups and not "EXCLUDED_GROUP" in groups'
