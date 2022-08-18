""" tests """
#pylint: disable=invalid-name,consider-using-enumerate,consider-using-dict-items
import copy
import pytest
from cube import Cube, DEFAULT_CUBE_CONFIG
from sticker import Sticker


def test_cube_values() -> None:
    """ test cube object values """
    config = {
            "back": [
                [
                    {
                        "color": "green"
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "up": [
                [
                    {
                        "color": "white"
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "front": [
                [
                    {
                        "color": "blue"
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "left": [
                [
                    {
                        "color": "red"
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "right": [
                [
                    {
                        "color": "orange"
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "down": [
                [
                    {
                        "color": "yellow"
                    } for _ in range(3)
                ] for _ in range(3)
            ]
        }

    faces = {
            "back": [
                [
                    Sticker(DEFAULT_CUBE_CONFIG["back"]) for _ in range(3)
                ] for _ in range(3)
            ],
            "up": [
                [
                    Sticker(DEFAULT_CUBE_CONFIG["down"]) for _ in range(3)
                ] for _ in range(3)
            ],
            "front": [
                [
                    Sticker(DEFAULT_CUBE_CONFIG["front"]) for _ in range(3)
                ] for _ in range(3)
            ],
            "left": [
                [
                    Sticker(DEFAULT_CUBE_CONFIG["right"]) for _ in range(3)
                ] for _ in range(3)
            ],
            "right": [
                [
                    Sticker(DEFAULT_CUBE_CONFIG["left"]) for _ in range(3)
                ] for _ in range(3)
            ],
            "down": [
                [
                    Sticker(DEFAULT_CUBE_CONFIG["up"]) for _ in range(3)
                ] for _ in range(3)
            ],
        }

    cube1 = Cube(3)
    assert cube1 is not None
    assert cube1.size == 3
    assert isinstance(cube1.size, int)
    assert isinstance(cube1.faces, dict)
    for k in cube1.faces:
        assert isinstance(k, str)
        assert k in DEFAULT_CUBE_CONFIG

    cube2 = Cube(3, dico=config)
    assert cube2 is not None
    assert cube2.size == 3
    assert isinstance(cube2.size, int)
    for i in range(cube2.size):
        for j in range(cube2.size):
            for key in cube2.faces:
                assert cube2.faces[key][i][j] is not None
                assert isinstance(cube2.faces[key][i][j], Sticker)
                assert cube2.faces[key][i][j].equals(faces[key][i][j])
    assert cube2.faces is not None
    assert isinstance(cube2.faces, dict)

    with pytest.raises(TypeError):
        Cube("1") # type: ignore
    with pytest.raises(TypeError):
        Cube(3, ["test"]) # type: ignore
    with pytest.raises(ValueError):
        Cube(3, {"test":"foo"})
    with pytest.raises(ValueError):
        Cube(1)

def test_cube_to_dict() -> None:
    """ test to dict method """
    cube_dico = {
        "size": 3,
        "faces": {
            "back":[
                [
                    {
                        "color": "green",
                        "sprite": (0,255,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "up":[
                [
                    {
                        "color": "yellow",
                        "sprite": (255,255,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "front":[
                [
                    {
                        "color": "blue",
                        "sprite": (0,0,255)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "left":[
                [
                    {
                        "color": "orange",
                        "sprite": (255,150,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "right":[
                [
                    {
                        "color": "red",
                        "sprite": (255,0,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "down":[
                [
                    {
                        "color": "white",
                        "sprite": (255,255,255)
                    } for _ in range(3)
                ] for _ in range(3)
            ]
        }
    }

    cube_dict = Cube(3).to_dict()
    assert cube_dict is not None
    assert isinstance(cube_dict, dict)
    assert cube_dict == cube_dico


def test_get_dict_matrix() -> None:
    """ test submethod to_dict """
    matrix = [
        [
            {
                "color": "white",
                "sprite": (255,255,255)
            } for _ in range(3)
        ] for _ in range(3)
    ]

    cube_dict_matrix = Cube(3).get_dict_matrix("down")
    assert cube_dict_matrix is not None
    assert isinstance(cube_dict_matrix, list)
    assert cube_dict_matrix == matrix

def test_get_unical_sticker_matrix() -> None:
    """ test get unical sticker matrix """
    result = [[Sticker("green") for _ in range(3)] for _ in range(3)]
    cube_sticker_matrix = Cube(3).get_unical_sticker_matrix("green")
    for i in range(len(cube_sticker_matrix)):
        for j in range(len(cube_sticker_matrix)):
            assert cube_sticker_matrix[i][j] is not None
            assert isinstance(cube_sticker_matrix[i][j], Sticker)
            assert cube_sticker_matrix[i][j].equals(result[i][j])


def test_get_multi_sticker_matrix() -> None:
    """ test get_multi_sticker_matrix """
    matrix_color = [
        ["white","white","white"],
        ["green","green","green"],
        ["yellow","yellow","yellow"]
    ]

    matrix = [
        [Sticker("white") for _ in range(3)],
        [Sticker("green") for _ in range(3)],
        [Sticker("yellow") for _ in range(3)]
    ]

    cube_sticker_matrix = Cube(3).get_multi_sticker_matrix(matrix_color)
    assert cube_sticker_matrix is not None
    for i in range(len(cube_sticker_matrix)):
        for j in range(len(cube_sticker_matrix)):
            assert cube_sticker_matrix[i][j] is not None
            assert isinstance(cube_sticker_matrix[i][j], Sticker)
            assert cube_sticker_matrix[i][j].equals(matrix[i][j])
    assert isinstance(cube_sticker_matrix, list)

def test_validate_dict_param() -> None:
    """ test validate_dict_param """
    dico = {
        "back": [
            [
                {
                    "color": "green"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "up": [
            [
                {
                    "color": "yellow"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "front": [
            [
                {
                    "color": "blue"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "left": [
            [
                {
                    "color": "orange"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "right": [
            [
                {
                    "color": "red"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "down": [
            [
                {
                    "color": "white"
                } for _ in range(3)
            ] for _ in range(3)
        ],
    }
    dico2 = copy.deepcopy(dico)
    dico3 = copy.deepcopy(dico)

    test = Cube(3).validate_dict_param(dico)
    assert test

    dico2["back"].pop()
    test2 = Cube(3).validate_dict_param(dico2)
    assert not test2

    dico3["back"][0].pop()
    test3 = Cube(3).validate_dict_param(dico3)
    assert not test3

def test_get_dict_stickers_values() -> None:
    """ test get_dict_stickers_values """
    dico = {
        "back": [
            [
                {
                    "color": "green"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "up": [
            [
                {
                    "color": "yellow"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "front": [
            [
                {
                    "color": "blue"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "left": [
            [
                {
                    "color": "orange"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "right": [
            [
                {
                    "color": "red"
                } for _ in range(3)
            ] for _ in range(3)
        ],
        "down": [
            [
                {
                    "color": "white"
                } for _ in range(3)
            ] for _ in range(3)
        ],
    }
    dico2 = copy.deepcopy(dico)
    dico2["test"] = ["here","some","failing"] # type: ignore

    dico_cube = Cube(3).get_dict_stickers_values(dico)
    for k in dico_cube:
        for i in range(len(dico_cube[k])):
            for j in range(len(dico_cube[k][i])):
                assert dico_cube[k][i][j] is not None
                assert isinstance(dico_cube[k][i][j], Sticker)
                assert dico_cube[k][i][j].equals(Sticker(DEFAULT_CUBE_CONFIG[k]))
    with pytest.raises(ValueError):
        Cube(3).get_dict_stickers_values(dico2)

def test_to_dict() -> None:
    """ test to_dict """
    dico = {
        "size": 3,
        "faces": {
            "back": [
                [
                    {
                        "color": "green",
                        "sprite": (0,255,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "up": [
                [
                    {
                        "color": "yellow",
                        "sprite": (255,255,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "front": [
                [
                    {
                        "color": "blue",
                        "sprite": (0,0,255)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "left": [
                [
                    {
                        "color": "orange",
                        "sprite": (255,150,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "right": [
                [
                    {
                        "color": "red",
                        "sprite": (255,0,0)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
            "down": [
                [
                    {
                        "color": "white",
                        "sprite": (255,255,255)
                    } for _ in range(3)
                ] for _ in range(3)
            ],
        }
    }

    dico_cube = Cube(3).to_dict()
    assert dico_cube is not None
    assert dico_cube == dico
    assert isinstance(dico_cube, dict)
