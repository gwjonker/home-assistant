#!/bin/bash

USER="shuser"
PASS="shpasswoord"
DIR="/share/carportcam/FI9900P_00626E944A34/snap/"
WAIT=10       # Number of seconds before turning off sensor

# Tell syslog that we have started
logger "File monitor started!"

inotifywait -m -r -e create --format '%f' "${DIR}" | while read NEWFILE
do
    # Carport. Will detect new files that includes the name "MDAlarm"
    if [[ $NEWFILE == *"MDAlarm"* ]]; then
        TOPIC="homeassistant/carport/motion_sensor"
        # Publish MQTT message ON
        mosquitto_pub -P "$PASS" -u "$USER" -t "$TOPIC" -m "on"
        # Log action to syslog
        logger "Motion detected: Carport."
        # Delete file
        # rm ${DIR}${NEWFILE}
        # Wait $WAIT seconds and publish MQTT message OFF
        sleep $WAIT && mosquitto_pub -P "$PASS" -u "$USER" -t "$TOPIC" -m "off" &
    # Test
    elif [[ $NEWFILE == *"test"* ]]; then
        TOPIC="homeassistant/test/motion_sensor"
        mosquitto_pub -P "$PASS" -u "$USER" -t "$TOPIC" -m "on"
        logger "Motion detected: TEST."
        rm ${DIR}${NEWFILE}
        sleep $WAIT && mosquitto_pub -P "$PASS" -u "$USER" -t "$TOPIC" -m "off" &
    # Unknown file
    else
        echo "Filename $NEWFILE not recognized."
    fi
done