"""Student record file helpers for Week 4.

Complete the functions in this file. The tests expect these exact function names.
Use pathlib, csv, json, and UTF-8 text handling.
"""

from pathlib import Path


def ensure_folder(folder_path):
    """Create folder_path if it does not exist and return it as a Path."""
    # TODO: Convert folder_path to a Path, create the folder, and return the Path.
    raise NotImplementedError


def read_text_lines(file_path):
    """Return a list of non-empty stripped lines from a UTF-8 text file."""
    # TODO: Read text from file_path using UTF-8, strip whitespace, and skip blank lines.
    raise NotImplementedError


def write_text_lines(file_path, lines):
    """Write lines to a UTF-8 text file, one line per item.

    Create the parent folder if needed. Return the Path to the written file.
    """
    # TODO: Create the parent folder and write each item on its own line.
    raise NotImplementedError


def read_students_csv(file_path):
    """Read student records from a CSV file.

    The CSV file has columns: student_id, name, score.
    Return a list of dictionaries with student_id and name as strings and score as float.
    Skip rows with missing student_id, missing name, or invalid score.
    """
    # TODO: Use csv.DictReader. Convert score to float. Skip invalid rows.
    raise NotImplementedError


def write_students_csv(file_path, students):
    """Write student dictionaries to a CSV file with student_id, name, and score columns.

    Create the parent folder if needed. Return the Path to the written file.
    """
    # TODO: Use csv.DictWriter with the exact fieldnames.
    raise NotImplementedError


def load_students_json(file_path):
    """Load and return student records from a UTF-8 JSON file."""
    # TODO: Use json.load or json.loads with pathlib text reading.
    raise NotImplementedError


def save_students_json(file_path, students):
    """Save student records to a UTF-8 JSON file.

    Use indentation so the file is readable. Create the parent folder if needed.
    Return the Path to the written file.
    """
    # TODO: Use json.dump or json.dumps with indent=2.
    raise NotImplementedError


def student_names(students):
    """Return a sorted list of student names from a list of student dictionaries."""
    # TODO: Collect names and return them sorted alphabetically.
    raise NotImplementedError


def average_score(students):
    """Return the average score rounded to 2 decimals.

    Return 0.0 when the list is empty or when no valid scores are available.
    """
    # TODO: Convert valid scores to float and average them.
    raise NotImplementedError


def export_summary_json(file_path, students):
    """Create a JSON summary file for student records.

    The saved JSON object must contain:
    - count: number of student records
    - average_score: average score rounded to 2 decimals
    - names: sorted list of student names

    Return the summary dictionary after saving it.
    """
    # TODO: Build the summary dictionary, save it as JSON, and return it.
    raise NotImplementedError
