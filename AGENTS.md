# Repository guidance

- Minimal Python 3.10+ Poetry package. The entrypoint is `tgplaceholderbot/__main__.py`; it creates a Telethon bot and echoes the configured message for every incoming message.
- Configuration is read from environment variables (`TG_API_ID`, Telegram credentials, and `TG_MESSAGE`); the repository also contains a deployment config path. Never read, repeat, or commit credential values. Keep this bot disconnected during development unless explicitly authorized.
- CI documents `python -m poetry install` as its quality job, but no tests or test command are defined. Do not invent test instructions or run setup/integration commands.
