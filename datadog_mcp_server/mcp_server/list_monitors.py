from anyio import to_thread
from datadog_api_client.v1.api.monitors_api import MonitorsApi

from ._client import _get_client


async def list_monitors(
    name: str | None = None,
    tags: str | None = None,
) -> list[dict]:
    """Retrieve monitors configured in Datadog.

    Args:
        name: Optional name used to filter monitors.
        tags: Optional monitor tags for filtering.

    Returns:
        A list of monitors represented as dictionaries.
    """

    def _run() -> list[dict]:
        with _get_client() as api_client:
            api = MonitorsApi(api_client)
            monitors = api.list_monitors(name=name, tags=tags)
            return [m.to_dict() for m in monitors]

    return await to_thread.run_sync(_run)
