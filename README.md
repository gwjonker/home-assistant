# home-assistant
My Home Assistant config

Todo:
  * [x] carport detection weer aanzetten en analyseren wat fout gaat
  * [x] overloop lamp op 50% zetten als van unavailable naar off of aan
  * [x] opschoonscripts werkend maken
  * [ ] als poort nog open en Jonkertjes slapen, dan flashing lights
  * [ ] knoppen afstandsbediening koppelen aan scenes
  * [ ] testje met colorloop kantoorlamp
  * [x] melding als disk use% > x
  * [x] meld disk usage / free pre en post opschoonscripts
  * [x] lamp overloop alleen overdag op 50% zetten als eerst unavailable (dus niet s'nachts)
  * [x] lamp overloop 's nachts op 10% zetten als per ongeluk aan/uit gezet via lichtknop
  * [ ] sync camera beelden/videos naar cloud en zet link in slack
  * [ ] warning als camera buiten uit + koppeling met armed/beveiliging
  * [ ] solve issues
    * [x] buienradar [buienradar.buienradar_json] Data element with key='barometerfc' not loaded from br data!
    * [ ] recorder [homeassistant.components.recorder.util] Error executing query: (sqlite3.OperationalError) database is locked
    * [x]    Update of sensor.droger_aan_vandaag is taking over 10 seconds
    * [x]    Update of sensor.droger_aan_vanaf_begin is taking over 10 seconds
    * [x]    Update of sensor.lampen_aan_vandaag is taking over 10 seconds
    * [x]    Update of sensor.tv_aan_vanaf_begin is taking over 10 seconds
    * [x]    Update for sensor.tv_aan_deze_week fails
    * [ ]    (stream_worker) [libav.h264] Missing reference picture, default is 65546 --> FOSCAM