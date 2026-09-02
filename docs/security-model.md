# Plugin security model

Installing a plugin installs executable Python code. Review its source, publisher, release history, and dependency tree before installation. Prefer version-pinned releases from an index you trust.

Plugins may extend model pipeline stages, but assessment-tool plugins must remain behind Vharness's central scope, policy, approval, budget, and audit controls. A plugin cannot make an out-of-scope action authorized.

Plugin discovery must be side-effect free: imports and registration cannot perform requests, subprocess execution, target discovery, or credential use.
