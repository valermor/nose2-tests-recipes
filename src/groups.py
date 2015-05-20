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

SINGLE_GROUP = 'SINGLE_GROUP'
A_GROUP = 'A_GROUP'
ANOTHER_GROUP = 'ANOTHER_GROUP'
EXCLUDED_GROUP = 'EXCLUDED_GROUP'
CONCURRENT = 'CONCURRENT'
DATA_PROVIDER = 'DATA_PROVIDER'

def groups(*group_list):
    """Decorator that adds group name to test method for use with the attributes (-A) plugin.
    """
    def wrap_ob(ob):
        if len(group_list) == 1:
            setattr(ob, "group", group_list[0])
        elif len(group_list) > 1:
            setattr(ob, "groups", group_list)
        return ob
    return wrap_ob
