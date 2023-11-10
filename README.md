# Envoy frontend + Flask backend Example
## Quick Start

Required docker compose >= `2.23.0`
```
docker compose watch
```

## Fix envoy config
Edit `envoy.yaml`

If you want to use envoy only, fix `compose.yaml` as follows:

```diff
- ./envoy.yaml:/etc/envoy/envoy.yaml
+ ./envoy-only.yaml:/etc/envoy/envoy.yaml
```

## Fix flask app
Edit `app.py` and fix `requirements.txt` if nesessary.
