"""Week 4 student records exchange package."""

from .student_records import (
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

__all__ = [
    "ensure_folder",
    "read_text_lines",
    "write_text_lines",
    "read_students_csv",
    "write_students_csv",
    "load_students_json",
    "save_students_json",
    "student_names",
    "average_score",
    "export_summary_json",
]
