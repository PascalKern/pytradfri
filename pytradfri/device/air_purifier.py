"""Represent an air purifier."""
from __future__ import annotations

from typing import TYPE_CHECKING, cast

from ..const import (
    ATTR_AIR_PURIFIER_AIR_QUALITY,
    ATTR_AIR_PURIFIER_CONTROLS_LOCKED,
    ATTR_AIR_PURIFIER_FAN_SPEED,
    ATTR_AIR_PURIFIER_LEDS_OFF,
    ATTR_AIR_PURIFIER_MODE,
    ROOT_AIR_PURIFIER,
)
from ..resource import TypeRaw, TypeRawList

if TYPE_CHECKING:
    # avoid cyclic import at runtime.
    from . import Device


class AirPurifier:
    """Represent an air purifier."""

    def __init__(self, device: Device, index: int) -> None:
        """Create object of class."""
        self.device = device
        self.index = index

    @property
    def raw(self) -> TypeRaw:
        """Return raw data that it represents."""
        return cast(
            TypeRaw,
            cast(TypeRawList, self.device.raw)[ROOT_AIR_PURIFIER][self.index],
        )

    @property
    def mode(self) -> int:
        """Return the current mode of the air purifier.

        0: off
        1: Fan level auto
        10: Fan level 1
        20: Fan level 2
        30: Fan level 3
        40: Fan level 4
        50: Fan level 5
        """
        return cast(int, self.raw[ATTR_AIR_PURIFIER_MODE])

    @property
    def fan_speed(self) -> int:
        """Get the current fan speed of the air purifier.

        0: Device is off
        10..50: Fan speed with a step size of 5
        """
        return cast(int, self.raw[ATTR_AIR_PURIFIER_FAN_SPEED])

    @property
    def controls_locked(self) -> bool:
        """Return True if physical controls on the air purifier are locked."""
        return self.raw[ATTR_AIR_PURIFIER_CONTROLS_LOCKED] == 1

    @property
    def leds_off(self) -> bool:
        """Return True if led's on the air purifier are turned off."""
        return self.raw[ATTR_AIR_PURIFIER_LEDS_OFF] == 1

    @property
    def air_quality(self) -> int:
        """Get the current air quality measured by the air purifier.

        0..35: Good
        36..85: OK
        86..: Not good
        65535: If the fan is off or during measuring time after turning on
        """
        return cast(int, self.raw[ATTR_AIR_PURIFIER_AIR_QUALITY])
