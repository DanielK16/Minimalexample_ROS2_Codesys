# Dockerfile für ROS2 Jazzy und OPC UA Connection Minimalbeispiel

# Basis Image für ros2 jazzy mit desktop anwendungen (rviz2)
FROM osrf/ros:jazzy-desktop

# Arbeitsverzeichnis festlegen
WORKDIR /Projektarbeit_Koerper

# Tools und Dependencies installieren
RUN apt-get update && apt-get upgrade -y
RUN apt install python3-pip -y

# break system pacakges bei jazzy benötigt
RUN pip3 install asyncua --break-system-packages --ignore-installed cryptography

# source ros2 direkt in bashrc schreiben damit automatisch gesourced
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

# Standard-Befehl beim Start des Containers welches programm er öffnen soll!
CMD ["bash"]

