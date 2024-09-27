# zabbix-cli-plugin-entrypoint

Example plugin for Zabbix-CLI using package entry points.

## Installation

uv:

```bash
uv tool install git+https://github.com/unioslo/zabbix-cli.git@master --with git+https://github.com/pederhan/zabbix-cli-plugin-entrypoint.git@ma
in
```

pipx:

```bash
pipx install git+https://github.com/unioslo/zabbix-cli.git@master
pipx inject zabbix-cli git+https://github.com/pederhan/zabbix-cli-plugin-entrypoint.git@main
```

## Tests

> [!IMPORTANT]
> The tests require a running Zabbix server to connect to. Modify the config constructed in the `config` fixture in `tests/conftest.py` to match your Zabbix test environment. This is a limitation of the CLI design, and will be addressed in the future.

Install test dependencies:

```bash
uv sync --all-extras --dev
# or
pip install -U -e ".[test]"
```

Run tests:

```bash
pytest
```
