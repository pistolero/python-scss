#   Copyright 2012 Sergey Kirillov
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import sass
from nose.tools import eq_, assert_equal, raises

@raises(sass.CompileError)
def test1():
	result = sass.compile_string(b'asd', '', sass.SASS_STYLE_NESTED)
	eq_(result, b'asd')


def test2():
	result = sass.compile_string(b'''table.hl {
  margin: 2em 0;
  td.ln {
    text-align: right;
  }
}

li {
  font: {
    family: serif;
    weight: bold;
    size: 1.2em;
  }
}''', '', sass.SASS_STYLE_NESTED)

	expected = b'''table.hl {
  margin: 2em 0; }
  table.hl td.ln {
    text-align: right; }

li {
  font-family: serif;
  font-weight: bold;
  font-size: 1.2em; }
'''

	assert_equal(result, expected)
