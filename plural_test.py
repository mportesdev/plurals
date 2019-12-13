import pytest

from plural import plural


@pytest.mark.parametrize('input, expected',
                         [
                             ('bass', 'basses'),
                             ('fax', 'faxes'),
                             ('vacancy', 'vacancies'),
                             ('boy', 'boys'),
                             ('day', 'days'),
                             ('agency', 'agencies'),
                         ])
def test_plural(input, expected):
    assert plural(input) == expected
