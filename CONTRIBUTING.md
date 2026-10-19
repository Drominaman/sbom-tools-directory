# Contributing to SBOM Tools

Contributions are welcome from maintainers, vendors, security teams, and independent researchers.

## Propose a new tool

1. Check `data/tools.json` for an existing entry.
2. Open a pull request adding the product in alphabetical or category-neutral order, using the existing JSON schema.
3. Link to the official project or product and to public documentation that supports the description.
4. Keep the description factual and under 180 characters. No superlatives, unverifiable performance claims, or sales slogans.
5. Disclose any relationship to the vendor or project in the pull request.
6. Run `python3 scripts/validate.py` and `python3 scripts/build.py --check`.

## Correct a listing

Send a primary-source URL and state the exact claim that needs to change. A correction can update the description, category, pricing model label, or link.

## Category guide

- `generation`: creates SBOMs from software or artifacts
- `analysis`: uses SBOMs or package inventories to investigate security or license risk
- `validation`: checks SBOM structure, data quality, or release-to-release changes
- `management`: organizes SBOMs across software, releases, vendors, and teams
- `embedded`: works with embedded software, firmware or connected products

Most tools span categories. Assign the one best matching their primary use in this directory.

## Editing the site

Edit `data/tools.json` for catalog changes, then run:

```bash
python3 scripts/build.py
python3 scripts/validate.py
```

The generator updates `docs/index.html` and `docs/tools.csv` from the JSON catalog. Update the README summary by hand when adding or removing tools. No external dependencies are needed.