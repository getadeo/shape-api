## pipenv setup
```
$ python create_db.py
$ pipenv shell
$ pipenv install
$ flask run
```

## virtualenv/mkvirtualenv setup
``` 
$ virtualenv venv
$ source venv/bin/activate
$ source .env
$ flask run

``` 

## Sample Requests

### Square POST Request

```curl
$ curl -X POST \
  http://localhost:5000/square/ \
  -H 'Content-Type: application/json' \
  -d '{
	"side": 9
}'
```

### Response

```json
{
    "dataURL": {
        "areaURL": "http://0.0.0.0:5000/square/1/area",
        "perimeterURL": "http://0.0.0.0:5000/square/1/perimeter"
    },
    "message": "Succesfully saved",
    "squareData": {
        "id": 1,
        "side": 9
    }
}
```

### Square GET data by ID

```
$ curl -X GET http://0.0.0.0:5000/square/1
```

### Response

```json
{
    "squareData": {
        "id": 1,
        "side": 9
    }
}
```

### Square GET Area by ID

```
$ curl -X GET http://0.0.0.0:5000/square/1/area
```

### Response

```json
{
    "message": "The area value is 81.0",
    "squareData": {
        "area": 81,
        "id": 1,
        "side": 9
    }
}
```

### Square GET Perimeter by ID

```
$ curl -X GET http://0.0.0.0:5000/square/1/perimeter
```

### Response

```json
{
    "message": "The perimeter value is 36.0",
    "squareData": {
        "id": 1,
        "perimeter": 36,
        "side": 9
    }
}
```

### Square PUT by ID

```
$ curl -X PUT \
  http://0.0.0.0:5000/square/1 \
  -H 'Content-Type: application/json' \
  -d '{
	"side": 33.99
}'
```

### Response

```json
{
    "dataURL": {
        "areaURL": "http://0.0.0.0:5000/square/1/area",
        "perimeterURL": "http://0.0.0.0:5000/square/1/perimeter"
    },
    "message": "Succesfully updated",
    "squareData": {
        "id": 1,
        "side": 33.99
    }
}
```

### Square DELETE by ID

```
$ curl -X DELETE http://0.0.0.0:5000/square/1
```

### Response

```json
{
    "message": "Successfully deleted"
}
```

<!-- # See it in action: http:// -->