import pytest

from plurals import plural


@pytest.mark.parametrize(
    'noun, expected',
    [
        ('bass', 'basses'),
        ('fax', 'faxes'),
        ('waltz', 'waltzes'),
    ]
)
def test_rule_1(noun, expected):
    assert plural(noun) == expected


@pytest.mark.parametrize(
    'noun, expected',
    [
        ('coach', 'coaches'),
        ('rash', 'rashes'),
        ('cheetah', 'cheetahs'),
        ('sigh', 'sighs'),
    ]
)
def test_rule_2(noun, expected):
    assert plural(noun) == expected


@pytest.mark.parametrize(
    'noun, expected',
    [
        ('lullaby', 'lullabies'),
        ('agency', 'agencies'),
        ('blasphemy', 'blasphemies'),
        ('lorry', 'lorries'),
        ('day', 'days'),
        ('prey', 'preys'),
        ('boy', 'boys'),
    ]
)
def test_rule_3(noun, expected):
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
def test_rule_4(noun, expected):
    assert plural(noun) == expected


@pytest.mark.parametrize(
    'noun, expected',
    [
        ('fat guy', 'fat guys'),
        ('open the black box', 'open the black boxes'),
        ('come on, baby', 'come on, babies'),
    ]
)
def test_multi_word(noun, expected):
    assert plural(noun) == expected
