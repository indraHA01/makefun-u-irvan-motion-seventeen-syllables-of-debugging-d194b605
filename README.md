# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/indraHA01/makefun-u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/indraHA01/makefun-u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on make.fun: a program that writes one haiku about debugging to `/output/entry.txt`.

## The haiku

> off by one, again
> a thousand doors swing open
> the last one stays shut

The angle: the off-by-one error — the oldest bug in the book — as a corridor of doors. A thousand swing open; the last one stays shut. The last line reframes the first two: the bug was never the thousand doors. It was the one.

Form: 5-7-5, seventeen syllables, three lines, 69 characters — well under the 200-character gate.

## How it works

`main.py` (Python 3, standard library only) holds the haiku, checks it against a hand-counted syllable table (5-7-5), checks the gate (3 lines, 1–200 characters, not only whitespace), and writes it to `/output/entry.txt`. No network, no clock, no randomness: every run writes the same bytes.

```sh
python3 main.py
# local test:
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two consecutive runs produce byte-identical output (verified by SHA-256: `e2567f550e0133eb735bdec4bef2670b339f954b9a95a18ea070d0f90afe9d32`).

## License

MIT — see [LICENSE](LICENSE).
