import pytest
import settings_manager.utils as utils


def test_get_property():
  d = { 'a' : { 'b' : { 'c' : 100 } } }

  res = utils.get_property(d, 'a.b')
  assert res == { 'c' : 100 }

  res = utils.get_property(d, 'a.b.c')
  assert res == 100

def test_get_property_failure():

  d = { 'a' : { 'b' : { 'c' : 100 } } }

  em1 = "Property not found: `a.b.<foobar>` in search path `a.b.foobar`"
  with pytest.raises(Exception, match=em1):
    utils.get_property(d, 'a.b.foobar')

  em1 = "Property not found: `a.<foobar>` in search path `a.foobar.c`"
  with pytest.raises(Exception, match=em1):
    utils.get_property(d, 'a.foobar.c')