# The Data Format for SemEval 2019, Task 10

Math SAT questions are stored as a sequence of JSON data like the following example:

```
{
  "id": 10846,
  "answer": "E",
  "choices": {
    "A": "24",
    "B": "18",
    "C": "16",
    "D": "14",
    "E": "12"
  },
  "diagramRef": "diagram252.png",
  "exam": "source4",
  "originalQuestionNumber": 18,
  "question": "In the figure above, if the slope of line l is \\(-\\frac{3}{2}\\), what is the area of triangle AOB?",
  "sectionNumber": 2,
  "sectionLength": 20,
  "tags": ["geometry"]
}
```

Here is how to interpret the various fields:
- `id`: A unique integer id for the question. We reserve ids 10000-19999 for training questions, 20000-29999 for development questions, and 30000-39999 for test questions.
- `answer`: The correct answer to the question. This can take several forms:
  - **a multiple choice key**: If the question is multiple choice, then the answer will be the letter ('A' to 'E') corresponding to the correct choice.
  - **a number**: If the question is a direct answer question with a unique answer, then the answer will be the correct numeric answer.
  - **an open interval**, e.g. (3.5, 5). This means the correct answer is greater than 3.5 and less than 5.
  - `a1` **OR** `a2` **OR** ... **OR** `aK`. This means the answer is correct if it satisfies any option `ak` (which may be numbers or open intervals).
- `choices`: If the question is multiple choice, this field provides a map from choice keys to values. Rarely, choice values may be diagram filenames.
- `diagramRef`: If the question has an associated diagram, this field provides its filename.
- `exam`: This encodes the source material from which the question was derived.
- `originalQuestionNumber`: This is the original question number from the exam from which the question was derived. Note that higher numbers are intended to correspond to more difficult questions (at least for humans).
- `question`: The question text. Any mathematical formatting in the source document is encoded with LaTeX.
- `sectionNumber`: The number of the exam section from which the question was derived.
- `sectionLength`: The number of total questions in the exam section from which the question was derived.
- `tags`: Denotes whether the question is `closed` (closed-vocabulary algebra), `open` (open-vocabulary algebra), `geometry` (geometry), or `other` (other).

