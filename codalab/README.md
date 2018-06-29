# semeval2019-task10

## Task 10: Math Question Answering
## Organizers: Mark Hopkins, Ronan Le Bras, Cristian Petrescu-Prahova, Gabriel Stanovsky (Allen Institute for Artificial Intelligence), Hannaneh Hajishirzi, Rik Koncel-Kedziorski (University of Washington)

Note: This is a preliminary page, intended to provide information to SemEval 2018 attendees about SemEval 2019 Task 10. In the coming weeks, we will be adding more concrete dates and information. In the meantime, please join semeval-2019-task-10@googlegroups.com to keep abreast of task updates.

Over the past four years, there has been a surge of interest in math question answering. In this SemEval task, we provide the opportunity for math QA systems to test themselves against a benchmark designed to evaluate high school students: The Math SAT (short for Scholastic Achievement Test).

The training and test data consists of unabridged practice exams from various study guides, for the (now retired) exam format administered from 2005 to 2016. We have tagged questions into three broad categories:

Closed-vocabulary algebra, e.g. "Suppose 3x + y = 15, where x is a positive integer. What is the difference between the largest possible value of y and the smallest possible value of x, assuming that y is also a positive integer?"
Open-vocabulary algebra, e.g. "At a basketball tournament involving 8 teams, each team played 4 games with each of the other teams. How many games were played at this tournament?"
Geometry, e.g. "The lengths of two sides of a triangle are (x-2) and (x+2), where x > 2. Which of the following ranges includes all and only the possible values of the third side y?"
A majority of the questions are 5-way multiple choice, and a minority have a numeric answer. Only the Geometry subset contains diagrams.

We are planning to provide 3000-4000 training questions, and a test set of over 1000 questions. Questions are stored as JSON, using LaTeX to encode mathematical formatting.

```
{
  "id": 846,
  "exam": "Kaplan Test Prep Practice Test 9",
  "sectionNumber": 2,
  "sectionLength": 20,
  "originalQuestionNumber": 18,
  "question": "In the figure above, if the slope of line l is \\(-\\frac{3}{2}\\), what is the area of triangle AOB?",
  "answer": "E",
  "choices": {
    "E": "12",
    "A": "24",
    "B": "18",
    "C": "16",
    "D": "14"
  },
  "diagramRef": "Kaplan_Test9_5.png",
  "tags": ["geometry"]
}
```

Additionally, we will provide gold logical forms for a majority of the training questions in the Closed Algebra track. These logical forms are the same language used in the paper: 

Hopkins, M., Petrescu-Prahova, C., Levin, R., Le Bras, R., Herrasti, A., & Joshi, V. (2017). Beyond sentential semantic parsing: Tackling the math sat with a cascade of tree transducers. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (pp. 795-804).

We will also be providing documentation and an interpreter for the logical form language. Competitors are free to ignore the provided logical forms if desired. Evaluation will be based solely on a system's ability to answer questions correctly. Competitors will also be free to use additional publicly available math training questions, like AQuA or MAWPS; we ask only that competitors refrain from using additional Math SAT questions found on the web or elsewhere, to avoid potential train/test overlap.