## Team Squadron

Team members: Aarushi Bisht Shivam Rastogi Akhil Nagulavancha

To run and check the project please install the latest version of [docker](https://www.docker.com/get-started)

1) go to terminal in Mac/Linux or command promt in Windows and execute the following command .

```
git clone https://github.com/airavata-courses/Squadron/tree/aarushi-develop
```

Change the directory to the cloned repository 

To build the Data Retrival run the following command in the DataRetrival directory 

```
docker build -t data_retrieval .
```

To build the Model Service run the following command in the ModelService directory

```
docker build -t model .

```

To build the Post Processing service run the following command in the PostProcessing directory

```
docker build -t post_processing .
```


To build the Session Management folder run the following command in the session.management directory

```
docker build -t session .

```

To run all the above mentioned services run the following command in the root directory of the Squadron folder. 

```
docker-compose up -d

```


