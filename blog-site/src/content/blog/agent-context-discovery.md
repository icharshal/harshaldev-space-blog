---
title: "Optimizing AI Agent Context Windows via Structured Discovery Skills"
description: "How to design context discovery instructions to help local code agents navigate repositories, find config parameters, and minimize token costs."
pubDate: "Jun 05 2026"
heroImage: "../../assets/blog-placeholder-1.jpg"
---

Large Language Models now support massive context windows, but sending an entire repository to an LLM for every query is slow and expensive. Moreover, cluttering the context window with irrelevant files can lead to the model "losing" key details in the middle of the prompt.

To solve this, we can write a **Context Discovery Skill** that instructs the agent how to efficiently explore a directory using target commands like `git grep` or directory listings, rather than reading every file blindly.

---

## 🏗️ The Discovery Skill Structure

Instead of letting the agent explore randomly, the discovery skill outlines a step-by-step search strategy to locate key configuration points and business logic.

Let's design a specialized context discovery skill file:

```markdown
# File: .agents/skills/context-discovery.md
# Skill: Project Discovery and Context Search

Use this skill when exploring a new repository or searching for specific components.

## Search Strategy

When asked to modify a feature, follow this checklist to discover context:

### 1. Identify Entry Points
* Read the root `package.json` (Node), `requirements.txt` (Python), or equivalent dependency configuration.
* Locate the main execution files (e.g., `server.js`, `main.py`).

### 2. Search for Symbols
* Use grep commands to search for functions or classes.
  * **Command**: `git grep -n "class CustomController"`
* Do not read entire files; use targeted line ranges (e.g., lines 10-35) to read class definitions.

### 3. Trace Configuration Files
* Find environment variables or configs (e.g., `.env.example`, `config.yaml`).
```

---

## 🔄 Search Workflow

By constraining the discovery flow, the agent saves thousands of tokens on every run:

```
[Incoming Request] ==> [Check Entry Points] ==> [Grep Specific Symbols] ==> [Inspect Small File Ranges]
                                                                                      ||
                                                                                      \/
[Deliver Final Plan] <====================================================== [Load Only Required Files]
```

This prevents the agent from reading unrelated logs, build artifacts, or vendor packages, keeping the prompt clean and responsive.

---

## 🚀 Developer Benefits
* **Cost Efficiency**: Reduces input tokens significantly by avoiding reading bulk code.
* **Accuracy**: The agent focuses on relevant lines of code, reducing hallucinations.
* **Speed**: Faster execution runs due to smaller context sizes.

---

## 💬 Conclusion

Writing explicit instructions on how to explore code structures makes your AI assistants faster and more accurate. Start checking in context discovery guidelines to optimize your development costs today.
