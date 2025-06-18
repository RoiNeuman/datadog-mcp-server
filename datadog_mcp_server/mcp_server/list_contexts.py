"""Tool for listing stored contexts."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import _state


async def list_contexts(model_name: str | None = None, tag: str | None = None) -> List[Dict[str, Any]]:
    """List stored contexts with optional filtering.

    Args:
        model_name: Filter by model name.
        tag: Filter by tag contained in context tags.

    Returns:
        A list of context dictionaries.
    """

    results = list(_state.contexts.values())
    if model_name is not None:
        results = [ctx for ctx in results if ctx["model_name"] == model_name]
    if tag is not None:
        results = [ctx for ctx in results if tag in ctx["tags"]]
    return results
