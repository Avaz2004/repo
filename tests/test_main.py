from main import get_name, get_directory, documents, directories, vote, add, solution
import pytest


class TestPytest():
    def test_get_name(self):
        assert get_name("2207 876234") == "Василий Гупкин"

    def test_get_directory(self):
        assert get_directory("2207 876234") == '1'

    def test_add(self):
        add('passport', '5620 784', 'Павел Петрович', 3)
        assert documents[4]['type'] == 'passport'
        assert documents[4]['number'] == '5620 784'
        assert documents[4]['name'] == 'Павел Петрович'
        assert directories['3'] == ['5620 784']

    @pytest.mark.parametrize('a, b, c, result', [
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (1, 1, 1, 'корней нет'),
    ])

    def test_solution(self, a, b, c, result):
        assert solution(a, b, c) == result

    @pytest.mark.parametrize('votes, max_vote', [
        ([1, 1, 1, 2, 3], 1),
        ([1, 2, 3, 2, 2], 2)
    ])

    def test_vote(self, votes: list, max_vote):
        assert vote(votes) == max_vote