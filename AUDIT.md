# Local audit — lego-sets-business-analytics-dashboard-main

## Changes

Profiled all 18,457 catalog rows; documented the unresolved 2,669-set screenshot population. Added a reproducible CSV profiler, preserved the PBIX and four actual dashboard screenshots, and removed personal profile links, the promotional banner and redundant .gitkeep.

## Validation performed

- **PASS** — lego-sets-business-analytics-dashboard-main/scripts/profile_data.py: Python syntax
- **PASS** — lego-sets-business-analytics-dashboard-main/Dashboard/LEGO Sets Dashboard.pbix: Archive CRC; XML; PBIX layout where applicable (not native execution)
- **PASS** — `python3 scripts/profile_data.py`: 18,457 distinct set IDs, 14 fields, 1970–2022, 154 themes; missing-value and nonmissing-price counts recomputed.
- Archive members and XML were parsed where present; images decoded and screenshots reviewed. Notebook/JSON syntax and local paths were checked.
- No plaintext secret candidates, personal contact emails, promotional GitHub/LinkedIn profile links or machine-home paths were detected in the final scanned text/package content. This is a bounded local pattern scan, not proof that opaque native models contain no sensitive data.

## Remaining limitations

Power BI refresh/DAX, interactive filtering and remote image resolution were not tested. Raw-to-dashboard filtering lineage is unresolved. The compressed DataModel is not fully inspectable here. No license file or explicit dataset/third-party image redistribution permission was supplied.

## Provenance and execution scope

Original source datasets and SQL are retained. No Git history was present in the five extracted folders. Original Downloads folders match their pre-copy SHA-256 hashes. No GitHub command, authentication, repository creation, commit, push or upload was performed.

Original authorship and legally required notices remain in [ATTRIBUTION.md](ATTRIBUTION.md). Personal UI redactions do not replace author attribution.
