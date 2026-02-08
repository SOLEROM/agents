# agents

## playground 
* [ollama](./ollama/readme.md)
* llama.cpp
* TensorRT
* [claude](./cloude/readme.md)
* [codex](./codex/readme.md)
* opencode
* [openclaw](./openclaw/readme.md)
* [nanochat](./nanochat/readme.md)
* n8n

# Terms

## chatbot
* Generates responses to text/voice prompts

## agents
built around large language models but include additional decision logic and tool access; that can:
* Observes (takes input from the environment),
* Plans/Reason (interprets goals and context),
* Acts (executes tasks and uses tools or interfaces autonomously) / automating workflows.
* Learning or Memory (can persist state across interactions)


## Engines
underlying system that executes models ; agent stack:
* Agent: Makes decisions + orchestrates actions.
* Model: Provides the intelligence (i.e., generates text / reasoning results).
* Tools / APIs: Functions the agent can call (search, calculator, scripts, etc.).

## orchestrators
coordinating multiple parts or agents to accomplish a larger goal

* Managing multiple agents or models
* Sequencing actions
* Handling communication between modules
* Tracking context and state
* Deciding which agent should handle this request
* Maintaining shared context between sub-agents
* Managing error recovery and task dependencies


