"""Tool for creating a new context."""

from __future__ import annotations

from typing import Any, Dict, List

from . import _state


async def create_context(context_id: str, model_name: str, data: Dict[str, Any], tags: List[str] | None = None) -> Dict[str, str]:
    """Create a new context and store it in memory.

    Args:
        context_id: Unique identifier for the context.
        model_name: Name of the model associated with the context.
        data: Context data dictionary.
        tags: Optional list of tags for categorization.

    Returns:
        A dictionary with the operation status and context ID.
    """

    if context_id in _state.contexts:
        return {"status": "error", "message": "Context ID already exists"}

    _state.contexts[context_id] = {
        "context_id": context_id,
        "model_name": model_name,
        "data": data,
        "tags": tags or [],
    }
    return {"status": "created", "context_id": context_id}
