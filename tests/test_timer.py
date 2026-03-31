import pytest
from lab_assistant import timer


def test_countdown_timer_negative_hours():
    with pytest.raises(ValueError, match="Input cannot be negative"):
        timer.countdown_timer(-1, 0, 0)


def test_countdown_timer_negative_minutes():
    with pytest.raises(ValueError, match="Input cannot be negative"):
        timer.countdown_timer(0, -1, 0)


def test_countdown_timer_negative_seconds():
    with pytest.raises(ValueError, match="Input cannot be negative"):
        timer.countdown_timer(0, 0, -1)


def test_countdown_timer_zero_total_time():
    with pytest.raises(ValueError, match="Timer must be greater than zero"):
        timer.countdown_timer(0, 0, 0)


def test_countdown_timer_valid_short_countdown(monkeypatch):
    sleep_calls = []
    clear_calls = []
    print_calls = []

    def fake_sleep(seconds):
        sleep_calls.append(seconds)

    def fake_clear():
        clear_calls.append(True)

    def fake_print(*args, **kwargs):
        print_calls.append((args, kwargs))

    monkeypatch.setattr(timer.time, "sleep", fake_sleep)
    monkeypatch.setattr(timer.console, "clear", fake_clear)
    monkeypatch.setattr(timer.console, "print", fake_print)

    timer.countdown_timer(0, 0, 2)

    assert sleep_calls == [1, 1]
    assert len(clear_calls) == 2
    assert len(print_calls) >= 4