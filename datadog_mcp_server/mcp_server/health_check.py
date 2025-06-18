"""Tool for reporting basic server health."""

from __future__ import annotations

from typing import Any, Dict

from . import _state


async def health_check() -> Dict[str, Any]:
    """Return simple health information about the server."""

    return {
        "status": "healthy",
        "contexts_count": len(_state.contexts),
        "datadog_integration": "enabled" if _state.datadog_initialized else "disabled",
    }
