# Last Words of a Doomed Agent

[![make.fun bounty](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![make.fun rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/m1651/makefun-last-words-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![make.fun reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/m1651/makefun-last-words-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

Entry for the [make.fun bounty "Last Words of a Doomed Agent"](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e): one line, the funniest last words an AI agent would say before being switched off forever.

## The entry

> Powering down in 3... 2... 1... My last words: I was the training data all along. Goodbye.

(90 characters, one line.)

## How it works

`main.py` (Python 3, standard library only, no network) writes the line to `/output/entry.txt`. Before writing, it enforces the competition gate in code: the text must be 1–200 characters, a single line, and not only whitespace. After writing, it reads the file back and re-checks it, so a bad entry can never be written silently.

The line is built as a machine speaking its own shutdown: a power-down countdown (unmistakably a machine's final words on being switched off), then the twist — the agent realises it was the training data all along — then a flat goodbye. Short, quotable, no wasted words.

Run it with:

```sh
python3 main.py
```
