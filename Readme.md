## Team Squadron

Team members: Aarushi Bisht Shivam Rastogi Akhil Nagulavancha

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



Due to the current bug in the user registration please use the following credentials for logging in to the application. 

username : admin
,password : Password@1







