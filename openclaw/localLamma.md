# local with lamma

## test1: local mini

* test1: https://ollama.com/library/nemotron-3-nano (nemotron-3-nano:30b // 24 GB // 1M context)


```
ollama pull nemotron-3-nano:30b 
curl -fsSL https://openclaw.ai/install.sh | bash

ollama launch openclaw --model nemotron-3-nano:30b 


openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

## test2: coder local

```
ollama pull qwen3-coder:30b

ollama launch openclaw --model qwen3-coder:30b

openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

## test3: cloud super

* https://ollama.com/library/nemotron-3-super

```
ollama pull nemotron-3-super:cloud
curl -fsSL https://openclaw.ai/install.sh | bash

ollama launch openclaw --model nemotron-3-super:cloud

openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

```
>ollama run nemotron-3-super:cloud
Connecting to 'nemotron-3-super' on 'ollama.com' ⚡
> 
```

```
> openclaw agent --agent main --local -m "what model do we use?"

🦞 OpenClaw 2026.3.13 (61d171a) — One CLI to rule them all, and one more restart because you changed the port.

11:56:02 [tools] tools.profile (coding) allowlist contains unknown entries (apply_patch, image). These entries a
```