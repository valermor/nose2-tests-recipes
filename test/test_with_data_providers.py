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
from nose2.tools import params
from src.data_providers import odd_configs_data_provider, even_configs_data_provider
from src.groups import DATA_PROVIDER, groups


class ConcurrencyTest(unittest.TestCase):

    @groups(DATA_PROVIDER)
    @params(*odd_configs_data_provider)
    def test_odd_configs(self, config):
        print 'Running {n}: '.format(n=config.name)
        print 'Config says: {say}, '.format(say=config.value)
        print 'number #{num}\n'.format(num=config.number)

    @groups(DATA_PROVIDER)
    @params(*even_configs_data_provider)
    def test_even_configs(self, config):
        print 'Running {n}: '.format(n=config.name)
        print 'Config says: {say}, '.format(say=config.value)
        print 'number #{num}\n'.format(num=config.number)
