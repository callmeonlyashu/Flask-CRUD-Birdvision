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
```

the file to run is `main.py`

test cases can be run directly by executing `test_product.py` file