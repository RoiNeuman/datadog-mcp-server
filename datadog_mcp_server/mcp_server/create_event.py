from anyio import to_thread
from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest

from ._client import _get_client


async def create_event(title: str, text: str) -> dict:
    """Create a Datadog event.

    Args:
        title: Title of the event.
        text: Body of the event.

    Returns:
        The created event represented as a dictionary.
    """

    def _run() -> dict:
        with _get_client() as api_client:
            api = EventsApi(api_client)
            body = EventCreateRequest(title=title, text=text)
            resp = api.create_event(body)
            return resp.to_dict()

    return await to_thread.run_sync(_run)
