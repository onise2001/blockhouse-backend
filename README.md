## Overview

This is a backend app developed with django/DRF for Blockhouse Full-Stack Developer technical task, I provided sqlite database with hardcoded data that can be used to test the application, you can also add new items by sending POST requests in correct format to the endpoints listed below.

## Installation

- Clone the repository:

```
git clone https://github.com/onise2001/blockhouse-backend.git
```

- Navigate to project directory:

```
cd blockhouse-backend
```

- Build and run Docker image and Container by running the following command:

```
docker-compose up --build --detach

```

## OR

- Create virtual environment with the following coomand (python3 if on linux):

```
python -m venv venv
```

- Activate the virtual environment:

```
Windows: venv\scripts\activate

Linux: source venv/bin/activate

```

- Install required modules by running the following command:

```
pip install -r requirements.txt
```

- Run server (python3 if on linux):

```
python manage.py runserver

```

## Endpoints

- /api/candlestick-data/

```
GET Request response example:
[
    {
        x = "2023-14-1",
        open = 6,
        high = 10,
        low = 11,
        close = 12
    },
    {
        x = "2023-14-2",
        open = 12,
        high = 15,
        low = 7,
        close = 11
    }
]

POST Request format example:
{
    x = "2023-14-2",
    open = 12,
    high = 15,
    low = 7,
    close = 11
}
```

- /api/line-chart-data/

```

GET Request response example:
{
  "labels": ["Jan", "Feb", "Mar", "Apr"],

  "data": [10, 20, 30, 40]
}

POST Request format example:
[
    {
        label:Jan,
        data:10
    },
    {
        label:Feb,
        data:20
    }
]

```

- /api/bar-chart-data/

```

GET Request response example:
{
    "labels": ["Product A", "Product B", "Product C"],
    "data": [100, 150, 200]
}

POST Request format example:
[
    {
        label:Product A,
        data:100
    },
    {
        label:Product B,
        data:150
    }
]

```

- /api/pie-chart-data/

```

GET Request response example:
{
    "labels": ["Red", "Blue", "Yellow"],
    "data": [300, 50, 100]
}

POST Request format example:
[
    {
        label:Red ,
        data:300
    },
    {
        label:Blue,
        data:50
    }
]

```
