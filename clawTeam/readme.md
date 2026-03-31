# ClawTeam

https://github.com/HKUDS/ClawTeam

## install the tool

TBD

## usage1: skill

using skill : ~/.claude/skills/clawteam

then ``` "Build a web app. Use clawteam to split the work across multiple agents."```

* the skill: https://github.com/HKUDS/ClawTeam/blob/main/skills/clawteam/SKILL.md

## usage2: manual

```
# 1. Create a team (you become the leader)
clawteam team spawn-team my-team -d "Build the auth module" -n leader

# 2. Spawn worker agents — each gets a git worktree, tmux window, and identity
clawteam spawn --team my-team --agent-name alice --task "Implement the OAuth2 flow"
clawteam spawn --team my-team --agent-name bob   --task "Write unit tests for auth"

# 3. Workers auto-receive a coordination prompt that teaches them to:
#    ✅ Check tasks:    clawteam task list my-team --owner alice
#    ✅ Update status:  clawteam task update my-team <id> --status completed
#    ✅ Message leader: clawteam inbox send my-team leader "Done!"
#    ✅ Report idle:    clawteam lifecycle idle my-team

# 4. Watch them work side-by-side
clawteam board attach my-team
```