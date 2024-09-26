from __future__ import annotations

from zabbix_cli.app import app
from zabbix_cli.config.model import PluginConfig
from zabbix_cli.logs import logger
from zabbix_cli.output.console import error
from zabbix_cli.output.console import exit_err
from zabbix_cli.output.console import info
from zabbix_cli.output.console import success
from zabbix_cli.output.console import warning
from zabbix_cli.output.render import render_result

CATEGORY = "Sample Plugin"


def __configure__(config: PluginConfig) -> None:
    logger.info("Running configuration for plugin %s", __package__)

    custom_option = config.get("custom_option", "default_value", type=str)
    logger.debug("Got custom_option value: %s", custom_option)
    # Do something with the value here

    # Can mutate the app config using values from the plugin config
    if hostgroups := config.get("hostgroup", [], type=list[str]):
        app.state.config.app.default_hostgroups.extend(hostgroups)

    config.set("some_option", "some_value")


@app.command(name="my_command", rich_help_panel=CATEGORY)
def my_command():
    # We can print independently of the output format
    # All messages go to stderr
    info("This is an info message")
    success("This is a success message")
    warning("This is a warning")
    error("This is an error")

    config = app.get_plugin_config("zabbix_cli_plugin_entrypoint")

    # do some stuff with the config
    success(f"Command completed successfully: {config}")


@app.command(name="my_result_command", rich_help_panel=CATEGORY)
def my_other_command():
    """Renders a result."""
    # Inline import to lazily define Pydantic models
    from zabbix_cli_plugin_entrypoint.results import MyResult

    # Renders Table or JSON depending on the output format
    render_result(MyResult(col1="Hello", col2=42, col3=["a", "b", "c"]))


@app.command(name="my_failing_command", rich_help_panel=CATEGORY)
def my_failing_command():
    # Prints an error message and returns a non-zero exit code
    exit_err("Command failed")

    # Can specify exact code and en exception to pass along
    # exit_err("Command failed", code=123, exception=MyCustomException("Failed"))


@app.command(rich_help_panel=CATEGORY)
def command_with_dash():
    """Typer will generate the name 'command-with-dash' for this command."""
    info("This command has a generated name")
