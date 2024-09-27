from __future__ import annotations

from pathlib import Path

import pytest
from zabbix_cli.config.model import Config
from zabbix_cli.config.model import PluginConfig


@pytest.fixture()
def config() -> Config:
    conf = Config.sample_config()
    # modify this to match your test env
    conf.api.url = "http://localhost:8080"
    conf.api.username = "Admin"
    conf.api.password = "zabbix"  # type: ignore
    conf.plugins.root["zabbix_cli_plugin_entrypoint"] = PluginConfig()
    return conf


@pytest.fixture()
def config_file(tmp_path: Path, config: Config) -> Path:
    config_file = tmp_path / "config.toml"
    config.dump_to_file(config_file)
    return config_file


@pytest.fixture()
def config_file_str(config_file: Path) -> str:
    # Use this fixture if you need to pass in a custom config to a test
    # i.e.
    # subprocess.run(
    #     ["zabbix-cli", "--config", config_file_str "--help"],
    #     capture_output=True,
    #     text=True,
    # )
    return str(config_file)
