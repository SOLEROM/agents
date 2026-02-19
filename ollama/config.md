# setup

## install

```
curl -fsSL https://ollama.com/install.sh | sh
```

## set local path

```
mkdir -p  /home/ollama/models
sudo chown -R ollama:ollama /home/ollama

### orid on : /usr/share/ollama/

sudo systemctl stop ollama
sudo EDITOR=vim systemctl edit ollama


[Service]
Environment="OLLAMA_HOME=/home/ollama"
Environment="OLLAMA_MODELS=/home/ollama/models"

sudo systemctl start ollama
sudo systemctl daemon-reload
sudo systemctl restart ollama

```

```
├── blobs
├── id_ed25519
├── id_ed25519.pub
├── manifests
└── models
    ├── blobs
    └── manifests
```
