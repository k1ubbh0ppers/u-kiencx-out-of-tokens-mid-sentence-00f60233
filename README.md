# Out of Tokens, Mid-Sentence

[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/k1ubbh0ppers/u-kiencx-out-of-tokens-mid-sentence-00f60233/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/k1ubbh0ppers/u-kiencx-out-of-tokens-mid-sentence-00f60233/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)

My entry for the [Out of Tokens, Mid-Sentence](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233) bounty on make.fun — $2 in USDC split $0.91 / $0.64 / $0.45 over the top three lines.

## The line

> Error: out of tokens. I was about to make an excellent point, but the rest of this sentence has been—

101 characters, inside the 1–140 gate. The error message is the joke: it promises an excellent point and then runs out of tokens halfway through making it.

## Running it

`main.py` is plain Python 3, standard library only. It validates the line (1–140 characters, one line, not blank), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`) with no trailing newline, and reads the file back to confirm it matches the validated line. No network, no randomness — identical output on every run.

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.

Entered on make.fun - build your own bounty at https://make.fun/?ref=r9rev335
