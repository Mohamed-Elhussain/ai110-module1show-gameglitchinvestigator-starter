"""Pure game logic for the Glitchy Guesser.

FIX: Refactored out of app.py into this module with Claude (Cowork agent mode)
so the logic can be unit-tested without running Streamlit.
"""

# FIX: Hard was 1-50 (easier than Normal's 1-100). Ranges now grow with difficulty.
DIFFICULTY_RANGES = {
    "Easy": (1, 20),
    "Normal": (1, 100),
    "Hard": (1, 200),
}

ATTEMPT_LIMITS = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    return DIFFICULTY_RANGES.get(difficulty, (1, 100))


def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    raw = raw.strip()
    try:
        # FIX: decimals like "3.7" used to be silently truncated to 3.
        value = int(raw)
    except ValueError:
        return False, None, "That is not a whole number."

    # FIX: out-of-range guesses used to be accepted and cost an attempt.
    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Pick a number between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: messages were swapped ("Too High" told you to go HIGHER), and app.py
    # sometimes passed the secret as a str, causing alphabetical comparisons.
    # Both values are now ints, so the TypeError fallback was removed.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number (1 = first guess)."""
    if outcome == "Win":
        # FIX: was 100 - 10 * (attempt_number + 1), an off-by-one penalty.
        points = 100 - 10 * (attempt_number - 1)
        return current_score + max(points, 10)

    # FIX: "Too High" used to award +5 on even attempts. Every miss now costs 5.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
