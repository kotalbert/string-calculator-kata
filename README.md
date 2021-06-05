# String calculator kata 
## Project description.

Write a method `add` under an object `StringCalculator` that, given a delimited string, returns the sum of the numbers in the string.

1. An empty string returns zero `'' => 0`
2. A single    number returns the value `'1' => 1 '2' => 2`
3. Two numbers, comma delimited, returns the sum `'1,2' => 3 '10,20' => 30`
4. Two numbers, newline delimited, returns the sum '`1\n2' => 3
5. Three numbers, delimited either way, returns the sum `'1\n2,3\n4' => 10`
6. Negative numbers throw an exception with the message `'-1,2,-3' => 'negatives not allowed: -1,-3'`
7. Numbers greater than 1000 are ignored
8. A single char delimiter can be defined on the first line starting with `//` (e.g. `//#\n1#2` for a ‘#’ as the delimiter)
9. A multi char delimiter can be defined on the first line starting with `//` (e.g. `//###\n1###2` for ‘###’ as the delimiter)

source: https://github.com/wix/tdd-katas#string-calculator
