#!/usr/bin/env bash
set -e

echo "== Stop user services =="
systemctl --user stop openclaw-gateway.service 2>/dev/null || true
systemctl --user disable openclaw-gateway.service 2>/dev/null || true

# kill any remaining processes
pkill -f openclaw || true
pkill -f nemoclaw || true
pkill -f openshell || true

echo "== Remove systemd user service files =="
rm -f ~/.config/systemd/user/openclaw-gateway.service
systemctl --user daemon-reexec
systemctl --user daemon-reload

echo "== Remove CLI binaries (if installed in common locations) =="
rm -f ~/.local/bin/openclaw
rm -f ~/.local/bin/nemoclaw
rm -f ~/.local/bin/openshell

# optional: if installed globally
sudo rm -f /usr/local/bin/openclaw 2>/dev/null || true
sudo rm -f /usr/local/bin/nemoclaw 2>/dev/null || true
sudo rm -f /usr/local/bin/openshell 2>/dev/null || true

echo "== Remove configs and state =="
rm -rf ~/.openclaw
rm -rf ~/.nemoclaw
rm -rf ~/.config/openclaw
rm -rf ~/.config/nemoclaw

echo "== Remove Docker containers/images related to claw =="
docker ps -a --format '{{.ID}} {{.Image}} {{.Names}}' | grep -E 'claw|openshell' || true

# remove containers
docker ps -a --format '{{.ID}} {{.Image}} {{.Names}}' | \
  grep -E 'claw|openshell' | awk '{print $1}' | \
  xargs -r docker rm -f

# remove images
docker images --format '{{.Repository}}:{{.Tag}} {{.ID}}' | \
  grep -E 'claw|openshell' | awk '{print $2}' | \
  xargs -r docker rmi -f

echo "== Remove Docker volumes (optional, comment if unsure) =="
docker volume ls | grep -E 'claw|openshell' | awk '{print $2}' | xargs -r docker volume rm

echo "== Clean leftover ports (8080 etc) =="
lsof -i :8080 || true

echo "== Done. Recommend logout/login or reboot =="
