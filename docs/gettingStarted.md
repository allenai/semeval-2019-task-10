# Getting Started with SemEval 2019, Task 10

The following is a quickstart guide for Task 10:
1. Fork the Task 10 repository: <https://github.com/allenai/semeval-2019-task-10>
2. The available datasets are in the repo directory (the file format is described [here](https://github.com/allenai/semeval-2019-task-10/blob/master/docs/dataFormat.md)):
  - Training data: `data/sat.train.json`
  - Training diagrams: `data/diagrams/diagrams.train.tar.gz`
  - Development data: `data/sat.dev.json`
  - Development diagrams: `data/diagrams/diagrams.dev.tar.gz`
3. Create a program that can take `data/sat.dev.json` as input and output a list of JSON datum `{ id: <id>, response: "<response>"}`, where `<id>` is the integer index of a question and `<response>` is the guessed response (either a choice key or a numeric string). An example program is provided in the repo at `baselines/guesser.py`. Run `python baselines/guesser.py data/sat.dev.json answer.json b-guesser`. This program will guess "B" for every multiple choice question (and abstain from direct answer questions). The output is stored in `answer.json'.
4. Create a CodaLab submission file:
```
zip submission.zip answer.json 
```
5. Submit the file to the Task 10 Codalab competition by:
  - Going to the Participate tab.
  - Going to the Submit/View Results submenu.
  - Clicking the Submit button to upload a new result.
  - Finding submission.zip in your local directory structure and uploading it.
  
6. You can then wait until the status of your submission says Completed (you will likely need to click the Refresh Status button or refresh your browser to force a status change).
7. Your scores should become visible and you are given the option to submit your result to the leaderboard.



  
