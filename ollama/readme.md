# ollama

* https://ollama.com/search
* [config local](./config.md)
* [web gui](./frontGui.md)

## basic usage

```
> ollama pull  xxx
> ollama list
> ollama run gemma3:27b

```
pulls
```
ollama pull gpt-oss:20b
ollama pull gemma3:12b
ollama pull gemma3:27b
ollama pull gemma3:4b
ollama pull llama3.2:3b
ollama pull glm-4.7-flash:q4_K_M
ollama pull qwen3-coder:30b


```


## banchmarks
* [see banchmarks results log](banchmarks_results.md)


### test latency and memory footprint

* deps
```
pip install requests transformers sentencepiece psutil

```

* runs

```
sudo python3 ollama_benchmark.py
sudo python3 ollama_benchmark.py --model llama3.2:latest
sudo python3 ollama_benchmark.py --num-predict 256 --warmup 1 --repeats 4 --csv bench.csv --json bench.json
```


