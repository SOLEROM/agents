#

## install

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

```
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


* run `openclaw doctor` to review skills + requirements.

* control : http://127.0.0.1:18789

* local config: ~/.openclaw/openclaw.json


### telegram 

* add apikey ; get user id and Approve a sender

```
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

## restart

systemctl --user restart openclaw-gateway.service


## stop

systemctl --user stop openclaw-gateway.service
systemctl --user disable openclaw-gateway.service

