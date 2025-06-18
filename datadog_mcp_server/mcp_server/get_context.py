"""Tool for retrieving a stored context."""

from __future__ import annotations

from typing import Any, Dict

from . import _state


async def get_context(context_id: str) -> Dict[str, Any]:
    """Retrieve a context by its ID.

    Args:
        context_id: Identifier of the context.

    Returns:
        The stored context or an error message.
    """

    if context_id not in _state.contexts:
        return {"status": "error", "message": "Context ID not found"}
    return _state.contexts[context_id]
