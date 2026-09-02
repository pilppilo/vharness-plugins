from vharness.core import PROBE_REGISTRY
from vharness_example_probe.plugin import register_plugins


def test_registers_example_probe():
    register_plugins()
    assert PROBE_REGISTRY.get("example-probe").help.startswith("reference")
