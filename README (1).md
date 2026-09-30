# AI Tic-Tac-Toe

An unbeatable Tic-Tac-Toe opponent built with the **Minimax algorithm**. You play X, the AI plays O. The best a human can do is draw.

**Live demo:** _add your GitHub Pages link here_

## How it works

- The AI searches the full game tree recursively, assuming both players play optimally.
- Terminal scores: AI win = `10 - depth`, human win = `depth - 10`, draw = `0`. Using depth makes the AI prefer faster wins and delay losses.
- The AI picks the square with the highest Minimax score.

## Files

| File | What it is |
|---|---|
| `tictactoe.py` | Python version: Minimax engine + terminal game |
| `index.html` | Browser version (same algorithm in JavaScript), hosted on GitHub Pages |

## Run locally

```bash
python tictactoe.py
```

For the web version, open `index.html` in any browser.

## Tech

Python, JavaScript, HTML/CSS
