# EDA_repo
This repo is a sandbox for exploratory data analysis functions. 

The exemple data has the following format.
- Normal dist on column normal.
- Categorical in the categorical column, and
- Continuous in the continuous column.

|     normal | categories   |   continuous |
|-----------:|:-------------|-------------:|
|   1.18967  | a            |            1 |
|   0.689035 | b            |            2 |
| nan        | --           |            3 |
|   0.599741 | nan          |            4 |
|  -0.605406 | c            |          nan |
|  -1.09387  | a            |            6 |
| nan        | a            |            7 |
|  -0.768324 | c            |          nan |
|  -0.396219 | a            |            9 |
|  -0.914014 | nan          |           10 |

Notice that we are missing info, and missleading information ('--').

The exemple data set cover at least the following edge cases.
- Normal is missing 2 values, in this case expresed as nan.
- Categories missing 3 values, two of them are nan and the third one "--".
- Continuous is missing 2 values.





