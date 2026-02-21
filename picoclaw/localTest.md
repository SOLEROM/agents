# test on composer

## build the src

```
# 1. Clone this repo
git clone https://github.com/sipeed/picoclaw.git
cd picoclaw

# 2. Set your API keys
cp config/config.example.json config/config.json
vim config/config.json      # Set DISCORD_BOT_TOKEN, API keys, etc.

# 3. Build & Start
docker compose --profile gateway up -d

# 4. Check logs
docker compose logs -f picoclaw-gateway


//get shell
docker exec -it picoclaw-gateway sh

# 5. Stop
docker compose --profile gateway down
```

## test with local

(1) run local ollama (0.0.0.0) 


```
OLLAMA_HOST=0.0.0.0:11434 ollama serve
ollama pull qwen3:0.6b

//test working
curl http://localhost:11434/api/tags


```

(2) config to use that

```
cp docker-compose.yml_localFix to local src prj
cp config.json_local to <picoclaw>/config/config.json
```


## build the src

```
# 1. Clone this repo
git clone https://github.com/sipeed/picoclaw.git
cd picoclaw

# 2. Set your API keys
cp config/config.example.json config/config.json
vim config/config.json      # Set DISCORD_BOT_TOKEN, API keys, etc.

# 3. Build & Start
docker compose --profile gateway up -d

# 4. Check logs
docker compose logs -f picoclaw-gateway


//get shell
docker exec -it picoclaw-gateway sh

# 5. Stop
docker compose --profile gateway down
```



### run agent

```
# Ask a question
docker compose run --rm picoclaw-agent -m "What is 2+2?"

# Interactive mode
docker compose run --rm picoclaw-agent

```
