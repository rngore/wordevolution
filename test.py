import pytest
from main import genword, similarity, generate_population, get_average_similarity, reproduce, char


def test_genword():
    word = genword(10)

    assert len(word) == 10
    assert all(letter in char for letter in word)


def test_similarity():
    assert similarity("HELLO", "HELLO") == 5
    assert similarity("HELLO", "HEYYY") == 2
    assert similarity("ABCDE", "FGHIJ") == 0


def test_generate_population():
    population = generate_population(100, "HELLO")

    assert len(population) == 100
    assert all(len(word) == 5 for word in population)
    assert all(all(letter in char for letter in word) for word in population)


def test_get_average_similarity():
    population = ["HELLO", "HEXXO", "XXXXX"]

    average = get_average_similarity(population, "HELLO")

    assert average == pytest.approx(2.6666666667)


def test_reproduce():
    elites = ["HELLO", "WORLD"]

    population = reproduce(elites, 50, 0)

    assert len(population) == 50
    assert all(word in elites for word in population)


def test_reproduce_with_full_mutation():
    elites = ["AAAAA"]

    population = reproduce(elites, 20, 1)

    assert len(population) == 20
    assert all(len(word) == 5 for word in population)
    assert all(all(letter in char for letter in word) for word in population)


def test_similarity_with_spaces():
    assert similarity("HI YOU", "HI YOU") == 6
    assert similarity("HI YOU", "HI ALL") == 3


def test_genword_zero_length():
    assert genword(0) == ""


def test_generate_population_empty_target():
    population = generate_population(5, "")

    assert len(population) == 5
    assert all(word == "" for word in population)
