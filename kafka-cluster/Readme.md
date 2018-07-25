Please remember to add kafka-1, kafka-2 and kafka-3 hosts to the client /etc/hosts file with the IP of the virtual nic
192.168.1.231 kafka-1 kafka-2 kafka-3

# install client tool
sudo apt-get install kafkacat

# list brokers
kafkacat -L -b kafka-1:19092

# producer
kafkacat -P -b kafka-1:19092 -t helloworld_topic

# consumer
kafkacat -C -b kafka-3:39092 -t helloworld_topic


