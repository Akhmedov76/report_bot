from enum import Enum

from loader import _


class UserStatus(str, Enum):
    active = _("active")
    inactive = _("inactive")


class ReportStatus(str, Enum):
    deactivated = _("deactivated")
    activated = _("activated")

class ReportType(str, Enum):
    income = _("income")
    expense = _("expense")
