#!/bin/sh

# Check the variables exist
echo $CONTROLLER_URL
echo $CONTROL_API_KEY

# Check initial config
cat /app/src/environments/environment.prod.ts

# Replace config
cat >/app/src/environments/environment.prod.ts <<EOL
export const environment = {
  production: true,
  controllerUrl: "${CONTROLLER_URL}",
  controllerApiKey: "${CONTROL_API_KEY}",
};
EOL

# Check resuling config
cat /app/src/environments/environment.prod.ts

# Run the app
ng serve --host 0.0.0.0 --configuration production --live-reload false --disable-host-check true
