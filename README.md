# Minimalbeispiel für Datenaustausch zwischen ROS2 und Codesys via OPC UA
Das Ziel ist es mithilfe von **turlesim** den Datenaustausch zwischen ROS2 und Codesys darzustellen und zu erlernen wie OPC UA dafür eingebaut und genutzt werden kann.
turtlesim ist ein Einsteigertool um ROS2 Konzepte zu erlernen.
Das Gesamtsystem besteht aus:
* ROS2 Simulation turtlesim
* OPC UA Brücke(asyncua)
* Codesys VSPS und Visualisierung


# Installation and Usage
0. github in wsl workspace clonen
´´´
git clone https://github.com/DanielK16/Minimalexample_ROS2_Codesys.git
´´´
1. image bauen mit Dockerfile:
```
docker build -t <image_name> .
```
2. image -> container
´´´
docker run -it \
  --name minimalbsp_ros2_codesys \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ~/Minimalexample_ROS2_Codesys:/Minimalexample_ROS2_Codesys \
  <image_name> \
  /bin/bash
```
3. Codesys Projekt öffnen und mit Deploy Tool Container einrichten

# Entwicklungsumgebung
|Tool|Version|Befehl zum Prüfen|
|---|---|---|
|Host Betriebssystem|WIN11|winver|
|Subsystem|WSL2: Ubuntu-24.04 | wsl -l -v|	
|Container Plattform|Docker Desktop 4.88.1|docker version|	
|SPS Entwicklungsumgebung|Codesys Development V3.5 SP22 Patch 2|Codesys Installer |
|SPS Runtime| CODESYS Virtual Runtime for Linux SL|Codesys Installer|
|ROS Distribution	|ROS2 Jazzy| echo $ROS_DISTRO|
|Versionsverwaltung|git 2.43.0| git --version|

![Entwicklungsumgebung Aufbau](/doc/img/Aufbau_Entwicklungsumgebung.png)

# Datenaustausch ROS2 und Codesys
Für Datenaustausch zwischen ROS2 und Codesys gibt es generell 3 Möglichkeiten:
- Shared Memory (IPC) -> z.B: ROBIN Projekt
- Feldbusse (ModbusTCP, EtherCAT, ...)
- Netzwerkprotokolle (OPC UA, MQTT, rosbridge)

Entschieden für OPC UA, da industrieller Standard und "einfach" zu implementieren.
![Datenaustausch ROS2 und Codesys](/doc/img/Datenaustausch_Codesys_ROS2.png)

Für OPC UA wird die asyncua Bibliothek verwendet.


# Beispiel
![Beispielsdarstellung](/doc/vid/codesys_ros2_minimalbeispiel.gif)

In diesem Beispiel wird der Datenaustausch wird der Datenaustausch in beide Richtungen getestet:
Einmal von ROS2 -> Codesys: In diesem Fall wird die Position der Schildkröte übertragen und in Codesys angezeigt.
Dabei wird zunächst auf das topic /tutle1_pose subscribed und dann die variablen in die Itemliste geschrieben.
Codesys -> ROS2: Steuerung der Schildkröte mit Tastern
Dafür werden die Items in Variablenlsite beschrieben und bei Datenänderung dann von mit einer ros2 node gepublished.


