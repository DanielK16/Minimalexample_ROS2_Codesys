# Minimalbeispiel für Datenaustausch zwischen ROS2 und Codesys via OPC UA

Software Stack
| | |
|---|---|
| | |


Das Ziel ist es mithilfe von turlesim den Datenaustausch zwischen ROS2 und Codesys darzustellen.
turtlesim ist ein einsteigerrtool um ros2 konzepte zu erlernen.
Das Gesamtsystem besteht aus:
* ROS2 Simulation turtlesim

* OPC UA Brücke(asyncua)

* Codesys VSPS und Visualisierung

In diesem Beispiel wird der Datenaustausch wird der Datenaustausch in beide Richtungen getestet:
Wir möchten einmal von ROS2 -> Codesys verbindung herstellen. in diesem fall die Position der Schildkröte übertragen und in Codesys anzeigen
und einmal Codesys -> ROS2: Steuerung der Schildkröte mit Tastern
Für OPC UA wird die asyncua Bib verwendet

