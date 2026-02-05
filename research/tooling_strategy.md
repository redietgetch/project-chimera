# Tooling & MCP Strategy

## Developer MCP Servers (Dev-time)
These MCP servers help development, debugging, and repository automation.

- `mcp-git` — exposes Git operations (branch, commit, push) via MCP tools for agent-driven repository actions (require explicit human approval for push to main).
- `mcp-fs` — filesystem access with sandboxed root.
- `mcp-sense` — Tenx MCP Sense: telemetry sink for agent actions (MANDATORY).
- `mcp-ci` — simulates CI-run artifacts and test results.
- `mcp-issue` — creates triage tickets when tasks fail.

**Config suggestions**
```yaml
mcp-git:
  allowed_repos: ["your-org/project-chimera"]
  require_human_push: true

mcp-sense:
  endpoint: "https://tenx.example/sense"
  agent_token_env: "MCP_SENSE_TOKEN"
