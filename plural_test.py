import pytest

from plural import plural


@pytest.mark.parametrize(
    'noun, expected',
    [
        ('bass', 'basses'),
        ('fax', 'faxes'),
        ('waltz', 'waltzes'),
        ('coach', 'coaches'),
        ('rash', 'rashes'),
        ('cheetah', 'cheetahs'),
        ('sigh', 'sighs'),
        ('vacancy', 'vacancies'),
        ('boy', 'boys'),
        ('day', 'days'),
        ('agency', 'agencies'),
    ]
)
def test_plural(noun, expected):
    assert plural(noun) == expected


@pytest.mark.parametrize(
    'noun, expected',
    [
        ('leaf', 'leaves'),
        ('loaf', 'loaves'),
        ('dwarf', 'dwarves'),
        ('scarf', 'scarves')
    ]
)
def test_irregular_plural(noun, expected):
    assert plural(noun) == expected
