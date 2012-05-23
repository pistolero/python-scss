import sass
from nose.tools import eq_, assert_equal, raises

@raises(sass.CompileError)
def test1():
	result = sass.compile_string('asd', '', sass.SASS_STYLE_NESTED)
	eq_(result, 'asd')


def test2():
	result = sass.compile_string('''table.hl {
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

	expected = '''table.hl {
  margin: 2em 0; }
  table.hl td.ln {
    text-align: right; }

li {
  font-family: serif;
  font-weight: bold;
  font-size: 1.2em; }
'''

	assert_equal(result, expected)