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

class TestConfig(object):
    """
    Class storing configuration values for the tests.
    """
    def __init__(self, name, value, number):
        super(TestConfig, self).__init__()
        self.name = name
        self.value = value
        self.number = number


FIRST_TEST_CONFIG = TestConfig('config #1', 'this is the first configuration', 1)
SECOND_TEST_CONFIG = TestConfig('config #2', 'this is the second configuration', 2)
THIRD_TEST_CONFIG = TestConfig('config #3', 'this is the third configuration', 3)
FOURTH_TEST_CONFIG = TestConfig('config #4', 'this is the fourth configuration', 4)
FIFTH_TEST_CONFIG = TestConfig('config #5', 'this is the fifth configuration', 5)

all_configs = [FIRST_TEST_CONFIG, SECOND_TEST_CONFIG, THIRD_TEST_CONFIG, FOURTH_TEST_CONFIG, FIFTH_TEST_CONFIG]

odd_configs_data_provider = tuple(filter(lambda x: (x.number % 2) == 1, all_configs))
even_configs_data_provider = tuple(filter(lambda x: (x.number % 2) == 0, all_configs))
