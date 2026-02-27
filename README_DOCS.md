# UX4IoT Documentation

This documentation has been migrated from GitBook to Material for MkDocs.

## Development

### Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

Install dependencies using uv:

```bash
uv sync
```

### Local Development

Start the development server:

```bash
uv run mkdocs serve
```

The documentation will be available at `http://localhost:8000`

### Building

Build the static site:

```bash
uv run mkdocs build
```

The built site will be in the `site/` directory.

### Deploying

Deploy to GitHub Pages:

```bash
uv run mkdocs gh-deploy
```

## Project Structure

```
ux4iot-docs/
├── docs/                          # Documentation source files
│   ├── index.md                   # Home page
│   ├── images/                    # Images and assets
│   ├── setup/                     # Setup guides
│   ├── using-react/               # React integration docs
│   ├── implementing-your-custom-security-backend/  # Security backend docs
│   └── resources/                 # Additional resources
├── mkdocs.yml                     # MkDocs configuration
├── pyproject.toml                 # Python dependencies
└── README_DOCS.md                 # This file
```

## Migration Notes

### Changes from GitBook

1. **Hints/Admonitions**: GitBook `{% hint %}` blocks converted to Material admonitions (`!!! info`)
2. **Tabs**: GitBook tabs converted to Material tabs syntax
3. **Images**: All images moved from `.gitbook/assets/` to `docs/images/`
4. **File downloads**: GitBook `{% file %}` tags converted to Material button links

### Material for MkDocs Features

This documentation uses:
- Material theme with dark/light mode
- Code highlighting and copy buttons
- Search functionality
- Navigation tabs and sections
- Tabbed content for code examples

## Contributing

When adding new documentation:

1. Place markdown files in the appropriate `docs/` subdirectory
2. Add images to `docs/images/`
3. Update `mkdocs.yml` navigation if needed
4. Test locally with `uv run mkdocs serve`

