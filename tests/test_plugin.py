from __future__ import annotations

import subprocess

from inline_snapshot import snapshot


def test_plugin_imported(config_file_str: str) -> None:
    result = subprocess.run(
        ["zabbix-cli", "--config", config_file_str, "--help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Sample Plugin" in result.stdout


def test_my_command(config_file_str: str) -> None:
    result = subprocess.run(
        ["zabbix-cli", "--config", config_file_str, "my_command"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "This is an info message" in result.stderr
    assert "This is a success message" in result.stderr
    assert "This is a warning" in result.stderr
    assert "This is an error" in result.stderr
    assert "Command completed successfully" in result.stderr


def test_my_result_command_table(config_file_str: str) -> None:
    result = subprocess.run(
        ["zabbix-cli", "--config", config_file_str, "-o", "table", "my_result_command"],
        capture_output=True,
        text=True,
    )

    assert result.stdout == snapshot(
        """\
╭───────┬──────────┬─────────╮
│ Col1  │ Column 2 │ Col3    │
├───────┼──────────┼─────────┤
│ Hello │ 42       │ a, b, c │
╰───────┴──────────┴─────────╯
"""
    )


def test_my_result_command_json(config_file_str: str) -> None:
    result = subprocess.run(
        ["zabbix-cli", "--config", config_file_str, "-o", "json", "my_result_command"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout == snapshot(
        """\
{
  "message": "",
  "errors": [],
  "return_code": "Done",
  "result": {
    "col1": "Hello",
    "col2": 42,
    "col3": [
      "a",
      "b",
      "c"
    ]
  }
}
"""
    )


def test_my_failing_command(config_file_str: str) -> None:
    result = subprocess.run(
        ["zabbix-cli", "--config", config_file_str, "my_failing_command"],
        capture_output=True,
        text=True,
    )

    assert "Command failed" in result.stderr
    assert result.returncode == 1


def test_command_with_dash(config_file_str: str) -> None:
    result = subprocess.run(
        ["zabbix-cli", "--config", config_file_str, "command-with-dash"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "This command has a generated name" in result.stderr
