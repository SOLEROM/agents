# comapres


params:

```
gen tok/s   RSS ΔMB   RSS pk    VmHWM    wall s   GR3D    RAMpk   ok 

## gen tok/s (generation tokens per second)
 How fast the model produces output tokens, computed as:
 eval_count / eval_duration

## RSS ΔMB (resident set size delta, MB)
  The increase in Ollama process RAM during inference:
  RSS peak – RSS baseline
  Measured via /proc while the model is running.

## RSS pk (resident set size peak, MB)
  The maximum RAM used by the Ollama process during the run.  
  If this approaches total system RAM → crash risk

## VmHWM (high-water mark RSS, MB)
  Linux-reported peak RSS ever reached by the Ollama process (VmHWM in /proc/<pid>/status).
    RSS pk → measured during this run
    VmHWM → kernel’s lifetime max for the process
  Confirms whether allocator spikes occurred
  Helps detect hidden transient peaks (e.g. during model load)

## wall s (wall-clock seconds)
  Total real time for the request, including:
    model load (if cold)
    prompt processing
    generation
    kernel scheduling delays

## GR3D (Jetson GPU activity peak)
    Peak value reported by tegrastats for: GR3D_FREQ
    Usually a percentage or MHz, depending on JetPack.
    Confirms the model actually used the GPU
    Rough indicator of GPU saturation

## RAMpk (system RAM used peak, MB)
    Peak system-wide RAM usage (from tegrastats, not just Ollama).
    This shows global memory pressure, not just one process.

```

## jetson orion

```

=== SUMMARY ===
Model                         gen tok/s   RSS ΔMB   RSS pk    VmHWM    wall s   GR3D    RAMpk   ok 
---------------------------------------------------------------------------------------------------
llama3.2:latest                    21.25       3.5     113.5    122.4    12.62       -       -  yes
gemma3:latest                      16.97      63.2     143.6    143.8    15.89       -       -  yes
gpt-oss:latest                      7.68      70.1     133.6    133.6    34.18       -       -  yes
gemma3:12b                          7.25      62.8     132.0    132.1    36.19       -       -  yes
gemma3:27b                             -         -         -        -        -       -       -   no

```

## GeForce RTX 2070 

```
Model                         gen tok/s   RSS ΔMB   RSS pk    VmHWM    wall s   GR3D    RAMpk   ok 
---------------------------------------------------------------------------------------------------
llama3.2:3b                        98.79       0.0     116.4    127.4     3.11       -       -  yes
gemma3:4b                          69.98      67.8     142.5    142.5     4.07       -       -  yes
gemma3:12b                         19.33      69.6     146.0    146.0    13.76       -       -  yes
qwen3-coder:30b                    17.96      38.9      98.5     98.5    14.51       -       -  yes
glm-4.7-flash:q4_K_M               14.29      62.2     134.0    134.0    18.28       -       -  yes
gpt-oss:20b                        12.45      69.1     155.5    155.8    21.06       -       -  yes
gemma3:27b                          2.88      63.1     142.8    142.8    89.95       -       -  yes

``` 
