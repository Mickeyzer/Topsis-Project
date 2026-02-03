# topsis-ishan-102313022

`topsis-ishan-102313022` is a Python package for solving **Multiple Criteria Decision Making (MCDM)** problems using the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**.

It helps rank alternatives based on their relative closeness to the ideal solution and is useful in real-world decision-making scenarios such as:

- Choosing the best product
- Selecting the best candidate
- Ranking investment options
- Engineering design evaluation
- Research and management decision analysis

---

## Installation

Use the Python package manager `pip` to install the package:

```bash
pip install topsis-ishan-102313022

Usage

Provide the input CSV file followed by the weights vector and impacts vector.

Command Format
topsis input.csv "w1,w2,w3,..." "+,-,+,..." output.csv

Example
topsis sample.csv "1,1,1,1" "+,-,+,+" result.csv


Vectors can also be provided without quotes if they contain no spaces:

topsis sample.csv 1,1,1,1 +,-,+,+ result.csv


To view help information:

topsis -h

Example Dataset
sample.csv

A CSV file showing data for different mobile handsets with varying features:

Model	Storage Space (GB)	Camera (MP)	Price ($)	Looks (out of 5)
M1	         16	              12	     250	         5
M2	         16	               8	     200	         3
M3	         32	              16	     300	         4
M4	         32	               8	     275	         4
M5	         16	              16	     225	         2
Weights Vector
[0.25, 0.25, 0.25, 0.25]

Impacts Vector
[+, +, -, +]

Sample Command
topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+" output.csv

Sample Output
----------------------------
       TOPSIS RESULTS
----------------------------
Alternative   Score     Rank
1             0.534277  3
2             0.308368  5
3             0.691632  1
4             0.534737  2
5             0.401046  4


The output CSV file will contain two additional columns:

Topsis Score

Rank

Important Notes

The first column of the CSV file must contain the alternative names (e.g., M1, M2, ...).

All remaining columns must contain numerical values only.

The number of weights must match the number of criteria columns.

The number of impacts must match the number of criteria columns.

Impacts must be either:

+ for benefit criteria

- for cost criteria

Do not include categorical (non-numeric) data in criteria columns.

Author

Developed by Ishan Bhat

License

This project is released for academic and educational use.
"# Topsis-Project" 
