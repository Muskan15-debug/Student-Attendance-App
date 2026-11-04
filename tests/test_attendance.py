import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import check_attendance

@pytest.mark.parametrize(
    "att, expected",
    [
        (85, "Allowed"),
        (75, "Not allowed to sit in exam"),
        (80, "Allowed"),
        (60, "Not allowed to sit in exam"),
    ]
)

def test_check_attendance(att, expected):
    result = check_attendance(att)
    assert result == expected
