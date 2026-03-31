# remove


systemctl --user stop openclaw-gateway.service
systemctl --user disable openclaw-gateway.service

openclaw uninstall --all --yes --non-interactive 
npm rm -g openclaw.
