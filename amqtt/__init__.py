# See the file license.txt for copying permission.
from importlib.metadata import version, PackageNotFoundError

try:
    __version__: str = version("amqtt")
except PackageNotFoundError:  # pragma: no cover
    __version__: str = "unknown"
finally:
    del version, PackageNotFoundError
