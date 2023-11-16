"""Commands module."""
from deebot_client.command import Command, CommandMqttP2P

from .advanced_mode import GetAdvancedMode, SetAdvancedMode
from .auto_empty import GetAutoEmpty, SetAutoEmpty
from .battery import GetBattery
from .carpet import GetCarpetAutoFanBoost, SetCarpetAutoFanBoost
from .charge import Charge
from .charge_state import GetChargeState
from .clean import Clean, CleanArea, GetCleanInfo
from .clean_count import GetCleanCount, SetCleanCount
from .clean_logs import GetCleanLogs
from .clean_logs_v2 import GetCleanLogsV2
from .clean_preference import GetCleanPreference, SetCleanPreference
from .clear_map import ClearMap
from .common import JsonCommand
from .continuous_cleaning import GetContinuousCleaning, SetContinuousCleaning
from .efficiency import GetEfficiencyMode, SetEfficiencyMode
from .error import GetError
from .fan_speed import GetFanSpeed, SetFanSpeed
from .life_span import GetLifeSpan, ResetLifeSpan
from .map import (
    GetCachedMapInfo,
    GetMajorMap,
    GetMapSet,
    GetMapSubSet,
    GetMapTrace,
    GetMinorMap,
)
from .multimap_state import GetMultimapState, SetMultimapState
from .network import GetNetInfo
from .play_sound import PlaySound
from .pos import GetPos
from .relocation import SetRelocationState
from .stats import GetStats, GetTotalStats
from .true_detect import GetTrueDetect, SetTrueDetect
from .voice_assistant_state import GetVoiceAssistantState, SetVoiceAssistantState
from .volume import GetVolume, SetVolume
from .water_info import GetWaterInfo, SetWaterInfo
from .work_mode import GetWorkMode, SetWorkMode

__all__ = [
    "GetAdvancedMode",
    "SetAdvancedMode",
    "GetAutoEmpty",
    "SetAutoEmpty",
    "GetBattery",
    "GetCarpetAutoFanBoost",
    "SetCarpetAutoFanBoost",
    "GetCleanCount",
    "SetCleanCount",
    "GetCleanPreference",
    "SetCleanPreference",
    "ClearMap",
    "Charge",
    "GetChargeState",
    "Clean",
    "CleanArea",
    "GetCleanInfo",
    "GetCleanLogs",
    "GetCleanLogsV2",
    "GetContinuousCleaning",
    "SetContinuousCleaning",
    "GetEfficiencyMode",
    "SetEfficiencyMode",
    "GetError",
    "GetFanSpeed",
    "SetFanSpeed",
    "GetLifeSpan",
    "ResetLifeSpan",
    "GetCachedMapInfo",
    "GetMajorMap",
    "GetMapSet",
    "GetMapSubSet",
    "GetMapTrace",
    "GetMinorMap",
    "GetMultimapState",
    "SetMultimapState",
    "GetNetInfo",
    "PlaySound",
    "GetPos",
    "SetRelocationState",
    "GetStats",
    "GetTotalStats",
    "GetTrueDetect",
    "SetTrueDetect",
    "GetVoiceAssistantState",
    "SetVoiceAssistantState",
    "GetVolume",
    "SetVolume",
    "GetWaterInfo",
    "SetWaterInfo",
    "GetWorkMode",
    "SetWorkMode",
]

# fmt: off
# ordered by file asc
_COMMANDS: list[type[JsonCommand]] = [
    GetAdvancedMode,
    SetAdvancedMode,

    GetAutoEmpty,
    SetAutoEmpty,

    GetBattery,

    GetCarpetAutoFanBoost,
    SetCarpetAutoFanBoost,

    GetCleanCount,
    SetCleanCount,

    GetCleanPreference,
    SetCleanPreference,

    ClearMap,

    Charge,

    GetChargeState,

    Clean,
    CleanArea,
    GetCleanInfo,

    GetCleanLogs,
    GetCleanLogsV2,

    GetContinuousCleaning,
    SetContinuousCleaning,

    GetEfficiencyMode,
    SetEfficiencyMode,

    GetError,

    GetFanSpeed,
    SetFanSpeed,

    GetLifeSpan,
    ResetLifeSpan,

    GetCachedMapInfo,
    GetMajorMap,
    GetMapSet,
    GetMapSubSet,
    GetMapTrace,
    GetMinorMap,

    GetMultimapState,
    SetMultimapState,

    GetNetInfo,

    PlaySound,

    GetPos,

    SetRelocationState,

    GetStats,
    GetTotalStats,

    GetTrueDetect,
    SetTrueDetect,

    GetVoiceAssistantState,
    SetVoiceAssistantState,

    GetVolume,
    SetVolume,

    GetWaterInfo,
    SetWaterInfo,

    GetWorkMode,
    SetWorkMode
]
# fmt: on

COMMANDS: dict[str, type[Command]] = {
    cmd.name: cmd for cmd in _COMMANDS  # type: ignore[misc]
}

COMMANDS_WITH_MQTT_P2P_HANDLING: dict[str, type[CommandMqttP2P]] = {
    cmd_name: cmd
    for (cmd_name, cmd) in COMMANDS.items()
    if issubclass(cmd, CommandMqttP2P)
}
