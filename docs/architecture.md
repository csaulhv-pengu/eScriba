# Architecture

eScriba follows a modular architecture:

- ui: Qt-based user interface
- core: domain models (Project, Chapter, Scene)
- storage: filesystem-based persistence
- resources: icons and static assets

## Design Decisions
- Python + PySide6
- Markdown for content
- YAML/JSON for metadata
- Filesystem as source of truth

This ensures transparency, portability and longevity.

## General structure for projects:
Project
 ├── books[]
 │    ├── chapters[]
 │    │    ├── scenes[]
 │    │    │    ├── text (markdown)
 │    │    │    └── metadata (tags, pov, status)
 │
 ├── characters[]
 ├── locations[]
 ├── timeline[]        (optional)
 ├── notes[]
 ├── references[]      (optional)
 │
 └── metadata
