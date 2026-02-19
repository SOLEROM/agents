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
ollama pull gpt-oss
ollama pull gemma3:12b
ollama pull gemma3:27b
ollama pull gemma3:latest
ollama pull llama3.2:latest
ollama pull glm-4.7-flash



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
python3 ollama_benchmark.py
python3 ollama_benchmark.py --model llama3.2:latest
python3 ollama_benchmark.py --num-predict 256 --warmup 1 --repeats 4 --csv bench.csv --json bench.json
```


