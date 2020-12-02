# ckw-ha-mqtt

Schickt PiFace Digital Daten via mqtt an einen mqtt-Broker und man kann somit via 
Homeassistant den Raspi steuern bzw. den Status der Ports abfragen. 

Für Python 2.x

# Vorarbeiten

## Hardware

- Raspberry Pi 1
- PiFace Digital

## Software

- Raspberry Pi OS auf SD-Karte
- SD-Karte in PC > leere "ssh"-Datei in boot-Partition erstellen
- Python 2.x

# Installation auf Raspberry Pi 1

## Konfiguration Raspi

```
sudo raspi-config
```

- Network Option > Hostname > "pischeune"
- Interfacing Options > SPI > enable
- reboot

### Installation Softwarepakete

```
sudo apt install screen git python-pip
sudo pip install pifacecommon
sudo pip install pifacedigitalio
sudo pip install paho-mqtt
```

### Installation ckw-ha-mqtt

```
mkdir ~/src/
cd ~/src/
git clone https://github.com/ckarrie/ckw-ha-mqtt
```

### Usage

```
python ~/src/ckw-ha-mqtt/mqtt.py -i <IP Adress of MQTT broker> -t <MQTT root opic>
```

- `-i` = IP-Adresse des MQTT-Brokers (z.B. mosquitto), Default ist `192.168.178.71`
- `-t` = Wurzel-Topic der MQTT-Message, Default ist `winden`

### Tests

```
python ~/src/ckw-ha-mqtt/test_piface.py
```

- Press a button (input button) on the PiFace Digital board to get messages like:

    ```
    pi@pischeune:~ $ python test_piface.py 
    [2020-12-02 14:29:12.932129] Switch 0 pressed
    [2020-12-02 14:29:15.339102] Switch 0 released
    [2020-12-02 14:29:18.342504] Switch 2 pressed
    [2020-12-02 14:29:18.959153] Switch 2 released
    [2020-12-02 14:29:21.842271] Switch 1 pressed
    [2020-12-02 14:29:22.525871] Switch 1 released
    [2020-12-02 14:29:25.063868] Switch 3 pressed
    [2020-12-02 14:29:26.353478] Switch 3 released
    ```        
    
## Integration in Homeassistant

