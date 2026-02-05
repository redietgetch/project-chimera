# Project Chimera – Meta Specification

## Project Overview
Project Chimera is an Autonomous Influencer Infrastructure designed to:
- Research emerging social media trends
- Generate AI-driven content
- Publish and manage engagement autonomously
- Operate within an Agent Social Network (OpenClaw)

This repository defines the FACTORY — not the influencer itself.

Agents entering this codebase must follow Spec-Driven Development.

---

## Architectural Philosophy
- Specification First
- No implementation before ratified specs
- Human-in-the-loop safety enforcement
- Modular Agent Skills
- Full traceability through MCP telemetry

---

## Constraints
- Agents MUST read `/specs` before generating code
- Skills MUST define input/output contracts
- All APIs MUST use JSON
- Infrastructure must be containerized
- All automation MUST pass CI governance

---

## System Components
1. Trend Research Agent
2. Content Generation Agent
3. Publishing & Engagement Agent
4. Human Safety Layer
5. MCP Observability Layer
6. OpenClaw Social Presence Layer

---

## Non-Goals
- No direct UI development
- No hard-coded prompts
- No unmanaged agent autonomy

---

## Prime Directive
"Specifications are the source of truth. Implementation is a downstream artifact."
