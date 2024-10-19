# Products API

## Overview

The **Products API** provides a RESTful interface for managing products with full CRUD (Create, Read, Update, Delete) functionality. This API allows users to retrieve a list of products, create new products, update existing products, and delete products as needed.

## Base URL

The base URL for the API is: http://localhost:8000

The endpoints are listed in openapi.yaml file

Create the `.env` file to have your DB credentials

```
DB_USER=XXXX
DB_PASS=XX
DB_HOST=XX
DB_PORT=XXX
DB_NAME=XXXX
JWT_SECRET_KEY=XXXXXX
```

The file to start the server is `wsgi.py`

Test cases can be run directly by executing `test_product.py` file

To get the JWT token, hit http://localhost:8000/auth/login by passing the "admin:password" 
in base64 encode string in the header. 

The JWT token received from the `auth/login` must be copied in headers of other endpoints as a Bearer token