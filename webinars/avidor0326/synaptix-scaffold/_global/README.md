# Windsurf Global Rules

> **Meta-configuration for ALL Windsurf projects.**  
> This folder is intentionally separate from `/template/` content.

---

## Contents

| File | Purpose | Version |
|------|---------|---------|
| `windsurf_global_rules.md` | Universal LLM agent behavior rules | 4.1 |

---

## Usage

### For Windsurf IDE
Copy `windsurf_global_rules.md` to your Windsurf global rules location.

### For Projects
Projects reference these rules but don't contain copies. Single source of truth.

---

## Key Concept: Vibes

**1 Vibe = 1,000 tokens** (input + output)

All tasks measured and tracked in Vibes. This is the universal measure for LLM-native development.

---

## Updates

When updating global rules:
1. Edit `windsurf_global_rules.md` in this folder
2. Bump version in the file header
3. Commit with message: `chore(_global): update windsurf rules vX.X`

---

*This folder is version-controlled but separate from project templates.*
