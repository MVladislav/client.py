"""Auto empty command module."""
from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from deebot_client.command import InitParam
from deebot_client.events import AutoEmptyMode, AutoEmptyModeEvent
from deebot_client.message import HandlingResult

from .common import JsonGetCommand, JsonSetCommand

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class GetAutoEmpty(JsonGetCommand):
    """Get auto empty command."""

    name = "getAutoEmpty"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        event_bus.notify(
            AutoEmptyModeEvent(
                enable=bool(data["enable"]),
                mode=AutoEmptyMode(str(data["frequency"])),
            )
        )
        return HandlingResult.success()


class SetAutoEmpty(JsonSetCommand):
    """Set auto empty command."""

    name = "setAutoEmpty"
    get_command = GetAutoEmpty
    _mqtt_params = MappingProxyType(
        {"enable": InitParam(bool), "frequency": InitParam(AutoEmptyMode)}
    )

    def __init__(
        self,
        enable: bool = True,  # noqa: FBT001, FBT002
        frequency: AutoEmptyMode | str | None = None,
    ) -> None:
        args: dict[str, int | str] = {"enable": int(enable)}
        if frequency is not None:
            if isinstance(frequency, str):
                frequency = AutoEmptyMode.get(frequency)
            args["frequency"] = frequency.value

        super().__init__(args)
