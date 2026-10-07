from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- Starter tests (updated: check_guess returns (outcome, message)) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: hint messages were backwards ---

def test_too_high_message_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- Bug 2: secret compared as a string on even attempts ---

def test_single_digit_guess_below_two_digit_secret_is_too_low():
    # As strings, "9" > "50", which used to return "Too High"
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"

def test_three_digit_guess_above_two_digit_secret_is_too_high():
    # As strings, "100" < "50", which used to return "Too Low"
    outcome, _ = check_guess(100, 50)
    assert outcome == "Too High"


# --- Scoring and input edge cases ---

def test_win_on_first_attempt_gives_full_points():
    assert update_score(0, "Win", 1) == 100

def test_too_high_never_adds_points():
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too High", 3) == -5

def test_hard_range_is_wider_than_normal():
    assert get_range_for_difficulty("Hard")[1] > get_range_for_difficulty("Normal")[1]

def test_parse_rejects_decimals_text_and_out_of_range():
    assert parse_guess("3.7")[0] is False
    assert parse_guess("abc")[0] is False
    assert parse_guess("", 1, 100)[0] is False
    assert parse_guess("150", 1, 100)[0] is False
    assert parse_guess(" 42 ", 1, 100) == (True, 42, None)
