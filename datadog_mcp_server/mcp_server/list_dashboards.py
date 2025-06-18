from anyio import to_thread
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

from ._client import _get_client


async def list_dashboards(
    filter_shared: bool | None = None,
    filter_deleted: bool | None = None,
) -> dict:
    """List dashboards from Datadog.

    Args:
        filter_shared: Whether to include only shared dashboards.
        filter_deleted: Whether to include deleted dashboards.

    Returns:
        The response from Datadog as a dictionary.
    """

    def _run() -> dict:
        with _get_client() as api_client:
            api = DashboardsApi(api_client)
            resp = api.list_dashboards(
                filter_shared=filter_shared,
                filter_deleted=filter_deleted,
            )
            return resp.to_dict()

    return await to_thread.run_sync(_run)
