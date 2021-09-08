Install the following libs:
sudo apt install python3-pip
sudo apt-get install -y python3-rtree
sudo pip install --upgrade protobuf

Run server:
https://github.com/roborescue/rcrs-server
Branch: protobuf-comm
cd rcrs-server/boot
./start.sh -m ../maps/gml/test/map -c ../maps/gml/test/config

Run python core:
https://github.com/roborescue/rcrs-core-python/tree/develop
Branch: develop
cd rcrs-core-python
./start.sh
