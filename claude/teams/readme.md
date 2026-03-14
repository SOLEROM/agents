# agent-teams

## refs
* https://code.claude.com/docs/en/agent-teams
* https://github.com/coleam00/context-engineering-intro/tree/main/use-cases/build-with-agent-team
* [team vs subagent](./vsSub.md)

## use cases

Agent teams are most effective for tasks where parallel exploration adds real value


* Research and review: multiple teammates can investigate different aspects of a problem simultaneously, then share and challenge each other’s findings
* New modules or features: teammates can each own a separate piece without stepping on each other
* Debugging with competing hypotheses: teammates test different theories in parallel and converge on the answer faster
* Cross-layer coordination: changes that span frontend, backend, and tests, each owned by a different teammate



## enable

* Enable them by adding CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS to your settings.json

```
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

```
settings.json
=============
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}

```

## calling

#### direct instructions:

```
some task .... then instruct ... Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.

```

```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

#### lead’s judgment

```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

```
“only approve plans that include test coverage”
“reject plans that modify the database schema.”

```

```
Wait for your teammates to complete their tasks before proceeding
```

#### for PR:

```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

#### Investigate with competing hypotheses

```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```



## finish

```
Ask the researcher teammate to shut down
```

```
Clean up the team
```

## Architecture

Component:
* Team lead	- The main Claude Code session that creates the team, spawns teammates, and coordinates work
* Teammates	- Separate Claude Code instances that each work on assigned tasks
* Task list	- Shared list of work items that teammates claim and complete
* Mailbox	- Messaging system for communication between agents

```
    Team config: ~/.claude/teams/{team-name}/config.json
    Task list: ~/.claude/tasks/{team-name}/
```

*  When spawned, a teammate loads the same project context as a regular session
