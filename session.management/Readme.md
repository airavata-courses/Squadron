## SESSION MANAGEMENT SERVICE

APIs exposed to API server

#### To create a new experiment
```
POST http://localhost:9096/api/v1/session
```
Sample request
```
{
	"request_id": "883iee1",
	"username":"user1",
	"pincode": 47408,
	"months": [1],
	"status": "PENDING",
	"house_area":2
}
```
