# Vharness plugin standard

## Compatibility

Plugins are regular Python distributions and must declare a compatible core range, for example `vharness>=0.2,<0.3`. Treat Vharness public base classes, data models, and documented entry-point protocol as the supported API. Internal modules and registry implementation details are not stable API.

Use an organization prefix for externally visible names (for example, `acme.http-observe`) to avoid collisions. A plugin must expose its own version through normal Python package metadata.

## Registration

Declare one entry point in the `vharness.plugins` group. The target should be a module or object that provides `register_plugins()` and performs all registrations explicitly. Registration must be deterministic and must not make network calls, read credentials, or execute assessment actions.

```toml
[project.entry-points."vharness.plugins"]
acme_http = "vharness_acme_http.plugin"
```

## Design requirements

- Validate configuration at construction time and fail with actionable errors.
- Bound output sizes, timeouts, retries, and concurrency.
- Keep imports inexpensive; defer optional dependency imports until use.
- Never log secrets, authorization headers, or full private targets by default.
- Preserve structured errors rather than converting them into clean results.
- Include unit tests and a `vharness list` discovery check.

## Assessment tools

Tool plugins are more sensitive than pipeline plugins. They accept only typed `ToolAction` objects and return `ToolResult` objects. They must not bypass scope validation, approval gates, rate limits, action budgets, or the action ledger. Those decisions belong to Vharness core, not to plugins or model output.

Declare the intended action category and risk in the plugin README. Start with passive or low-impact capabilities; any state-changing behavior must be explicitly opt-in and auditable.
