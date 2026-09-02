# Installing Vharness plugins

Install the core and plugin into the same virtual environment:

```bash
uv pip install vharness vharness-example-probe
vharness list
```

For a local checkout during development:

```bash
uv pip install -e ./plugins/example-probe
vharness list
```

For a private index, configure that index in the consuming project's `pyproject.toml` or your package manager settings, then install the plugin by distribution name.

Plugin code is installed in the Python environment's `site-packages`. Per-user settings belong under the XDG configuration directory (normally `~/.config/vharness`); caches and non-secret data belong under the XDG data directory. Keep credentials in environment variables, a protected OS secret store, or a user-only configuration file—never in a committed plugin config.

Pin core and plugin versions in `uv.lock` for reproducible team and CI runs.
