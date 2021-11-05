import io
import pytest
from charmonium.async_subprocess import run


@pytest.mark.asyncio
async def test_run() -> None:
    assert (
        await run(
            ["pwd"],
            cwd="/tmp",
            capture_output=True,
            text=True,
        )
    ).stdout == "/tmp\n"
    assert (
        await run(
            ["env"],
            env={"a": "b"},
            capture_output=True,
            text=True,
        )
    ).stdout == "a=b\n"
