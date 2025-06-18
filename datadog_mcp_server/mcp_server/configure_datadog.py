"""Tool for configuring Datadog credentials."""

from __future__ import annotations

import os

from . import _state


async def configure_datadog(api_key: str, app_key: str | None = None, site: str | None = None) -> dict:
    """Configure Datadog client credentials.

    Args:
        api_key: API key for Datadog (sets ``DD_API_KEY``).
        app_key: Optional application key (sets ``DD_APP_KEY``).
        site: Optional Datadog site for API calls.

    Returns:
        Dictionary describing the configuration status.
    """

    os.environ["DD_API_KEY"] = api_key
    if app_key is not None:
        os.environ["DD_APP_KEY"] = app_key
    if site is not None:
        os.environ["DD_SITE"] = site
    # Mark the configuration as loaded
    _state.datadog_initialized = True
    return {"status": "configured", "site": os.environ.get("DD_SITE", "datadoghq.com")}
