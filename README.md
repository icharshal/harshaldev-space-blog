# Technical Blog Writer & Publisher

An automated, version-controlled technical blog writing and deployment system designed for generating high-quality engineering guides on AI Agents and Cloud Automation, hosted on GitHub Pages with a custom domain (`harshaldev.space`).

This workspace contains both the **Astro-based frontend blog codebase** and the **AI Agent System instructions** that guide coding assistants to write clean, structured articles.

---

## 🏗️ Repository Architecture

```text
technical-blog-writer/
├── .agents/
│   ├── agent.md                  # Persona and style constraints for the AI Blog Writer
│   └── skills/
│       └── blog-writing.md       # Repeatable guidelines for structuring posts
├── .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions workflow for automatic deployment
├── blog-site/                    # Astro blog static site project
│   ├── src/
│   │   ├── content/
│   │   │   └── blog/             # Co-located blog post folders
│   │   └── pages/                # Pages (index.astro, about.astro, etc.)
│   └── public/
│       └── CNAME                 # Custom domain configuration file (harshaldev.space)
├── docs/                         # Planning and design specifications
└── hostinger_dns.py              # Playwright helper script for Hostinger DNS setup
```

---

## 🚀 How the System is Setup

1. **Astro Static Frontend**: Built with the Astro static site generator, styled with custom premium dark-mode CSS (`src/styles/global.css`) using modern typography (**Outfit** and **Plus Jakarta Sans**).
2. **Custom Domain Binding**: Configured via the `public/CNAME` file pointing to `harshaldev.space`, resolving to GitHub Pages using Hostinger DNS A/CNAME configurations.
3. **Continuous Deployment (CI/CD)**: Set up using GitHub Actions. Pushing commits to the `main` branch triggers a workflow runner (Node.js v22) that installs dependencies, compiles the site, and deploys the output to GitHub Pages instantly.

---

## ✍️ How to Write a Blog Post (Standard Workflow)

To publish a new article, create a dedicated folder under the content directory so that all assets are co-located:

### Step 1: Create a Post Directory
Create a new directory named after your post's slug:
```bash
mkdir blog-site/src/content/blog/your-post-slug
```

### Step 2: Add Post Content (`index.md`)
Create an `index.md` inside that directory and configure the YAML frontmatter:
```markdown
---
title: "Your Post Title Here"
description: "A short, engaging description for SEO cards."
pubDate: "Jun 01 2026"
heroImage: "./your-custom-image.png"
---

Your markdown blog body starts here...
```

### Step 3: Co-locate Assets
Place any images or custom assets directly inside the `blog-site/src/content/blog/your-post-slug/` folder, and reference them in frontmatter or post body using local relative paths (e.g., `./your-custom-image.png`).

---

## 🤖 Automating Writing Using the AI Agent

If you are pair-programming with an AI assistant (like Claude Code or Gemini), instruct the tool to read the agent profile and skills to ensure consistent formatting:

> *"Please read `.agents/agent.md` and `.agents/skills/blog-writing.md` to align with my writing style, and then draft an article inside `blog-site/src/content/blog/<slug>/index.md`."*

The agent will automatically follow the structured templates, outline technical architectures using ASCII diagrams, generate clean, complete code snippets, and exclude duplicate titles from the post body.

---

## 🚢 Publishing Your Post

Once you've written the file and added your images, run these standard Git commands to publish:

```bash
git add .
git commit -m "Publish: <your post title>"
git push origin main
```

Within 1-2 minutes, GitHub Actions will compile your site and make it live on **[https://harshaldev.space](https://harshaldev.space)**!
