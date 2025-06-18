"""Tool for executing a mock query against a context."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

from . import _state


async def query_model(context_id: str, query_data: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a simple query against a stored context.

    Args:
        context_id: Identifier of the context.
        query_data: Arbitrary query parameters.

    Returns:
        Dictionary representing query results or an error.
    """

    if context_id not in _state.contexts:
        return {"status": "error", "message": "Context ID not found"}

    context = _state.contexts[context_id]
    return {
        "context_id": context_id,
        "model_name": context["model_name"],
        "query": query_data,
        "result": {"processed": True, "timestamp": datetime.utcnow().isoformat()},
    }
