# Coursely

Coursely is a Python project that helps generate course outlines, lesson plans, and quizzes programmatically using large language models. It provides configurable prompts and templates to create structured teaching materials for different audiences and course lengths.

- Repository: https://github.com/Astroking2004/coursely
- Language: Python
- License: MIT

## Features

- Generate course outlines and module breakdowns
- Produce lesson plans with learning objectives and activities
- Create assessment questions and quizzes (various formats)
- Template-driven prompts so outputs can be customized
- Designed to integrate with LLM APIs (e.g., OpenAI-compatible models)

## Quickstart

These instructions are general and should work for typical Python projects. Adjust paths/commands to match the actual entrypoint in this repo (for example `main.py`, `app.py`, `scripts/generate_course.py`, or `python -m coursely`).

Prerequisites:
- Python 3.8+
- pip
- An API key for the language model provider you want to use (set via environment variable; e.g., `OPENAI_API_KEY`)

1. Clone the repo
```bash
git clone https://github.com/Astroking2004/coursely.git
cd coursely
```

2. Create a virtual environment and install dependencies
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

3. Configure environment variables
```bash
export OPENAI_API_KEY="your_api_key_here"
# On Windows (PowerShell)
# $env:OPENAI_API_KEY="your_api_key_here"
```

4. Run the generator
If the repository exposes a module entrypoint:
```bash
python -m coursely --help
```

Or, if there is a script under `scripts/`:
```bash
python scripts/generate_course.py \
  --title "Introduction to Algebra" \
  --length 8 \
  --audience "High school students" \
  --output "intro_to_algebra.md"
```

Replace the command above with the actual script or module provided in this repository.

## Example usage (library-style)

If this repo exposes Python functions or classes to call programmatically, an example might look like:

```python
from coursely import generate_course

course = generate_course(
    title="Introduction to Algebra",
    modules=8,
    audience="High school",
    style="concise"
)

print(course)  # or save to file
```

(Adjust imports and function names to match the code in the repository.)

## Configuration & Templates

- Prompts and templates: Look for a `templates/` or `prompts/` directory to edit the templates used for prompt generation.
- Models: You may be able to configure the LLM model via environment variables or a config file (e.g., `MODEL=gpt-4`).
- Output formats: Common output formats are Markdown, JSON, or plain text — adapt templates to change structure.

## Testing

If tests are included, run them with:
```bash
pytest
```

If no test suite exists, consider adding tests for prompt formatting, output structure, and any parsing logic.

## Contributing

Contributions are welcome. Typical workflow:

1. Fork the repo
2. Create a branch: `git checkout -b feat/my-feature`
3. Make changes and add tests
4. Submit a pull request describing the change

Please follow the repository's code style and include tests for new functionality.

## Roadmap / Ideas

- Add more output templates (syllabus, slide decks, formative assessment banks)
- Add a web UI for interactive course generation
- Add CLI flags for advanced control (rubrics, learning outcomes alignment)
- Add integration tests for model calls (mocked)

## Security & Secrets

Do not commit API keys or other secrets to the repository. Use environment variables or a secrets manager.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact / Questions

If you have questions about this repository or want help integrating a particular model/provider, open an issue or contact the repository owner: https://github.com/Astroking2004
