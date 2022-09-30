# Floating Experiment - EFEHR20 Source Model Testing


## Setup
### Docker quick setup
#### Install (from https://docs.docker.com/engine/install/ubuntu/)

Install docker engine in local machine. Skip if it is already installed.
```            
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

```
#### Test
```
sudo docker run hello-world
```

#### Post-installation steps (for rootless run and file writing permissions)

```
sudo groupadd docker
sudo usermod -aG docker $USER
```

### Install experiment dependencies
Make a conda virtual environment and install dependencies with
```
conda env create -f environment.yml
```

## Run

```
fecsep run config.yml
```