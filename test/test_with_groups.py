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

import unittest

from src.groups import groups, SINGLE_GROUP, A_GROUP, ANOTHER_GROUP, EXCLUDED_GROUP


class SingleGroupTest(unittest.TestCase):

    @groups(SINGLE_GROUP)
    def test_sorting_return_results_by_guest_rating(self):
        print 'first scenario\n'

    @groups(SINGLE_GROUP)
    def test_second_scenario(self):
        print 'second scenario\n'

    @groups(SINGLE_GROUP)
    def test_third_scenario(self):
        print 'third scenario\n'

    @groups(SINGLE_GROUP)
    def test_fourth_scenario(self):
        print 'fourth scenario\n'

    @groups(SINGLE_GROUP)
    def test_fifth_scenario(self):
        print 'fifth scenario\n'


class MultipleGroupsTest(unittest.TestCase):
    @groups(A_GROUP, ANOTHER_GROUP)
    def test_sorting_return_results_by_guest_rating(self):
        print 'first scenario from multiple groups tests\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_second_scenario(self):
        print 'second scenario from multiple groups tests\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_third_scenario(self):
        print 'third scenario from multiple groups tests\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_fourth_scenario(self):
        print 'fourth scenario from multiple groups tests\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_fifth_scenario(self):
        print 'fifth scenario from multiple groups tests\n'

    @groups(A_GROUP, ANOTHER_GROUP, EXCLUDED_GROUP)
    def test_sixth_scenario(self):
        print 'sixth scenario from multiple groups tests\n'
