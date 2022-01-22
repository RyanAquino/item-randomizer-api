# Item Randomizer API
Item Randomizer API is a program that generates 4 random objects that includes Alphabets, Integers, real numbers and Alphanumeric which is written in a 2mb text file.

### Endpoints
- `POST /v1/item` - Generate random objects and store in a file
- `GET /v1/item` - Retrieve generated item count details
- `GET /v1/item/download` - Download file generated
- `GET /api-docs` - Swagger API documentation 

### Requirements
- python 3
- docker
- docker-compose

### Technology
- python 3
- Flask
- Pydantic


### Setup
##### create virtual environment
```
python -m venv venv
```
##### Install required packages
```
pip install -r requirements.txt
```
##### Run server
```
python app.py
```

### Setup with Docker (Alternative)
```
docker-compose up -d
```

#### Access on browser
```
http://localhost:5000/api-docs
```

### Running tests
```
pytest .
```