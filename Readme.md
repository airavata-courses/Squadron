## Team Squadron [![Build Status](https://travis-ci.org/airavata-courses/Squadron.svg?branch=develop)](https://travis-ci.org/airavata-courses/Squadron)

Team members: Aarushi Bisht Shivam Rastogi Akhil Nagulavancha


### Building new infrastructure

Pre-requisites

- Install Terraform
- Install ansible-playbooks
- ssh key pair
- jetstream openrc,sh file from your jetstream account


Steps-1 < Provision Infrastructure >

1. Clone the repo
2. Checkout develop branch
3. Go to 'infrastructure/terraform-jetstream' folder 
4. Source the jetsream openrc file, so that terraform can use your credentials from environment
5. Execute the following commands to see the plan of the infrastructure that will be provisioned
	`terraform apply -var 'keypair-path=<your-ssh-key-path>' -var-file=example.tfvars`
6. Create Infrastructure
	`terraform apply -var 'keypair-path=../tg865717-api-key.pub' -var-file=example.tfvars`
7. Note down the IP address of the servers that are created and you can login into them using your private ssh key.

Note: if you want you can change the vm-name in example.tvfars file, by modifying variable 'vm-name = "Squadron"'


Step-2 < Deploy a kubernetes cluster > 
1. Open folder 'infrastructure/ansible-cluster' folder and edit the hosts file
2. In the hosts file update the IP addresses of the master server and 3 slave servers that were created earlier.
3. Execute the ansible scripts in this order: 
  ```
  ansible-playbook -i hosts kube-dependencies.yml 
  ansible-playbook -i hosts master.yml 
  ansible-playbook -i hosts worker.yml 
  ansible-playbook -i hosts create-storage.yml 
  ```

4. For any issues/doubts you can refer digital-ocean website

Step-3 < Set up master Node >
1. Install helm
2. clone the repo in the master node. 
3. Go to folder helm-chart and execute
	`helm install squadron squadron/`
4. Verify the application by executing command `kubectl get pods` and all the pods of our application will be created. You can refer the application from <floating_ip_server>:31001.



### Assignment 2

Our jenkins server is hosted here: http://149.165.171.122:32323/job/Squadron/job/develop/. Username: admin, Password: admin

A commit on the develop branch will automatically trigger the jenkins build which does the following steps:

- Builds the docker images for all the services
- Runs the test cases
- Pushes the latest images to docker hub 
- Deploys the latest changes to kubernetes cluster using helm charts

Travis CI build result can accessed by clicking on the build badge. 

Our service is hosted here. http://149.165.171.122:31001/login

### Load balance Testing using Jmeter 

Tested the load on the application using 1000 users in 300 seconds for three loops 

Application is giving a current average error rate of 0.02 for the above configuration

<img width="1440" alt="1000 users - 300 ramp up time " src="https://user-images.githubusercontent.com/16973298/77219438-2a333500-6b0c-11ea-93b7-43f2a51178eb.png">

<img width="1164" alt="doc 1000 300 " src="https://user-images.githubusercontent.com/16973298/77219447-3cad6e80-6b0c-11ea-8525-35b24e3b561c.png">

Tested the load on the application using 2000 users in 300 seconds in one loops and 3 replicas of the services

Application is giving a current average error rate of 0.16 for the above configuration

<img width="1440" alt="3 PODS 2000 users 1 loop" src="https://user-images.githubusercontent.com/16973298/77220544-abdc9000-6b17-11ea-8ec1-c885ab3831ad.png">

<img width="1439" alt="2000 , 3 Pod ,  graph" src="https://user-images.githubusercontent.com/16973298/77220557-cadb2200-6b17-11ea-8315-05b1fdd0a47c.png">

Tested the load on the application using 5000 users with 300 seconds ramp up time for once  and 3 replicas of the services

Application is breaking down after 1500 to 2000 threads and giving an average error rate of 50%

<img width="1424" alt="Graph 5000 , 3 " src="https://user-images.githubusercontent.com/16973298/77238305-58b11e80-6ba5-11ea-8795-11638cd594f4.png">

<img width="1433" alt="5000 , 3 " src="https://user-images.githubusercontent.com/16973298/77238306-5bac0f00-6ba5-11ea-9225-e7e908b9cbaa.png">

### Assignment 1

Link to architectural diagram https://user-images.githubusercontent.com/5948157/74495966-45a09400-4eff-11ea-8556-52300ba422cb.png

To run and check the project please install the latest version of [docker](https://www.docker.com/get-started)

1) go to terminal in Mac/Linux or command promt in Windows and execute the following command .

```
git clone https://github.com/airavata-courses/Squadron.git
```
Checkout develop branch

```
git checkout develop
```

Change the directory to the cloned repository 

### Data Retrieval Service
This service is responsible for fetching data from a public API. Gateway API will request average rainfall data for a pincode for user specified months and publishes the result to a kafka topic for the model service.

To build the Data Retrival run the following command in the DataRetrival directory 

```
cd DataRetrieval
docker build -t data_retrieval .
```
### Model Execution Service
This consumes the data from a kafka topic, calculates the amount of water that can saved for the specified months on the user specified pincode and house area. It computes the result and pushes the result to a topic on which post processing service is listening

To build the Model Service run the following command in the ModelService directory

```
cd ModelService
docker build -t model .
```

### Post Processing Service
This service consumes the result of model execution service and calculates the total cost saved for the amount of water saved.
Final result is pushed to another kafka queue which is consumed by the session service.

To build the Post Processing service run the following command in the PostProcessing directory

```
cd PostProcessing
docker build -t post_processing .
```

### Session Management Service

This microservice is responsible for saving all user requests. The API gateway requests the session service to get the final status of the user request. User request can be either PENDING, COMPLETED, FAILED.

To build the Session Management service run the following command in the session.management directory

```
cd session.management
docker build -t session .
```
### User Management Service
To build the User Management service run the following command in the user_management directory

```
cd user_management
docker build -t user .
```
### Api Gateway
To start the API gateway run the following command in the api_gateway directory

```
cd api_gateway
```
Create a python virtual environment and activate it
```
pip install -r requirements.txt
```
```
python api_gateway/manage.py runserver 7000
```

To run all the above mentioned services and kafka run the following command in the root directory of the Squadron folder. 
```
docker-compose up -d
```
Check the status of the services. All the services should be up
```
docker-compose ps
```

### User Interface

To Run the User Interface run the the following command in the UI directory 

```
cd UI

npm install 

npm start

```

open http://localhost:8080/ in your browser 

Click on the register button to register to create a new user 

click on Finish registration button to complete registration 

click on login with registered credentials to login with new credentials 

Once you login , Please enter the inputs as per instructions shown on the screen and click on submit button

click on view sessions buttoon to view all the sessions user as created. 





