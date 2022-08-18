# rubik_data
A Rubik's cube generic data model

## Requirement :
Python 3.10 is needed for dev / testing, pip too

### Install dependencies :
You need to enter the following command before any operations to get packages :

`pip install -r requirements.txt`

## Testing / Quality :

Run this to test :

`pytest `

You can use pylint to control the quality of a specific file :

`pylint ./myfile.py `

If you want to check the typing, use mypy command like this :

`mypy . --strict `

## Next features :

* To create cube's save manager with different file (xml,json,yml,csv,etc...)
* To create a piece manager for the cube
* Work on ClusterCube (a scaning / analysing / storing cube module)
* Using Poetry in a near future
