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
