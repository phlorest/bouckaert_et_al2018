# Notes


## Data:

> We compiled a binary matrix representing the
> presence (1) or absence (0) of 18,238 cognate sets
> across 200 basic vocabulary terms in 306
> Greater-Pama–Nyungan languages. T

## Methods:

| Model                                      | Score    | Program  | Comment            |
|--------------------------------------------|----------|----------|--------------------|
| covarion + relaxed (1 site rate)           | -157136  | BEAST2   | best fitting model |
| ctmc + gamma (1 site rate) + relaxed       | -157206  | BEAST2   |                    |
| ctmc + relaxed (1 site rate)               | -157410  | BEAST2   |                    |
| stochastic dollo + relaxed (1 site rate)   | -162572  | BEAST2   |                    |
| covarion + relaxed (word rates)            | -157235  | BEAST2   |                    |
| covarion + strict (1 site rate)            | -157652  | BEAST2   |                    |
| phylogeography                  |          | BEAST2   |                    |



## Analysis:

> We derived our tree prior using the birth–death
> skyline model61, a variant of the widely used pure
> birth (Yule62) tree prior that accounts for the
> fact that not all of our languages were sampled at
> the same time
