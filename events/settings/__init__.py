from events.settings.base import *

try:
    from events.settings.local import *
except ImportError as e:
    pass