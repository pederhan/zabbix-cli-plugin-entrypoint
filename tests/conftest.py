from __future__ import annotations

from pathlib import Path

import pytest
from zabbix_cli.config.model import Config
from zabbix_cli.config.model import PluginConfig


def config() -> Config:
    conf = Config.sample_config()
    conf.plugins.root["zabbix_cli_plugin_entrypoint"] = PluginConfig()
    return conf


@pytest.fixture()
def config_file(tmp_path: Path, config: Config) -> Path:
    # Use this fixture if you need to pass in a custom config to a test
    # i.e.
    # subprocess.run(
    #     ["zabbix-cli", "--config", config_path "--help"],
    #     capture_output=True,
    #     text=True,
    # )
    config_file = tmp_path / "config.toml"
    config.dump_to_file(config_file)
    return config_file
