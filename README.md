# CISC 217 Week 4 Lab: Student Records Exchange

## Weekly Topic

Text files, CSV, JSON, file paths, Unicode, and UTF-8.

## Lab Summary

In this lab, you will write Python functions that read and write student records using plain text, CSV, and JSON files. You will also practice using `pathlib.Path` and `encoding="utf-8"`.

You will complete the code in:

```text
src/cisc217_week4/student_records.py
```

Do **not** change function names, parameter names, file names, package names, or test file names unless your instructor tells you to.

## Learning Goals

By the end of this lab, you should be able to:

- Use `Path` objects to work with files and folders.
- Read and write UTF-8 text files.
- Explain the difference between text, characters, code points, encodings, and bytes.
- Read and write CSV files with `csv.DictReader` and `csv.DictWriter`.
- Read and write JSON files.
- Convert CSV string values into numeric values.
- Create a JSON summary file from student records.
- Run `pytest`, commit your work, push to GitHub, and complete peer review with a pull request.

## Development Workflow

1. Open the Classroom50 assignment link from this Canvas module and accept the assignment.
2. Click **Go to your GitHub repository** and keep the repository open in a browser tab.
3. Open [NRP JupyterHub](https://sdccd-jupyterhub.nrp-nautilus.io/).
4. Start your JupyterHub server with **0 GPUs, 2 CPU cores, 4 GB Memory, Stack Minimal**.
5. If you have not already created an SSH key in JupyterHub, run:

   ```bash
   ssh-keygen -t ed25519
   ```

   Press **Enter** three times to use the default location and skip a passphrase.

6. Print your SSH public key:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

7. Copy the full line that starts with `ssh-ed25519`.
8. Add the key to GitHub at <https://github.com/settings/keys>.
9. In your GitHub assignment repository, click **Code**, choose **SSH**, and copy the clone URL.
10. Clone the repository in JupyterHub:

    ```bash
    cd ~/
    git clone PASTE_YOUR_SSH_CLONE_URL_HERE
    cd REPOSITORY_FOLDER_NAME
    ```

11. Confirm you are in the repository root:

    ```bash
    pwd
    ls
    ```

12. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

13. Install the project and test tools:

    ```bash
    python -m pip install -e .[test]
    ```

14. Run the tests before editing:

    ```bash
    python -m pytest -q
    ```

15. Edit only this file:

    ```text
    src/cisc217_week4/student_records.py
    ```

16. Run tests until they pass:

    ```bash
    python -m pytest -q
    ```

17. Commit and push your work:

    ```bash
    git status
    git add src/cisc217_week4/student_records.py
    git commit -m "Complete week 4 student records exchange lab"
    git push origin main
    ```

18. Open the **Actions** tab in GitHub and confirm the autograder result.
19. If peer review access is not already available, grant the GitHub team `classroom50-cisc217-inter-python-programming` the **Read** role on your repository.
20. Post your GitHub repository link and required evidence in the Canvas lab discussion.

## Required Functions

Complete all functions in `student_records.py`.

### `ensure_folder(folder_path)`

Create the folder if it does not exist and return it as a `Path` object.

Rules:

- Accept either a string path or a `Path` object.
- Create missing parent folders.
- Do not fail if the folder already exists.
- Return the final folder path as a `Path` object.

### `read_text_lines(file_path)`

Read a UTF-8 text file and return a list of non-empty stripped lines.

Rules:

- Use UTF-8.
- Remove leading and trailing whitespace from each line.
- Skip blank lines.
- Return a list of strings.

### `write_text_lines(file_path, lines)`

Write text lines to a UTF-8 text file.

Rules:

- Create the parent folder if needed.
- Write one item per line.
- End lines with newline characters.
- Return the path to the written file as a `Path` object.

### `read_students_csv(file_path)`

Read student records from a CSV file.

The CSV file has these columns:

```text
student_id,name,score
```

Rules:

- Use `csv.DictReader`.
- Return a list of dictionaries.
- Keep `student_id` and `name` as strings.
- Convert `score` to a float.
- Skip rows with a missing student ID, missing name, or invalid score.

Example return value:

```python
[
    {"student_id": "s001", "name": "Ada", "score": 95.0},
    {"student_id": "s002", "name": "Grace", "score": 88.5},
]
```

### `write_students_csv(file_path, students)`

Write student records to a CSV file.

Rules:

- Use `csv.DictWriter`.
- Write the header row.
- Use exactly these field names: `student_id`, `name`, `score`.
- Create the parent folder if needed.
- Return the path to the written file as a `Path` object.

### `load_students_json(file_path)`

Load student records from a UTF-8 JSON file.

Rules:

- Read JSON from the file.
- Return the parsed Python object.

### `save_students_json(file_path, students)`

Save student records to a UTF-8 JSON file.

Rules:

- Create the parent folder if needed.
- Use indentation so the JSON is readable.
- Return the path to the written file as a `Path` object.

### `student_names(students)`

Return a sorted list of student names.

Rules:

- Read the `name` value from each student dictionary.
- Return names sorted alphabetically.

### `average_score(students)`

Return the average score rounded to 2 decimals.

Rules:

- Convert valid score values to floats.
- Ignore missing or invalid scores.
- Return `0.0` if there are no valid scores.

### `export_summary_json(file_path, students)`

Create a JSON summary file and return the summary dictionary.

The summary must contain:

```python
{
    "count": 2,
    "average_score": 91.75,
    "names": ["Ada", "Grace"]
}
```

Rules:

- `count` is the number of student records.
- `average_score` uses your `average_score()` function.
- `names` uses your `student_names()` function.
- Save the summary to JSON.
- Return the summary dictionary.

## Running the Tests

Run:

```bash
python -m pytest -q
```

A passing run should show output similar to:

```text
11 passed
```

The exact number of tests may change if your instructor updates the assignment.

## Canvas Initial Lab Post

After your tests pass and you push your work to GitHub, post in the Week 4 Lab Discussion.

Your initial post should include:

1. A link to your GitHub/Classroom50 repository.
2. Test evidence showing that you ran `python -m pytest -q` and passed the tests.
3. One example of where your code uses `pathlib.Path`.
4. One example of where your code reads or writes UTF-8 text.
5. One example of where your code reads or writes CSV.
6. One example of where your code reads or writes JSON.
7. One question, challenge, or debugging issue you encountered.

Example initial post:

> My repository is here: PASTE_LINK_HERE. My tests passed after I ran `python -m pytest -q`. I used `Path` in `ensure_folder()` to create folders and return a path object. I used UTF-8 when reading and writing text files so names like 李雷 can be stored correctly. I used `csv.DictReader` to read student rows as dictionaries and converted the score field to a float. I used JSON to save a summary file with the count, average score, and sorted names. One issue I had was remembering that CSV values are read as strings.

## Peer Review Pull Request

Your peer review is completed through a GitHub pull request and a Canvas reply in the same lab discussion board.

1. Fork a classmate's repository on GitHub.
2. Clone your fork into JupyterHub:

   ```bash
   cd ~/
   git clone PASTE_YOUR_FORK_SSH_URL_HERE
   cd REPOSITORY_FOLDER_NAME
   ```

3. Create a peer review branch:

   ```bash
   git checkout -b peer-review
   ```

4. Make a small helpful change, such as a documentation improvement or clarifying comment. Do not rewrite your classmate's solution.
5. Run the tests:

   ```bash
   python -m pytest -q
   ```

6. Commit the peer review:

   ```bash
   git add .
   git commit -m "Peer review feedback"
   ```

7. Push your branch to your fork:

   ```bash
   git push -u origin peer-review
   ```

8. Check the Actions tab on your fork to confirm your change did not break the project.
9. Open a pull request from your fork's `peer-review` branch into your classmate's `main` branch.
10. Reply in Canvas with the pull request link and one specific comment or question.

Example Canvas peer review reply:

> Hi Jordan, here is the pull request I opened on your repository: PASTE_PULL_REQUEST_LINK_HERE. I added a short comment about why `encoding="utf-8"` is used when writing JSON. I noticed your CSV reader converts the score field to a float, which is important because CSV values are read as strings. One question I had was how your function handles a row with a missing score.

After the pull request is created and your Canvas reply is posted, you may delete the cloned copy from JupyterHub if you no longer need it:

```bash
cd ~/
rm -rf REPOSITORY_FOLDER_NAME
```

## Academic Integrity

You may discuss setup steps, error messages, and general Python concepts with classmates. Your submitted code must be your own work. Do not copy another student's solution. Peer review pull requests should be small, helpful improvements rather than replacement solutions.
