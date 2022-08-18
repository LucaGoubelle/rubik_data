""" sticker module class """

from typing import Any, Dict

COLORS = {
    "white": (255,255,255),
    "yellow": (255,255,0),
    "blue": (0,0,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "orange": (255,150,0),
    "default": (32,32,32)
}

class Sticker:
    """ Sticker object """

    def __init__(self, color: str = "") -> None:
        self.color = color if color in COLORS else "default"
        self.sprite = COLORS[color] if color in COLORS else COLORS["default"]

    def equals(self, other: object) -> bool:
        """ equals """
        return self.color == other.color and self.sprite == other.sprite # type: ignore


    def to_dict(self) -> Dict[str, Any]:
        """ to dict object """
        return {
            "color": self.color,
            "sprite": self.sprite
        }

    def dict_to_instance(self, dico: Dict[str,Any]) -> Any:
        """ return instance from dict """
        try:
            if "color" not in dico:
                raise ValueError("No key \"color\" in dict")
            return Sticker(dico["color"])
        except ValueError as error:
            print(f"{error}")
            raise ValueError from error
