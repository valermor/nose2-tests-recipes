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

from time import sleep
import unittest

from src.groups import groups, SINGLE_GROUP, A_GROUP, ANOTHER_GROUP, EXCLUDED_GROUP


WAIT_PERIOD = 2


class SingleGroupTest(unittest.TestCase):

    @groups(SINGLE_GROUP)
    def test_sorting_return_results_by_guest_rating(self):
        sleep(1 * WAIT_PERIOD)
        print 'exiting nose2_test - first scenario\n'

    @groups(SINGLE_GROUP)
    def test_second_scenario(self):
        sleep(2 * WAIT_PERIOD)
        print 'exiting nose2_test - second scenario\n'

    @groups(SINGLE_GROUP)
    def test_third_scenario(self):
        sleep(3 * WAIT_PERIOD)
        print 'exiting nose2_test - third scenario\n'

    @groups(SINGLE_GROUP)
    def test_fourth_scenario(self):
        sleep(4 * WAIT_PERIOD)
        print 'exiting nose2_test - fourth scenario\n'

    @groups(SINGLE_GROUP)
    def test_fifth_scenario(self):
        sleep(5 * WAIT_PERIOD)
        print 'exiting nose2_test - fifth scenario\n'


class MultipleGroupsTest(unittest.TestCase):
    @groups(A_GROUP, ANOTHER_GROUP)
    def test_sorting_return_results_by_guest_rating(self):
        sleep(1 * WAIT_PERIOD)
        print 'exiting nose2_test - first scenario\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_second_scenario(self):
        sleep(2 * WAIT_PERIOD)
        print 'exiting nose2_test - second scenario\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_third_scenario(self):
        sleep(3 * WAIT_PERIOD)
        print 'exiting nose2_test - third scenario\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_fourth_scenario(self):
        sleep(4 * WAIT_PERIOD)
        print 'exiting nose2_test - fourth scenario\n'

    @groups(A_GROUP, ANOTHER_GROUP)
    def test_fifth_scenario(self):
        sleep(5 * WAIT_PERIOD)
        print 'exiting nose2_test - fifth scenario\n'

    @groups(A_GROUP, ANOTHER_GROUP, EXCLUDED_GROUP)
    def test_sixth_scenario(self):
        sleep(6 * WAIT_PERIOD)
        print 'exiting nose2_test - sixth scenario\n'
