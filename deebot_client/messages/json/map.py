"""Map messages."""
from __future__ import annotations

import ast
from typing import TYPE_CHECKING, Any

from deebot_client.events import MapInfoEvent, MapSetType, MapTraceEvent, MinorMapEvent
from deebot_client.logging_filter import get_logger
from deebot_client.message import HandlingResult, HandlingState, MessageBodyDataDict
from deebot_client.util import decompress_7z_base64_data

_LOGGER = get_logger(__name__)

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class OnMapInfoV2(MessageBodyDataDict):
    """On map info message."""

    name = "onMapInfo_V2"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        if data.get("info"):
            coordinates = ast.literal_eval(
                decompress_7z_base64_data(data["info"]).decode()
            )
            coordinates = coordinates[0][1:]
            coordinates = [
                ",".join(
                    [",".join(part.split(",")[0:2]) for part in item.split(";")[1:]]
                )
                for item in coordinates
            ]

            event_bus.notify(
                MapInfoEvent(
                    id=data["mid"],
                    type=data["type"],
                    coordinates=coordinates,
                )
            )

            return HandlingResult.success()

        return HandlingResult.analyse()


class OnMapSetV2(MessageBodyDataDict):
    """On map set v2 message."""

    name = "onMapSet_V2"

    @classmethod
    def _handle_body_data_dict(
        cls, _: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        # check if type is know and mid us given
        if not MapSetType.has_value(data["type"]) or not data.get("mid"):
            return HandlingResult.analyse()

        # NOTE: here would be needed to call 'GetMapSetV2' again with 'mid' and 'type',
        #       that on event will update the map set changes,
        #       messages current cannot call commands again
        return HandlingResult(
            HandlingState.SUCCESS, {"mid": data["mid"], "type": data["type"]}
        )


class OnMapTrace(MessageBodyDataDict):
    """On map trace message."""

    name = "onMapTrace"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        total = int(data["totalCount"])
        start = int(data["traceStart"])

        if not data.get("traceValue"):
            # TODO verify that this is legit pylint: disable=fixme
            return HandlingResult.analyse()

        event_bus.notify(
            MapTraceEvent(start=start, total=total, data=data["traceValue"])
        )
        return HandlingResult(HandlingState.SUCCESS, {"start": start, "total": total})


class OnMinorMap(MessageBodyDataDict):
    """On map minor message."""

    name = "onMinorMap"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        if data.get("type", "ol") == "ol":
            # onMinorMap sends no type, so fallback to "ol"
            event_bus.notify(MinorMapEvent(data["pieceIndex"], data["pieceValue"]))
            return HandlingResult.success()

        return HandlingResult.analyse()
