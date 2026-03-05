# repetitive errors fix

## add instruction while working

```
stop claude with  :     > ESC
add memory command:     > # ..some instruction..
            then:       > continue

```
## go back in time and fix context
* for a case where it found something that dirty out context
* like missing deps that it needed to debug and install
* now for next repetitve task we want clear context

```
revert to previous msgs:    > ESC + ESC
```

## many dirty context to clear one
* when running multiple simillar task that he learned a lot about them
* and want a clear context with all the knowledge so far compact that to clear context and continue

```
/compact
```
