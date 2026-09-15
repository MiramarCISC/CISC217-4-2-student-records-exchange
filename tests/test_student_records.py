from pathlib import Path
import csv
import json

import pytest

from cisc217_week4.student_records import (
    ensure_folder,
    read_text_lines,
    write_text_lines,
    read_students_csv,
    write_students_csv,
    load_students_json,
    save_students_json,
    student_names,
    average_score,
    export_summary_json,
)


def test_ensure_folder_creates_folder(tmp_path):
    folder = tmp_path / "output" / "reports"

    result = ensure_folder(folder)

    assert isinstance(result, Path)
    assert result.exists()
    assert result.is_dir()


def test_write_and_read_text_lines_utf8(tmp_path):
    path = tmp_path / "output" / "names.txt"

    written = write_text_lines(path, ["Ada", "Grace", "李雷", "Python 🐍"])
    lines = read_text_lines(written)

    assert written == path
    assert lines == ["Ada", "Grace", "李雷", "Python 🐍"]


def test_read_text_lines_skips_blank_lines_and_strips(tmp_path):
    path = tmp_path / "names.txt"
    path.write_text("  Ada  

Grace

Linus
", encoding="utf-8")

    assert read_text_lines(path) == ["Ada", "Grace", "Linus"]


def test_read_students_csv_converts_scores_and_skips_invalid_rows(tmp_path):
    path = tmp_path / "students.csv"
    path.write_text(
        "student_id,name,score
"
        "s001,Ada,95
"
        "s002,Grace,88.5
"
        "s003,Missing Score,not-a-number
"
        ",No ID,77
"
        "s004,,91
",
        encoding="utf-8",
    )

    students = read_students_csv(path)

    assert students == [
        {"student_id": "s001", "name": "Ada", "score": 95.0},
        {"student_id": "s002", "name": "Grace", "score": 88.5},
    ]


def test_write_students_csv_writes_expected_header_and_rows(tmp_path):
    path = tmp_path / "exports" / "students.csv"
    students = [
        {"student_id": "s001", "name": "Ada", "score": 95.0},
        {"student_id": "s002", "name": "Grace", "score": 88.5},
    ]

    write_students_csv(path, students)

    with path.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert rows == [
        {"student_id": "s001", "name": "Ada", "score": "95.0"},
        {"student_id": "s002", "name": "Grace", "score": "88.5"},
    ]


def test_save_and_load_students_json_utf8(tmp_path):
    path = tmp_path / "exports" / "students.json"
    students = [
        {"student_id": "s001", "name": "Ada", "score": 95.0},
        {"student_id": "s003", "name": "李雷", "score": 91.0},
    ]

    written = save_students_json(path, students)
    loaded = load_students_json(written)

    assert written == path
    assert loaded == students


def test_saved_json_is_readable_with_indent(tmp_path):
    path = tmp_path / "students.json"
    students = [{"student_id": "s001", "name": "Ada", "score": 95.0}]

    save_students_json(path, students)
    text = path.read_text(encoding="utf-8")

    assert "
" in text
    assert "  " in text
    assert json.loads(text) == students


def test_student_names_returns_sorted_names():
    students = [
        {"student_id": "s003", "name": "Linus", "score": 91.0},
        {"student_id": "s001", "name": "Ada", "score": 95.0},
        {"student_id": "s002", "name": "Grace", "score": 88.5},
    ]

    assert student_names(students) == ["Ada", "Grace", "Linus"]


def test_average_score_rounds_to_two_decimals():
    students = [
        {"student_id": "s001", "name": "Ada", "score": 95},
        {"student_id": "s002", "name": "Grace", "score": "88.5"},
        {"student_id": "s003", "name": "Linus", "score": 91},
    ]

    assert average_score(students) == 91.5


def test_average_score_returns_zero_for_empty_or_invalid_scores():
    assert average_score([]) == 0.0
    assert average_score([{"name": "No Score"}, {"score": "bad"}]) == 0.0


def test_export_summary_json_saves_and_returns_summary(tmp_path):
    path = tmp_path / "output" / "summary.json"
    students = [
        {"student_id": "s002", "name": "Grace", "score": 88.5},
        {"student_id": "s001", "name": "Ada", "score": 95},
    ]

    summary = export_summary_json(path, students)
    loaded = json.loads(path.read_text(encoding="utf-8"))

    assert summary == {
        "count": 2,
        "average_score": 91.75,
        "names": ["Ada", "Grace"],
    }
    assert loaded == summary
