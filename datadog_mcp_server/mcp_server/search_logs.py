from __future__ import annotations

from datetime import datetime

from anyio import to_thread
from datadog_api_client.v2.api.logs_api import LogsApi

from ._client import _get_client


async def search_logs(
    query: str,
    start: datetime | None = None,
    end: datetime | None = None,
    limit: int | None = None,
) -> list[dict]:
    """Search logs using the Datadog Logs API.

    Args:
        query: Log search query in Datadog syntax.
        start: Optional start time for the query.
        end: Optional end time for the query.
        limit: Maximum number of logs to return per request.

    Returns:
        A list of logs represented as dictionaries.
    """

    def _run() -> list[dict]:
        with _get_client() as api_client:
            api = LogsApi(api_client)
            logs = api.list_logs_get_with_pagination(
                filter_query=query,
                filter_from=start,
                filter_to=end,
                page_limit=limit,
            )
            return [log.to_dict() for log in logs]

    return await to_thread.run_sync(_run)
