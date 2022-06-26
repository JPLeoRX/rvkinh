#!/bin/sh
echo $CONTROLLER_URL
echo $CONTROL_API_KEY

cat /app/src/environments/environment.prod.ts

cat >/app/src/environments/environment.prod.ts <<EOL
export const environment = {
  production: true,
  controllerUrl: "${CONTROLLER_URL}",
  controllerApiKey: "${CONTROL_API_KEY}",
};
EOL

cat /app/src/environments/environment.prod.ts



ng serve --host 0.0.0.0 --configuration production --live-reload false --disable-host-check true
