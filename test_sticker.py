""" tests """
#pylint: disable=invalid-name
import pytest
from sticker import Sticker

def test_sticker_value() -> None:
    """ tests values """
    stick = Sticker("white")
    assert stick.color == "white"
    assert stick.sprite == (255,255,255)
    assert isinstance(stick.color, str)
    assert isinstance(stick.sprite, tuple)

def test_sticker_to_dict() -> None:
    """ tests to dict func """
    stick_dict = Sticker("white").to_dict()
    assert stick_dict == {
        "color": "white",
        "sprite": (255,255,255)
    }
    assert isinstance(stick_dict, dict)
    for k,v in stick_dict.items():
        assert isinstance(k, str)
        assert isinstance(v, (str, tuple))

def test_sticker_dict_to_instance() -> None:
    """ test generate instance from dict """
    dico = {
        "color": "white",
        "sprite": [255,255,255]
    }

    stick_inst = Sticker().dict_to_instance(dico)
    assert stick_inst.color == "white"
    assert stick_inst.sprite == (255,255,255)
    assert isinstance(stick_inst.color, str)
    assert isinstance(stick_inst.sprite, tuple)

    dico2 = {
        "tyty": "white"
    }

    with pytest.raises(ValueError):
        Sticker().dict_to_instance(dico2)
