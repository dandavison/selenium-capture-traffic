sudo apt-get install -y docker.io
(cd /vagrant/docker/browsermob && sudo docker build -t dandavison/browsermob . > /dev/null)
sudo docker run -d -p 9999:9999 dandavison/browsermob
