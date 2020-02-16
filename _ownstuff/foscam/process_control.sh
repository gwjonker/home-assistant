#!/bin/bash

# Check if script is running. Start it if not.

if ! pgrep -f "/bin/bash /config/_ownstuff/foscam/image_monitor.sh" > /dev/null
then
    /usr/bin/nohup /config/_ownstuff/foscam/image_monitor.sh  > /dev/null 2>&1 &
    echo "Process image_monitor.sh not running. Starting up."
    logger "Process image_monitor was not running. Starting."
else
    echo "Process image_monitor.sh still running."
fi

# # /etc/crontab entry:
# # Process control for scripts
# */5 * * * *     root    /config/_ownstuff/foscam/process_control.sh > /dev/null 2>&1