# Minimalbeispiel für Datenaustausch zwischen ROS2 und Codesys via OPC UA

Software Stack
|Tool|Nutzung|
|---|---|
|asyncua|OPC UA Client erstellen|

![Datenaustausch ROS2 und Codesys](/doc/img/Datenaustausch_Codesys_ROS2.png)

Das Ziel ist es mithilfe von **turlesim** den Datenaustausch zwischen ROS2 und Codesys darzustellen.
turtlesim ist ein Einsteigertool um ROS2 Konzepte zu erlernen.
Das Gesamtsystem besteht aus:
* ROS2 Simulation turtlesim
* OPC UA Brücke(asyncua)
* Codesys VSPS und Visualisierung

In diesem Beispiel wird der Datenaustausch wird der Datenaustausch in beide Richtungen getestet:
Einmal von ROS2 -> Codesys: In diesem Fall die Position der Schildkröte übertragen und in Codesys anzeigen.
Codesys -> ROS2: Steuerung der Schildkröte mit Tastern
Für OPC UA wird die asyncua Bib verwendet

