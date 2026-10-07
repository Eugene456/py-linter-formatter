def format_linter_error(error: dict) -> dict:
    return {
        "line" : error["line_number"],
        "column" : error["column_number"],
        "message" : error["text"],
        "name" : error["code"],
        "source" : "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed",
        "errors": [
            {
                "line": item["line_number"],
                "column": item["column_number"],
                "message": item["text"],
                "name": item["code"],
                "source": "flake8"
            }
            for item in errors
        ]
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": file_path,
            "status": "passed" if len(errors) == 0 else "failed",
            "errors": [
                {
                    "line": item["line_number"],
                    "column": item["column_number"],
                    "message": item["text"],
                    "name": item["code"],
                    "source": "flake8"
                }
                for item in errors
            ]
        }
        for file_path, errors in linter_report.items()
    ]
