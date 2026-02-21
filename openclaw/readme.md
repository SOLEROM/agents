# openclaw 🦞

* https://docs.openclaw.ai/

## install

```
curl -fsSL https://openclaw.ai/install.sh | bash

//Run the onboarding wizard
openclaw onboard --install-daemon

//Check the Gateway
openclaw gateway status

//Open the Control UI
openclaw dashboard
openclaw status


//more config
openclaw configure

```

### security audit
```
openclaw security audit
openclaw security audit --deep
openclaw security audit --fix
```

### configure caddy as reverse proxy 

```
sudo apt install -y gnupg ca-certificates
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' \
  | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' \
  | sudo tee /etc/apt/sources.list.d/caddy-stable.list >/dev/null
sudo apt update
sudo apt install -y caddy


/etc/caddy/Caddyfile
openclaw.lan {
  reverse_proxy 127.0.0.1:18789
}

sudo systemctl reload caddy
sudo systemctl status caddy
```

### access using token over https

```
/etc/hosts
==========
x.y.z.t   openclaw.lan      //of the running device
```


```
surf using token
grep token ~/.openclaw/openclaw.json
https://openclaw.lan/#token=....
```

### pairing required

```
openclaw devices list
openclaw devices approve  <req from list>
```
