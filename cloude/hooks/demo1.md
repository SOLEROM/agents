## demo1

* TypeScript Type Checking Hook
* Runs tsc --noEmit to check for type errors


.claude/settings

```
 "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_response.filePath // .tool_input.file_path // empty' | xargs -I {} npx --yes prettier --write {} 2>/dev/null || true"
          },
          {
            "type": "command",
            "command": "node $PWD/hooks/tsc.js"
          }
        ]
      },

```

tsc.js:

```
...

 // Override to ensure no emit
  const compilerOptions = {
    ...parsed.options,
    noEmit: true,
  };

  // Create the program
  const program = ts.createProgram(parsed.fileNames, compilerOptions);

...
```