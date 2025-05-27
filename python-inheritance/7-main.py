[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
>>> bg = BaseGeometry()
>>> bg.integer_validator("name", "Jean")
Traceback (most recent call last):
    ...
TypeError: name must be an integer

>>> bg.integer_validator("age", 0)
Traceback (most recent call last):
    ...
ValueError: age must be greater than 0

>>> bg.integer_validator("distance", -4)
Traceback (most recent call last):
    ...
ValueError: distance must be greater than 0