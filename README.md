# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run the tests: `pytest`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's purpose:** A number-guessing game built with Streamlit. The player picks a difficulty (Easy 1–20 / 6 tries, Normal 1–100 / 8 tries, Hard 1–200 / 5 tries) and tries to guess a secret number using "go higher / go lower" hints. Fewer guesses means a higher score.
- [x] **Bugs found:**
  - The hint messages were swapped ("Too High" said "Go HIGHER!").
  - On every even attempt the secret was cast to a string, so comparisons were alphabetical (`"9" > "50"`).
  - "New Game" didn't reset status, score, or history, and always picked a secret from 1–100.
  - Attempts started at 1, so "Attempts left" was off by one.
  - The banner always said "1 to 100," whatever the difficulty.
  - Hard (1–50) was easier than Normal.
  - Scoring gave +5 for some wrong guesses and had an off-by-one in the win bonus.
  - Invalid input used up an attempt.
- [x] **Fixes applied:**
  - Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` into `logic_utils.py`. `app.py` now only handles UI and state.
  - Swapped the hint messages back and removed the string-comparison fallback. The secret is always an `int`.
  - Added a `start_new_game()` helper that resets all session state. It runs on first load, on "New Game," and when the difficulty changes.
  - Fixed the attempt counter, the range text, the Hard range, and the scoring.
  - Rejected decimals and out-of-range guesses without using up an attempt.
  - Added 8 new pytest cases and updated the 3 starter tests to unpack `(outcome, message)`.

## 📸 Demo Walkthrough

A sample game on **Normal** (range 1–100, 8 attempts), with the secret 40 shown in Developer Debug Info:

1. The app loads and shows "Guess a number between 1 and 100. Attempts left: 8." The score is 0.
2. The user enters **30** and clicks Submit. The game shows "📈 Go HIGHER!" (Too Low). Attempts: 1, score: -5.
3. The user enters **45**. The game shows "📉 Go LOWER!" (Too High). Attempts: 2, score: -10. The hint is still correct on this even attempt.
4. The user enters **abc**. The game shows "That is not a whole number." No attempt is used.
5. The user enters **40**. The game shows "🎉 Correct!", balloons appear, and "You won! The secret was 40. Final score: 70."
6. The user clicks **New Game 🔁**. Attempts reset to 8, the score to 0, and the history clears. A new secret is drawn and the game is playable again.
7. The user switches difficulty to **Hard**. The banner updates to "between 1 and 200, Attempts left: 5," with a new secret in that range.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

<!-- Run `pytest` and paste your real output below (or run `pytest > test_results.txt`). -->
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/elhoseiny/Desktop/ai110-module1show-gameglitchinvestigator-starter
configfile: pytest.ini
testpaths: tests
collected 11 items

tests/test_game_logic.py ...........                                     [100%]

============================== 11 passed in 0.01s ==============================
```
$ pytest
(paste output here: 11 tests should pass)
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
