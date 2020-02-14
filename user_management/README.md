# User-management

###Install instructions
Create a python virtual environment using:
1. `Python3 -m venv venv`
2. Activate the virtual environment `source venv/bin/activate`
3. Execute `python3 manage.py runserver`
4. [Need to be updated]

### Running via docker container
1. Clone repo
2. Go to directory user_management
3. There are two files `docker-compose.yml` and `Dockerfile`
4. Build docker image `docker-compose up -d --build`
5. Run docker file `docker-compose up`
6. Test the application by going to http://localhost:8000


### Troubleshooting
1. Verify if the application is running using `docker ps`


### API reference
- Register user API
`localhost:8000/api/register`
Data block:
```
{ 
    "username": <>,
    "first_name": <>,
    "last_name": <>,
    "email": <>,
    "password" <>
}
```

- Login API
```
curl --location --request POST 'localhost:8000/api-token-auth/' \
--header 'Content-Type: multipart/form-data; boundary=--------------------------721590326618091688121388' \
--form 'username=test_user_2' \
--form 'password=Password@1'
```

- Verify API

```
curl --location --request POST 'localhost:8000/api-token-verify/' \
--header 'Content-Type: multipart/form-data; boundary=--------------------------830518709566240864230619' \
--form 'token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
```

- For accessing user-permissions based API in Django use:
```
curl --location --request GET 'localhost:8000/api/users/12' \
--header 'Authorization: Jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
```

