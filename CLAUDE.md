# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project
Personal portfolio site for Auya — showcasing robotics, drone club, 
molecular docking research, MIT Astrobee, and greenhouse projects.

## Stack
- Python 3 + Flask
- Plain HTML/CSS only — no React, no Vue, no JS frameworks
- Jinja2 templates
- No database needed

## Conventions
- All routes in app.py
- Templates in templates/ folder
- Static files (images, videos) in static/ folder
- Run with: python app.py
- Test with: pytest tests/ -v
- Run a single test: pytest tests/test_routes.py::test_homepage -v

## Rules for Claude
- Always read task files before writing code
- Plan before implementing — use plan mode first
- Run pytest after every substantive change
- Never edit test files to make tests pass
- Contact form is UI-only — no email backend, no external services
- No JavaScript frameworks under any circumstances
- Keep CSS in static/style.css, not inline

## Media
- Images go in static/images/
- Videos go in static/videos/
- Keep file sizes reasonable for a portfolio

## Architecture
- `app.py` — Flask entry point; all routes defined here (no blueprints)
- `templates/base.html` — Jinja2 base layout with nav, header, footer
- `templates/index.html` — Homepage extending base
- `templates/project.html` — Per-project detail page, reused for all 5 projects via route param
- `static/style.css` — All styles; no inline CSS
- `static/images/`, `static/videos/` — Media assets per project

## Out of scope
- User authentication
- Database
- Email sending
- Payment or forms that submit to a backend