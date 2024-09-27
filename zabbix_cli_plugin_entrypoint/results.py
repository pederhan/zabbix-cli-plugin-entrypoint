"""Define result types in separate module to speed up application startup.

Import as-needed in each command."""

from __future__ import annotations

from typing import List

from pydantic import Field
from zabbix_cli.models import MetaKey
from zabbix_cli.models import TableRenderable


class MyResult(TableRenderable):
    col1: str
    col2: int = Field(default=..., json_schema_extra={MetaKey.HEADER: "Column 2"})
    col3: List[str] = Field(default=[], json_schema_extra={MetaKey.JOIN_CHAR: ", "})

    # Renders tables in the following format:
    # ╭───────┬──────────┬─────────╮
    # │ Col1  │ Column 2 │ Col3    │
    # ├───────┼──────────┼─────────┤
    # │ Hello │ 42       │ a, b, c │
    # ╰───────┴──────────┴─────────╯
    #               ↑           ↑
    #      Manual header name   │
    #                   Comma-separated instead of newline-separated
