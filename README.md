# Vharness Plugins

Official examples, templates, and community-maintained extensions for Vharness, the pluggable LLM security harness.

## Install a plugin

Install Vharness and the desired plugin into the same Python environment:

```bash
uv pip install vharness vharness-example-probe
vharness list
```

Vharness discovers installed plugins through the `vharness.plugins` Python entry-point group. No copying into the Vharness installation or configuration directory is required.

## Repository layout

- `docs/` — authoring, compatibility, installation, and security standards.
- `templates/basic-plugin/` — a copyable starting point for a new package.
- `plugins/example-probe/` — a minimal, tested reference implementation.

Each plugin is an independently versioned Python distribution. Publish it to PyPI or a private package index; do not publish the monorepo as one package.

## Author a plugin

Copy `templates/basic-plugin`, rename its package and distribution, implement the relevant Vharness interface, and register it via an entry point. See [the plugin standard](docs/plugin-standard.md) and [installation guidance](docs/installation.md).

## Development

```bash
cd plugins/example-probe
uv sync --group dev
uv run pytest
```

## Security reporting

Do not open a public issue for a vulnerability that could affect an active assessment target, plugin credentials, or the core harness. Contact the maintainers privately and include reproduction steps, affected versions, and impact.
