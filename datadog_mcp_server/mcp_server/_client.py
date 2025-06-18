from datadog_api_client import ApiClient, Configuration
from dotenv import load_dotenv

load_dotenv()


def _get_client() -> ApiClient:
    """Create a Datadog API client using environment configuration.

    The client reads ``DD_API_KEY`` and ``DD_APP_KEY`` from environment variables.
    These variables are loaded from a ``.env`` file if present. Existing
    environment variables take precedence over values defined in ``.env``.

    Returns:
        Configured :class:`ApiClient` instance.
    """

    return ApiClient(Configuration())
