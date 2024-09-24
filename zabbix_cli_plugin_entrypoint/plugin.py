from zabbix_cli.app import app
from zabbix_cli.config.model import PluginConfig


def __configure__(config: PluginConfig) -> None:
    print("Running configuration for plugin")


@app.command()
def my_command():
    print("Hello, World!")
    config = app.get_plugin_config("zabbix_cli_plugin_entrypoint")
    print(config)
