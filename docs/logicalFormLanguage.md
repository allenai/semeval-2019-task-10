# The Logical Form Language for SemEval 2019, Task 10

In this task, we provide gold logical form annotations (and an interpreter) for a majority of the
closed algebra training questions. This document provides a tutorial for the logical form
language.

### A simple example

The following program encodes the question ``If 9^r = 27^{r - 1}, then what is r?"

```
(assert (Strategy "DirectSolution"))
(assert (= (Pow 9 r) (Pow 27 (- r 1))))
(assert (= ?_id_0 r))
```

There are two key elements of this program. 

The first is the **query variable**, designated by a
"?"-prefix. In this case, the query variable is `?_id_0`. The interpreter's job is to provide a
satisfying value for the query variable.

The second is the **strategy**, which tells the interpreter
 how to provide a value for the query variable. In this case, the strategy is the simplest one -- 
 "DirectSolution" -- which tells the interpreter that the query variable has a numeric
 answer. Thus when we run this program, the result should assign a
  number to the query variable.
  
  
### A multiple choice example

The following program encodes the multiple choice question ``If 4x + 2 = 26, then what is 4x + 8? 
(A) 32, (B) 34, (C) 36, (D) 38, (E) 40":

```
(assert (Strategy "CheckUnsatisfiable"))
(assert (= 26 (+ (* 4 x) 2)))
(assert (Not (= (+ (* 4 x) 8) ?_id_0)))
(assert (MenuItem "A" 32))
(assert (MenuItem "B" 34))
(assert (MenuItem "C" 36))
(assert (MenuItem "D" 38))
(assert (MenuItem "E" 40))
```

In the "CheckUnsatisfiable" strategy, each **menu item** corresponds to
 a program, obtained by substituting the item's value for
the query variable. For example, the program corresponding to menu item B is:

```
(assert (Strategy "CheckUnsatisfiable"))
(assert (= 26 (+ (* 4 x) 2)))
(assert (Not (= (+ (* 4 x) 8) 34)))
```

If the program corresponding to menu item M is the only unsatisfiable one, then
the interpreter should respond with M's key. Otherwise, the interpreter should abstain from
responding.

The "CheckSatisfiable" strategy is analogous, but specifies that the interpreter
should respond with M's key, if the program corresponding to menu item M is the only satisfiable 
one.


### "Combo meal" questions

The Math SAT also features more complicated multiple choice questions, like: 

>If p < q, r < s, and r < q, which of the following must be true? 
>I. p < s II. s < q III. r < p
>>(A) None
>>(B) I only
>>(C) III only
>>(D) I and II
>>(E) II and III

We call these "combo meal" questions, using the metaphor of a menu (e.g., keys I, II, and III) 
from which we create several combo meals (e.g. keys A through E). The above question
can be formulated as follows:

```
(assert (Strategy "CheckUnsatisfiable"))
(assert (< p q))
(assert (< r q))
(assert (< r s))
(assert (Not ?_id_14_18))
(assert (MenuItem "I" (< p s)))
(assert (MenuItem "II" (< s q)))
(assert (MenuItem "III" (< r p)))
(assert (ComboItem "A" "noneOfTheAbove"))
(assert (ComboItem "B" "I"))
(assert (ComboItem "C" "III"))
(assert (ComboItem "D" "I"))
(assert (ComboItem "D" "II"))
(assert (ComboItem "E" "II"))
(assert (ComboItem "E" "III"))
```

Note that the directive `(assert (ComboItem "D" "I")` states that menu item
`I` is a member of combo meal `D`. The keyword `noneOfTheAbove` states that a
particular combo meal is an empty set.


### Function Signatures




##### (= x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Boolean`

Returns whether x and y are equal.

##### (< x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Boolean`

Returns whether x is less than y.

##### (+ x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Numeric`

Returns the sum of x and y.

##### (- x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Numeric`

Returns x minus y.

##### (* x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Numeric`

Returns the product of x and y.

##### (/ x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Numeric`

Returns the (floating-point) division of x by y.

##### (Pow x y)
- `x`: `Numeric`
- `y`: `Numeric`
- return value: `Numeric`

Returns x to the power of y.


##### (Abs n)

- `n`: `Numeric`
- return value: `Numeric`

Returns the absolute value of n.

##### (And b1 b2)
- `b1`: `Boolean`
- `b2`: `Boolean`
- return value: `Boolean`

Returns the Boolean conjunction of `b1` and `b2`.

##### (Average l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the average of the numbers in `l`.

##### (Between n1 n2 n3)

- `n1`: `Numeric`
- `n2`: `Numeric`
- `n3`: `Numeric`
- return value: `Boolean`

Returns whether `n2` < `n1` < `n3`.

