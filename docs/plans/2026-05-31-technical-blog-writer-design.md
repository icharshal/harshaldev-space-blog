# Technical Blog Writer — Design Document

## Goal
Build a dedicated system for generating high-quality technical blogs focused on AI Agents and Python Automation, with Astro hosted on GitHub Pages and a custom domain configured via Hostinger DNS automation.

## Project Structure
We will create a new directory `d:\mygithub\technical-blog-writer\` with the following structure:
* `.agents/agent.md`: The system prompt defining the AI Technical Writer persona.
* `.agents/skills/blog-writing.md`: Guidelines and structures for high-quality technical writing.
* `blog-site/`: The Astro site containing the layout and pages.
* `hostinger_dns.py`: A Playwright automation script to configure Hostinger DNS.

## DNS Custom Domain Configuration
Point `harshaldev.space` to GitHub Pages:
* A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
* CNAME record: `www` pointing to `<username>.github.io`

## GitHub MCP Integration
Use GitHub MCP server to:
1. Create a repository on GitHub.
2. Initialize files and push them.
3. Keep the codebase synced.
