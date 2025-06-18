# Shared state for context data and Datadog configuration.
from typing import Any, Dict

contexts: dict[str, Dict[str, Any]] = {}

datadog_initialized: bool = False
