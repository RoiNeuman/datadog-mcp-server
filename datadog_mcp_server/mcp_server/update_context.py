"""Tool for updating an existing context."""

from __future__ import annotations

from typing import Any, Dict, List

from . import _state


async def update_context(context_id: str, model_name: str, data: Dict[str, Any], tags: List[str] | None = None) -> Dict[str, str]:
    """Update a context's values.

    Args:
        context_id: Identifier of the context to update.
        model_name: New model name.
        data: Updated context data.
        tags: Updated list of tags.

    Returns:
        A dictionary with the operation status and context ID.
    """

    if context_id not in _state.contexts:
        return {"status": "error", "message": "Context ID not found"}

    _state.contexts[context_id] = {
        "context_id": context_id,
        "model_name": model_name,
        "data": data,
        "tags": tags or [],
    }
    return {"status": "updated", "context_id": context_id}
