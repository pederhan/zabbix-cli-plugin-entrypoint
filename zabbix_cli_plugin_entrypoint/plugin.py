from zabbix_cli.app import app
from zabbix_cli.config.model import PluginConfig


def __configure__(config: PluginConfig) -> None:
    print("Running configuration for plugin")


@app.command()
def my_command():
    print("Hello, World!")
    conf_opt = app.get_plugin_config()
    print(conf_opt)
