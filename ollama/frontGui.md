# front web gui

##  open-webui
* https://github.com/open-webui/open-webui


```
sudo docker rm -f open-webui 2>/dev/null || true

sudo docker run -d --network host \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main

```

```
admin@admin.admin
admin
```

* WebUI talks to the Ollama server over HTTP (http://127.0.0.1:11434), and the Ollama server loads models from its configured storage.

```
[ Browser ]
     ↓
[ Open WebUI ]   ← persistent UI state (Docker volume)
     ↓ HTTP
[ Ollama daemon ] ← persistent models (OLLAMA_MODELS dir)
     ↓
[ CUDA / CPU ]

```