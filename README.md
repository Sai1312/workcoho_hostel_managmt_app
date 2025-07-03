# **Hostel Management App - Django REST FrameWork**

A comprehensive Hostel Management Application API developed using Django and Django REST Framework,featuring
secure JWT authentication for user access control. The API supports full CRUD (Create, Read, Update,Delete)
operations, enabling efficient management of hostel entities such as rooms, students, fees,and staff.

## API Endpoints

> Base URL: `http://127.0.0.1:8000/`

###  Authentication

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| `POST` | `/api/token/` | Obtain JWT token (login) |
| `POST` | `/api/token/refresh/` | Refresh JWT access token |

###  Hostel Management App 

| Method | Endpoint | Description |
| -------- | ---------- | ------------- |
| `GET` | `/api/hostelfees/` | List all entities *(requires token)* |
| `GET` | `/api/hostels/` | List all entities *(requires token)* |
| `GET` | `/api/students/` | List all entities *(requires token)* |
| `GET` | `/api/rooms/` | List all entities *(requires token)* |
| `GET` | `/api/hostelfees/<int:pk>/` | List particular entities *(requires token)* |
| `GET` | `/api/hostels/<int:pk>/` | List particular entities *(requires token)* |
| `GET` | `/api/students/<int:pk>/` | List particular entities *(requires token)* |
| `GET` | `/api/rooms/<int:pk>/` | List particular entities *(requires token)* |
| `POST` | `/api/hostelfees/` | Create new entities *(requires token)* |
| `POST` | `/api/hostels/` | Create new entities *(requires token)* |
| `POST` | `/api/students/` | Create new entities *(requires token)* |
| `POST` | `/api/rooms/` | Create new entities *(requires token)* |
| `PUT` | `/api/hostelfees/<int:pk>/` | Updates an existing resource completely *(requires token)* |
| `PUT` | `/api/hostels/<int:pk>/` | Updates an existing resource completely *(requires token)* |
| `PUT` | `/api/students/<int:pk>/` | Updates an existing resource completely *(requires token)* |
| `PUT` | `/api/rooms/<int:pk>/` | Updates an existing resource completely *(requires token)* |
| `PATCH` | `/api/hostelfees/<int:pk>/` | Updates an existing resource partially *(requires token)* |
| `PATCH` | `/api/hostels/<int:pk>/` | Updates an existing resource partially *(requires token)* |
| `PATCH` | `/api/students/<int:pk>/` | Updates an existing resource partially *(requires token)* |
| `PATCH` | `/api/rooms/<int:pk>/` | Updates an existing resource partially *(requires token)* |
| `DELETE` | `/api/hostelfees/<int:pk>/` | Removes a resource from the server *(requires token)* |
| `DELETE` | `/api/hostels/<int:pk>/` | Removes a resource from the server *(requires token)* |
| `DELETE` | `/api/students/<int:pk>/` | Removes a resource from the server *(requires token)* |
| `DELETE` | `/api/rooms/<int:pk>/` | Removes a resource from the server *(requires token)* |

All API endpoints are secured and require a valid JWT (JSON Web Token) to be included in the request header for authentication and authorization. Without a valid token, access to any operation—whether retrieving, creating, updating, or deleting resources—is restricted.

Authorization -> Select 'Bearer Token' -> Paste <your_token>

---

## HTTP Status Code

### 1xx – Informational
| Code | Meaning | Description                        |
| ---- | -------- |  ----------- |
| 100  | Continue | Request received, continue process |
| 101  | Switching Protocols | Server is switching protocols |

### 2xx - Success
| Code | Meaning | Description |
| ---- | ---------- | ------------- |
| 200  | OK         | Request successful |
| 201  | Created    | Resource created (e.g., after POST) |
| 202  | Accepted   | Request accepted but not yet processed |
| 204  | No Content | Success, but no content to return |

### 3xx - Redirection
| Code | Meaning | Description |
| ---- | -------- | ----------- |
| 301  | Moved Permanently | Resource has been moved to a new URL  |
| 302  | Found | Temporary redirect |
| 304  | Not Modified | Client has the latest version (cache) |

### 4xx - Client Errors 
| Code | Meaning | Description |
| ---- | --------- | ---------- |
| 400  | Bad Request | Invalid request syntax |
| 401  | Unauthorized | Requires authentication |
| 403  | Forbidden | You don’t have permission |
| 404  | Not Found | Resource not found |
| 405  | Method Not Allowed | HTTP method not supported (e.g., PUT not allowed) |
| 409  | Conflict | Conflict in current state (e.g., duplicate entry) |
| 422  | Unprocessable Entity | Valid data but cannot process it (e.g., validation error) |

### 5xx - Server Errors
| Code | Meaning | Description |
| ---- | -------- | ---------- |
| 500  | Internal Server Error | Server-side error |
| 502  | Bad Gateway | Server got invalid response from upstream |
| 503  | Service Unavailable | Server down or overloaded |
| 504  | Gateway Timeout | Upstream server failed to respond in time |

## ZUSTAND

Zustand (German for “state”) is a fast, minimal state management solution built by the creators of react-spring.

### Installation

Install Zustand using npm:

    npm install zustand


## AXIOS

Axios is a promise-based HTTP client used to:
- Make API requests
    - GET, POST, PUT, PATCH, DELETE

- Handle JSON data

- Work easily with async/await

### Installation 

    npm install axios


## CORS

CORS stands for Cross-Origin Resource Sharing. It's a security feature enforced by web browsers.

### Installation 

    - Run the below line in terminal:
        pip install django-cors-headers
    
    - Add to INSTALLED_APPS in settings.py as below:
        INSTALLED_APPS = [
            ...
            'corsheaders',
        ]
    
    -Add the middleware at the top of the MIDDLEWARE list as below:
        MIDDLEWARE = [
            'corsheaders.middleware.CorsMiddleware',  
            'django.middleware.common.CommonMiddleware',
            ...
        ]
    
    - Then add below line under the middleware:
        CORS_ALLOW_ALL_ORIGINS = True