##### (BetweenIncl n1 n2 n3)

- `n1`: `Numeric`
- `n2`: `Numeric`
- `n3`: `Numeric`
- return value: `Boolean`

Returns whether `n2` <= `n1` <= `n3`.

##### (Consecutive s l)

- `s`: `String`
- `l`: `List[Numeric]`
- return value: `Boolean`

Returns whether the elements of `l` are consecutive according to the criterion `s`:

- `s` == "integer": Are the elements consecutive integers?
- `s` == "even": Are the elements consecutive even integers?
- `s` == "odd": Are the elements consecutive odd integers?
- `s` == "prime": Are the elements consective prime integers?
- `s` == "k" (for some integer k): Are the elements consecutive multiples of k?

##### (Cube n)

- `n`: `Numeric`
- return value: `Numeric`

Returns the cube of n.

##### (Difference l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the largest element of `l` minus the smallest element.

##### (DigitCount n1 n2)

- `n1`: `Numeric`
- `n2`: `Numeric`
- return value: `Boolean`

Returns whether there are exactly `n2` digits in `n1`.

##### (Divides n1 n2)

- `n1`: `Numeric`
- `n2`: `Numeric`
- return value: `Boolean`

Returns whether `n1` divides `n2` evenly.

##### (DivisibleBy n1 n2)

- `n1`: `Numeric`
- `n2`: `Numeric`
- return value: `Boolean`

Returns whether `n1` is evenly divisible by `n2`.


##### (Elements n1 ... nK)

- `n1`: `Numeric`
- `nK`: `Numeric`
- return value: `List[Numeric]`

Returns the list of numbers [`n1`, ..., `nk`]

##### (Equivalent l)

- `l`: `List[Numeric]`
- return value: `Boolean`

Returns whether the elements of `l` are pairwise equal.

##### (Even n)

- `n`: `Numeric`
- return value: `Boolean`

Returns whether `n` is an even integer.

##### (Exists v b)

- `v`: `Var`
- `b`: `Boolean`
- return value: `Boolean`

Returns whether `b` is true for some real assignment to `v`.

##### (Forall v b)

- `v`: `Var`
- `b`: `Boolean`
- return value: `Boolean`

Returns whether `b` is true for all real assignments to `v`.

##### (GreaterThan n1 n2)

- `n1`: `Numeric`
- `n2`: `Numeric`
- return value: `Boolean`

Returns whether `n1` > `n2`.


##### (Increasing l)

- `l`: `List[Numeric]`
- return value: `Boolean`

Returns whether the elements of `l` appear in strictly increasing order.


##### (Index n l)

- `n`: `Numeric`
- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the `n`th element of `l`.

##### (Max l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the maximal element of `l`.

##### (Median l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the median element of `l`.

##### (MemberOf n l)

- `n`: `Numeric`
- `l`: `List[Numeric]`
- return value: `Boolean`

Returns whether `n` is a member of `l`.

##### (Min l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the minimal element of `l`.

##### (Negative n)

- `n`: `Numeric`
- return value: `Boolean`

Returns whether `n` is a negative number.

##### (Nonzero n)

- `n`: `Numeric`
- return value: `Boolean`

Returns whether `n` is a nonzero number.

##### (Not b)
- `b`: `Boolean`
- return value: `Boolean`

Returns the Boolean negation of `b`.

##### (Odd n)

- `n`: `Numeric`
- return value: `Boolean`

Returns whether `n` is an odd integer.

##### (Or b1 b2)
- `b1`: `Boolean`
- `b2`: `Boolean`
- return value: `Boolean`

Returns the Boolean disjunction of `b1` and `b2`.

##### (Positive n)

- `n`: `Numeric`
- return value: `Boolean`

Returns whether `n` is a positive number.

##### (Prime n)

- `n`: `Numeric`
- return value: `Boolean`

Returns whether `n` is a prime number.

##### (Product l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the product of the elements of `l`.

##### (SizeIs l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the number of elements in `l`.

##### (Square n)

- `n`: `Numeric`
- return value: `Numeric`

Returns the square of `n`.

##### (Sum l)

- `l`: `List[Numeric]`
- return value: `Numeric`

Returns the sum of the elements of `l`.

##### (Take n l)

- `n`: `Numeric`
- `l`: `List[Numeric]`
- return value: `List[Numeric]`

Returns a list of the first `n` elements of `l`.


##### (True b)

- `b`: `Boolean`
- return value: `Boolean`

Returns the truth value of `b`.



(HasPrototype s v)
(IsPrototype v s)
(Strategy x)
(MenuItem x n)
(ComboItem x1 x2)


## Errata

464 (all)
608 (forward ref)
842 (forward ref)
927 (forall)
