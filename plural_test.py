import pytest

from plural import plural


@pytest.mark.parametrize('input_noun, expected', [('bass', 'basses'),
                                                  ('fax', 'faxes'),
                                                  ('waltz', 'waltzes'),
                                                  ('coach', 'coaches'),
                                                  ('rash', 'rashes'),
                                                  ('cheetah', 'cheetahs'),
                                                  ('vacancy', 'vacancies'),
                                                  ('boy', 'boys'),
                                                  ('day', 'days'),
                                                  ('agency', 'agencies')])
def test_plural(input_noun, expected):
    assert plural(input_noun) == expected
