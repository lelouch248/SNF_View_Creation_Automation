# SDM Views Creation

Utilities for validating and managing Snowflake views in the `Database.Schema` schema.

This project is focused on:
- Connecting to Snowflake using environment-based configuration
- Listing views by environment (DEV, TST, PRD)
- Running lightweight validation checks on views using `EXPLAIN`
- Keeping SQL backup scripts for pre-change rollback safety

## Why This Project Exists

When making schema/view changes, it is easy to introduce breakage. These scripts provide a quick way to:
- Verify view health before or after change windows
- Detect views that fail to compile/query
- Preserve backup DDL scripts so views can be restored quickly

## Current Workflow

1. Connect to Snowflake using `snowflake_con.py`
2. Fetch all views from `Database.Schema` using `utility.py`
3. Validate each view with `EXPLAIN` in `testing_views.py`
4. Review backup SQL files before applying structural changes

## Repository Structure

- `testing_views.py`: Main validation script that checks each view and reports pass/fail.
- `snowflake_con.py`: Snowflake connection helper using `.env` values and `externalbrowser` auth.
- `utility.py`: Helper function(s) for retrieving view lists.
- `main.py`: Archived/experimental automation logic (backup generation, rename/deployment ideas).
- `dev_bkp_scripts_before_changes.sql`: DEV backup DDL snapshot.
- `tst_bkp_scripts_before_changes.sql`: TST backup DDL snapshot.
- `notebook.ipynb`: Notebook-based experimentation.

## Requirements

- Python 3.10+
- Snowflake account access
- Role with permission to show/query views in target schemas

Install dependencies:

```bash
pip install snowflake-connector-python python-dotenv
```

## Environment Setup

Create a `.env` file in project root:

```env
user=your.email@company.com
account=your_account_identifier
warehouse=your_warehouse
database=your_database
schema=your_schema
role=your_role
```

Notes:
- Authentication is set to `externalbrowser`, so a browser login prompt is expected.
- Keep `.env` out of source control.

## How To Run

Run view validation:

```bash
python testing_views.py
```

Expected output pattern:
- `Total views found: <count>`
- `<fully_qualified_view_name>: no issue found`
- `<fully_qualified_view_name>: issue found - <error>`

## Safe Change Practices

- Always take or refresh backup DDL scripts before bulk view changes.
- Test in lower environments (DEV/TST) before PRD.
- Run the validator after any rename or definition change.

## Future Improvements

- Add CLI arguments for environment selection (`DEV`, `TST`, `PRD`)
- Add structured logging + CSV/JSON result export
- Add unit tests with mocked Snowflake cursor responses
- Move commented logic in `main.py` into reusable modules

## Disclaimer

These scripts execute metadata and validation queries against Snowflake. Review permissions and target environment carefully before running in production.
