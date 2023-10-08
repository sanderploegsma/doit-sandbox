from pathlib import Path

src_dir = "src"
test_dir = "test"
src_files = list(Path(src_dir).glob("**/*.py"))
test_files = list(Path(test_dir).glob("**/*.py"))

def task_format():
    """Auto-formats Python files"""

    yield {
        "name": "black",
        "actions": [["black", src_dir, test_dir]],
        "file_dep": src_files + test_files,
    }

    yield {
        "name": "isort",
        "actions": [["isort", src_dir, test_dir]],
        "file_dep": src_files + test_files,
    }

def task_lint():
    """Lints Python files"""

    yield {
        "name": "black",
        "actions": [["black", "--check", src_dir, test_dir]],
        "file_dep": src_files + test_files,
    }

    yield {
        "name": "isort",
        "actions": [["isort", "--check-only", src_dir, test_dir]],
        "file_dep": src_files + test_files,
    }

    yield {
        "name": "pylint",
        "actions": [["pylint", src_dir, test_dir]],
        "file_dep": src_files + test_files,
    }

def task_test():
    """Runs tests"""

    return {
        "actions": [["pytest", test_dir]],
        "uptodate": [False],
        "verbosity": 2,
    }
