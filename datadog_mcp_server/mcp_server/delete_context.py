"""Tool for deleting a context."""

from __future__ import annotations

from typing import Dict

from . import _state


async def delete_context(context_id: str) -> Dict[str, str]:
    """Delete a context from storage.

    Args:
        context_id: Identifier of the context.

    Returns:
        A dictionary with the operation status and context ID.
    """

    if context_id not in _state.contexts:
        return {"status": "error", "message": "Context ID not found"}

    del _state.contexts[context_id]
    return {"status": "deleted", "context_id": context_id}
