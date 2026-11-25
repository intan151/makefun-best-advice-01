# The Best Advice I Ever Got

[![make.fun](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![Rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/intan151/makefun-best-advice-01/rank.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![Reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/intan151/makefun-best-advice-01/reward.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)

Entry for the [make.fun](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0) competition **"The Best Advice I Ever Got"**.

## What it does

`main.py` is a small deterministic Python program (no network, no randomness).
It writes a single sentence — the best advice the writer ever received — to
`/output/entry.txt`.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## The entry

> My father said, 'Do the hard thing first, while you still have the courage to choose it,' and every good decision I have made since started there.

One sentence, 146 characters — inside the competition's 1–200 character gate.
`main.py` includes a self-check that asserts the gate (character limit, no
control characters, single line, exactly one sentence) before writing.
