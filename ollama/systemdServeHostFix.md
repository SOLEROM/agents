# fix to run pubic 0.0.0.0

```
sudo systemctl stop ollama

sudo EDITOR=vi systemctl edit ollama

[Service]
Environment="OLLAMA_HOST=0.0.0.0"

sudo systemctl daemon-reload
sudo systemctl restart ollama


systemctl show ollama | grep OLLAMA_HOST
```
