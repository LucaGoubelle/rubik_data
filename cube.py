""" cube module class """
#pylint: disable=invalid-name
from typing import Any, Dict, List, Optional
from sticker import Sticker

DEFAULT_CUBE_CONFIG = {
    "back": "green",
    "up": "yellow",
    "front": "blue",
    "left": "orange",
    "right": "red",
    "down": "white"
}

class Cube:
    """ Cube object """

    def __init__(self, size: int, dico: Optional[Dict[str, Any]] = None) -> None:
        try:
            if not isinstance(size, int):
                raise TypeError("size must be 'int' type")
            if size<=1:
                raise ValueError("size must be 'int' > 1")
            self.size = size
            if not isinstance(dico, dict | None):
                raise TypeError("dico must be a dict")
            if not self.validate_dict_param(dico):
                raise ValueError(
                    "matrix in dict had wrong size, expected self.size value"
                )
            self.faces = self.get_dict_stickers_values(
                dico
            ) if dico else self.get_default_config()
        except (TypeError,ValueError) as error:
            print(f"{error}")
            raise error

    def get_default_config(self) -> Dict[str, List[List[Sticker]]]:
        """ get default config """
        return {
            "back":self.get_unical_sticker_matrix(DEFAULT_CUBE_CONFIG["back"]),
            "up":self.get_unical_sticker_matrix(DEFAULT_CUBE_CONFIG["up"]),
            "front":self.get_unical_sticker_matrix(DEFAULT_CUBE_CONFIG["front"]),
            "left":self.get_unical_sticker_matrix(DEFAULT_CUBE_CONFIG["left"]),
            "right":self.get_unical_sticker_matrix(DEFAULT_CUBE_CONFIG["right"]),
            "down":self.get_unical_sticker_matrix(DEFAULT_CUBE_CONFIG["down"])
        }

    def get_unical_sticker_matrix(self, color: str) -> List[List[Sticker]]:
        """ get sticker matrix """
        return [
            [
                Sticker(color) for _ in range(self.size)
            ] for _ in range(self.size)
        ]

    def get_multi_sticker_matrix(
        self,
        colors: List[List[str]]
    ) -> List[List[Sticker]]:
        """ get heterogenic sticker matrix"""
        return [
            [
                Sticker(colors[i][j]) for j in range(len(colors[i]))
            ] for i in range(len(colors))
        ]

    def get_dict_matrix(self, key: str) -> List[List[Dict[str, Any]]]:
        """ get dict matrix """
        return [
            [
                stick.to_dict() for stick in self.faces[key][i]
                ] for i in range(self.size)
        ]

    def to_dict(self) -> Dict[str, Any]:
        """ to dict object """
        return {
            "size": self.size,
            "faces": {
                "back": self.get_dict_matrix("back"),
                "up": self.get_dict_matrix("up"),
                "front": self.get_dict_matrix("front"),
                "left": self.get_dict_matrix("left"),
                "right": self.get_dict_matrix("right"),
                "down": self.get_dict_matrix("down")
            }
        }

    def get_colors_matrix(self, dico: Dict[str, Any], key: str) -> List[List[str]]:
        """ get str color matrix """
        return [
            [
                dico[key][i][j]["color"] for j in range(len(dico[key][i]))
            ] for i in range(len(dico[key]))
        ]

    def get_dict_stickers_values(
        self,
        dico: Dict[str, Any]
    ) -> Dict[str, List[List[Sticker]]]:
        """ to instance object """
        try:
            for k in dico:
                if k not in DEFAULT_CUBE_CONFIG:
                    raise ValueError(f"unvalid key '{k}'")
            return {
                "back": self.get_multi_sticker_matrix(
                    self.get_colors_matrix(dico,"back")
                ),
                "up": self.get_multi_sticker_matrix(
                    self.get_colors_matrix(dico,"up")
                ),
                "front": self.get_multi_sticker_matrix(
                    self.get_colors_matrix(dico,"front")
                ),
                "left": self.get_multi_sticker_matrix(
                    self.get_colors_matrix(dico,"left")
                ),
                "right": self.get_multi_sticker_matrix(
                    self.get_colors_matrix(dico,"right")
                ),
                "down": self.get_multi_sticker_matrix(
                    self.get_colors_matrix(dico,"down")
                ),
            }
        except ValueError as error:
            print(f"{error}")
            raise ValueError from error

    def validate_dict_param(self, dico: Optional[Dict[str, Any]]) -> bool:
        """ validate dict structure"""
        if dico:
            for _,v in dico.items():
                if len(v) != self.size:
                    return False
                for row in v:
                    if len(row) != self.size:
                        return False
        return True
