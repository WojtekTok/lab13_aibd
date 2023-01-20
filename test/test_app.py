from app import hello
from app import extract_sentiment
from app import text_contain_word
import app
import pytest


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

test_data3 = [
    ([2, 4, 3, 1, 5], [1, 2, 3, 4, 5]),
    ([1, 7, 2, 4, 4, 10, 14, 167, 13, 5, 4, 2, 9, 20], [1, 2, 2, 4, 4, 4, 5, 7, 9, 10, 13, 14, 20, 167]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (12345, None),
    ((1, 4, 5, 3, 1), None),
    ('Aleksandra', None),
    ({4, 3, 1, 2, 7, 10}, None),
    (['a', 'd', 'b', 'c', 'g', 'z'], ['a', 'b', 'c', 'd', 'g', 'z'])
]

@pytest.mark.parametrize('sample, expected_output', test_data3)
def test_bubbleSort_1(sample, expected_output):

    assert app.bubbleSort(sample) == expected_output