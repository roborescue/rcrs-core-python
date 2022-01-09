Install the following libs:
sudo apt install python3-pip
sudo apt-get install -y python3-rtree
sudo pip install --upgrade protobuf

Run server:
https://github.com/roborescue/rcrs-server
Branch: protobuf-v6
cd rcrs-server/scripts
./start.sh -m ../maps/test/map -c ../maps/test/config

Run python core:
https://github.com/roborescue/rcrs-core-python/tree/develop
Branch: process
cd rcrs-core-python
./start.sh
