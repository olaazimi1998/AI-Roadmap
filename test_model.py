import pytest

from model import HousePriceModel


def test_predict_price():
    model = HousePriceModel()

    result = model.predict(100)

    assert result == 100000


def test_predict_larger_house():
    model = HousePriceModel()

    result = model.predict(200)

    assert result == 200000


def test_zero_size_raises_error():
    model = HousePriceModel()

    with pytest.raises(ValueError):
        model.predict(0)