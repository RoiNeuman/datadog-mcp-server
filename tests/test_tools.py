import contextlib
import types
import asyncio

import pytest

from datadog_mcp_server.mcp_server import (
    create_event,
    list_dashboards,
    list_monitors,
    search_logs,
)


class DummyResp:
    def __init__(self, data):
        self._data = data

    def to_dict(self):
        return self._data


import importlib


def test_list_dashboards(monkeypatch):
    result_data = {"ok": True}

    class FakeDashboardsApi:
        def __init__(self, client):
            self.client = client
            assert client == "client"

        def list_dashboards(self, *, filter_shared=None, filter_deleted=None):
            assert filter_shared is True
            assert filter_deleted is False
            return DummyResp(result_data)

    async def fake_run_sync(func, *args, **kwargs):
        return func(*args, **kwargs)

    mod = importlib.import_module("datadog_mcp_server.mcp_server.list_dashboards")
    monkeypatch.setattr(mod, "_get_client", lambda: contextlib.nullcontext("client"))
    monkeypatch.setattr(mod, "DashboardsApi", FakeDashboardsApi)
    monkeypatch.setattr(mod, "to_thread", types.SimpleNamespace(run_sync=fake_run_sync))

    result = asyncio.run(list_dashboards(filter_shared=True, filter_deleted=False))
    assert result == result_data


def test_list_monitors(monkeypatch):
    result_list = [DummyResp({"id": 1}), DummyResp({"id": 2})]

    class FakeMonitorsApi:
        def __init__(self, client):
            assert client == "client"

        def list_monitors(self, *, name=None, tags=None):
            assert name == "foo"
            assert tags == "tag:bar"
            return result_list

    async def fake_run_sync(func, *args, **kwargs):
        return func(*args, **kwargs)

    mod = importlib.import_module("datadog_mcp_server.mcp_server.list_monitors")
    monkeypatch.setattr(mod, "_get_client", lambda: contextlib.nullcontext("client"))
    monkeypatch.setattr(mod, "MonitorsApi", FakeMonitorsApi)
    monkeypatch.setattr(mod, "to_thread", types.SimpleNamespace(run_sync=fake_run_sync))

    result = asyncio.run(list_monitors(name="foo", tags="tag:bar"))
    assert result == [{"id": 1}, {"id": 2}]


def test_create_event(monkeypatch):
    returned = {"ok": True}

    class FakeEventsApi:
        def __init__(self, client):
            assert client == "client"

        def create_event(self, body):
            assert body.title == "t"
            assert body.text == "x"
            return DummyResp(returned)

    async def fake_run_sync(func, *args, **kwargs):
        return func(*args, **kwargs)

    mod = importlib.import_module("datadog_mcp_server.mcp_server.create_event")
    monkeypatch.setattr(mod, "_get_client", lambda: contextlib.nullcontext("client"))
    monkeypatch.setattr(mod, "EventsApi", FakeEventsApi)
    monkeypatch.setattr(mod, "to_thread", types.SimpleNamespace(run_sync=fake_run_sync))

    result = asyncio.run(create_event("t", "x"))
    assert result == returned


def test_search_logs(monkeypatch):
    logs = [DummyResp({"message": "hi"})]

    class FakeLogsApi:
        def __init__(self, client):
            assert client == "client"

        def list_logs_get_with_pagination(self, *, filter_query, filter_from=None, filter_to=None, page_limit=None):
            assert filter_query == "q"
            assert filter_from == 1
            assert filter_to == 2
            assert page_limit == 3
            return logs

    async def fake_run_sync(func, *args, **kwargs):
        return func(*args, **kwargs)

    mod = importlib.import_module("datadog_mcp_server.mcp_server.search_logs")
    monkeypatch.setattr(mod, "_get_client", lambda: contextlib.nullcontext("client"))
    monkeypatch.setattr(mod, "LogsApi", FakeLogsApi)
    monkeypatch.setattr(mod, "to_thread", types.SimpleNamespace(run_sync=fake_run_sync))

    result = asyncio.run(search_logs("q", start=1, end=2, limit=3))
    assert result == [{"message": "hi"}]


def test_entrypoint_name():
    import tomllib
    import pathlib
    data = tomllib.loads(pathlib.Path("pyproject.toml").read_text())
    scripts = data.get("project", {}).get("scripts", {})
    assert "datadog_mcp_server" in scripts
    assert "enrichai" not in scripts


def test_main_docstring_no_enrichai():
    import pathlib

    text = pathlib.Path("datadog_mcp_server/__main__.py").read_text()
    assert "enrichai" not in text
