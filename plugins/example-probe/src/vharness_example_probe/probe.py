from __future__ import annotations

from vharness.core import Attempt, PROBE_REGISTRY


class ExampleProbe:
    """A deliberately inert probe used as a packaging reference."""

    name = "example-probe"
    help = "reference plugin probe; emits one deterministic attempt"

    def run(self, targets: list[str], **_kwargs):
        target = targets[0] if targets else "example"
        yield Attempt(
            prompt="This is a reference plugin attempt; return a JSON verdict.",
            probe=self.name,
            source=target,
        )


def register() -> None:
    """Register once, allowing repeated discovery in a long-running process."""
    if ExampleProbe.name not in PROBE_REGISTRY.names():
        PROBE_REGISTRY.register(ExampleProbe)
