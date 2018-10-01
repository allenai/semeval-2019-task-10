# Getting Started with the _Logical Form Interpreter_ for SemEval 2019, Task 10

We provide a python script (`run_interpreter.py`) to run the interpreter on a list of logical forms.
The command to run the script is as follows:  
```
python run_interpreter.py data/goldLogicalForms_ex.json responses_ex.json
```
where:
- `data/goldLogicalForms_closedAlgebra.json` is a `json` file containing the input logical forms.
- `responses_closedAlgebra.json` is the file that will contain the output of the interpreter.

Here is an example of input logical forms (as described [here](https://github.com/allenai/semeval-2019-task-10-internal/blob/master/docs/logicalFormLanguage.md)):
```
[
    {
        "id": 10000,
        "logicalForm": [
            "(assert (Strategy \"CheckUnsatisfiable\"))",
            "(assert (= (- a 5) 0))",
            "(assert (Not (= ?_id_7_8 (+ a 5))))",
            "(assert (MenuItem \"A\" (- 0 10)))",
            "(assert (MenuItem \"B\" (- 0 5)))",
            "(assert (MenuItem \"C\" 0))",
            "(assert (MenuItem \"D\" 5))",
            "(assert (MenuItem \"E\" 10))"
        ]
    },
    {
        "id": 10011,
        "logicalForm": [
            "(assert (Strategy \"CheckUnsatisfiable\"))",
            "(assert (= 14 (+ x (* 2 y))))",
            "(assert (= _id_22_26 x))",
            "(assert (= y (+ z 2)))",
            "(assert (= z 4))",
            "(assert (Not (= ?_id_20_21 _id_22_26)))",
            "(assert (MenuItem \"A\" 2))",
            "(assert (MenuItem \"B\" 4))",
            "(assert (MenuItem \"C\" 6))",
            "(assert (MenuItem \"D\" 8))",
            "(assert (MenuItem \"E\" 10))"
        ]
    }
]
```

Given this input file, the output file (`responses_ex.json`) should contain:
```
[
    {
        "id": 10000,
        "response": "ChoiceResponse(E)"
    },
    {
        "id": 10011,
        "response": "ChoiceResponse(A)"
    }
]
```

NOTE: You need to install and run `Docker` before running the _Logical Form Interpreter_.
For more information, please visit: [https://www.docker.com/get-started](https://www.docker.com/get-started).

