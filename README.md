## SemEval 2019, Task 10: Math Question Answering

### Organizers

Mark Hopkins, Ronan Le Bras, Cristian Petrescu-Prahova, Gabriel Stanovsky (Allen Institute for Artificial Intelligence), Hannaneh Hajishirzi, Rik Koncel-Kedziorski (University of Washington)

### Mailing List
semeval-2019-task-10@googlegroups.com 

### Key Dates
- 20 Aug 2018: CodaLab competition website ready and made public. Should include basic task description and mailing group information for the task. Trial data ready. Evaluation script ready for participants to download and run on the trial data.
- 17 Sep 2018: Training data ready. Development data ready. CodaLab competition website updated to include an evaluation script uploaded as part of the competition so that participants can upload submissions on the development set and the script immediately checks the submission for format and computes the results on the development set. This is also the date by which a benchmark system should be made available to participants. Also, the organizers should run the submission created with the benchmark system on CodaLab, so that participants can see its results on the LeaderBoard.
- 10 Jan 2019: Evaluation start
- 24 Jan 2019: Evaluation end
- 05 Feb 2019: Results posted
- 28 Feb 2019: System and Task description paper submissions due by 23:59 GMT -12:00
- 14 Mar 2019: Paper reviews due (for both systems and tasks)
- 06 Apr 2019: Author notifications
- 20 Apr 2019: Camera ready submissions due
- Summer 2019: SemEval 2019

### Quickstart
Go [here](https://github.com/allenai/semeval-2019-task-10/blob/master/docs/gettingStarted.md) to get started.

### Task Overview

Over the past four years, there has been a surge of interest in math question answering. In this SemEval task, we provide the opportunity for math QA systems to test themselves against a benchmark designed to evaluate high school students: The Math SAT (short for Scholastic Achievement Test).

The training and test data consists of unabridged practice exams from various study guides, for the (now retired) exam format administered from 2005 to 2016. We have tagged questions into three broad categories:
- Closed-vocabulary algebra, e.g. "Suppose 3x + y = 15, where x is a positive integer. What is the difference between the largest possible value of y and the smallest possible value of x, assuming that y is also a positive integer?"
- Open-vocabulary algebra, e.g. "At a basketball tournament involving 8 teams, each team played 4 games with each of the other teams. How many games were played at this tournament?"
- Geometry, e.g. "The lengths of two sides of a triangle are (x-2) and (x+2), where x > 2. Which of the following ranges includes all and only the possible values of the third side y?"

A majority of the questions are 5-way multiple choice, and a minority have a numeric answer. Only the Geometry subset contains diagrams.

### Provided Datasets

We will provide over 2500 training questions, 500 development questions, and 1000 test questions, all derived from Math SAT study guides. Questions are stored as JSON, using LaTeX to encode mathematical formatting.

```
{
  "id": 846,
  "exam": "source4",
  "sectionNumber": 2,
  "sectionLength": 20,
  "originalQuestionNumber": 18,
  "question": "In the figure above, if the slope of line l is \\(-\\frac{3}{2}\\), what is the area of triangle AOB?",
  "answer": "E",
  "choices": {
    "A": "24",
    "B": "18",
    "C": "16",
    "D": "14",
    "E": "12"
  },
  "diagramRef": "diagram252.png",
  "tags": ["geometry"]
}
```

For more details on the JSON data format, please visit [this page](https://github.com/allenai/semeval2019-task10/blob/master/docs/dataFormat.md).

### Gold Logical Forms

Additionally, we will provide gold logical forms for a majority of the training questions in the Closed Algebra track. These logical forms are the same language used in the paper: 

Hopkins, M., Petrescu-Prahova, C., Levin, R., Le Bras, R., Herrasti, A., & Joshi, V. (2017). Beyond sentential semantic parsing: Tackling the math sat with a cascade of tree transducers. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (pp. 795-804). [(pdf)](https://pdfs.semanticscholar.org/c22a/240d1087603664826e9aab809273ed9bff15.pdf?_ga=2.52187753.1130679049.1530133172-566539276.1446829155&_gac=1.6555398.1527028246.EAIaIQobChMI9YuywK-a2wIVlcBkCh0WKw_kEAAYASAAEgKwgPD_BwE)

The logical form language is described [here](https://github.com/allenai/semeval2019-task10/blob/master/docs/logicalFormLanguage.md).
Competitors are free to ignore the provided logical forms if desired. Evaluation will be based solely on a system's ability to answer questions correctly. Competitors will also be free to use additional publicly available math training questions, like AQuA or MAWPS; we ask only that competitors refrain from using additional Math SAT questions found on the web or elsewhere, to avoid potential train/test overlap.

### Evaluation

Evaluation will be based solely on a system's ability to answer questions correctly.

For each subtask, the main evaluation metric will simply be question accuracy, i.e. the number of correctly answered questions. The evaluation script takes as input a list of JSON datum { id: \<id\>, response: "\<response\>"}, where \<id\> is the integer index of a question and \<response\> is the guessed response (either a choice key or a numeric string). It will output the system’s score as the number of correct responses divided by the total number of questions in the subtask.

While the main evaluation metric includes no penalties for guessing, we will also compute a secondary metric called penalized accuracy that implements the actual evaluation metric used to score these SATs. This metric is the number of correct questions, minus 1/4 point for each incorrect guess. We include this metric to challenge participants to investigate high-precision QA systems.

### Terms and Conditions

By submitting results to this competition, you consent to the public release of your scores at the SemEval-2018 workshop and in the associated proceedings, at the task organizers' discretion. Scores may include, but are not limited to, automatic and manual quantitative judgments, qualitative judgments, and such other metrics at the task organizers' discretion. You accept that the ultimate decision of metric choice and score value is that of the task organizers. You further agree that the task organizers are under no obligation to release scores and that scores may be withheld if it is the task organizers' judgment that the submission was incomplete, erroneous, deceptive, or violated the letter or spirit of the competition's rules. Inclusion of a submission's scores is not an endorsement of a team or individual's submission, system, or science.

You further agree that your system may be named according to the team name provided at the time of submission, or to a suitable shorthand as determined by the task organizers. You agree to respect the following statements about the dataset:

AI2 makes no warranties regarding the Dataset, including but not limited to being up-to- date, correct or complete. AI2 cannot be held liable for providing access to the Dataset or usage of the Dataset.
The Dataset should only be used for scientific or research purposes related to this competition. Any other use is explicitly prohibited.
You take full responsibility for usage of the Dataset at any time.
AI2 reserves the right to terminate your access to the Dataset at any time.
The Dataset is distributed under "fair use". Copyright will remain with the owners of the content. We will remove data upon request from a copyright owner.
