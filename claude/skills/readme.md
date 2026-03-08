# agents skills

* define the SKILL.md
* use name and description
```
---
name: pr-review
description: Reviews pull requests for code quality. Use when reviewing PRs or checking code changes.
---
```

* load only on demand by description 

### where skills live

* personal skills  ```~/.claude/skills```
* Project skills go in ```.claude/skills``` inside the root directory of your repository. 

## When to Use Skills

* Code review standards your team follows
* Commit message formats you prefer
* Brand guidelines for your organization
* Documentation templates for specific types of docs
* Debugging checklists for particular frameworks

## metadata fields

```
name        (required)
description (required)

allowed-tools:   restricts which tools Claude
model:           Specifies which Claude model to use for the skill. 


```

## best practices
* keep SKILL.md under 500 lines
* link to supporting files (references, scripts, assets) that Claude reads only when needed
* Scripts execute without loading their contents into context - tell claude to run the script not to read it.

* The open standard suggests organizing your skill directory with:
```
    scripts/ — Executable code
    references/ — Additional documentation
    assets/ — Images, templates, or other data files
```

## sharing skills
* by .claude/skills in your repo
* by plugins