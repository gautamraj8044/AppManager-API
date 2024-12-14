
## Installation

### Prerequisites

- Python 3.7 or higher
- Virtual environment (optional, but recommended)

### Steps to Install

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/gautamraj8044/AppManager-API.git
   cd appmanager-api
   ```



---

### How to Run the App Management API

1. **Extract the files** into a directory.

2. **Navigate to the project directory** in your terminal or command prompt.

3. **Create and activate a virtual environment**:

   For Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   For Mac/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**:
   Make sure to install the required libraries by running:
   ```bash
   pip install flask flask_sqlalchemy
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

   The app will be available at `http://127.0.0.1:5000/`.

---
Here's a sample set of data you can use to test the API:

### Sample Data for API Testing:

#### 1. **Add a New App (POST /apps)**

You can use **Postman** or **cURL** to send the following data to test the `POST /apps` endpoint.

**Request**:
- URL: `http://127.0.0.1:5000/apps`
- Method: `POST`
- Body (form-data):



### cURL Command:
```bash
curl -X POST http://127.0.0.1:5000/add-app \
  -F "app_name=MyApp" \
  -F "version=1.0" \
  -F "description=This is a test app."
```

### Explanation:
- `-X POST`: Specifies the HTTP method, which is `POST`.
- `http://127.0.0.1:5000/apps`: The endpoint where you are sending the request.
- `-F "app_name=MyApp"`: The `app_name` field in the form data.
- `-F "version=1.0"`: The `version` field in the form data.
- `-F "description=This is a test app."`: The `description` field in the form data.



**Response**:
```json
{
  "message": "App added successfully",
  "id": 1
}
```

#### 2. **Get All Apps (GET /apps)**

You can get all the apps using this **GET** request:

**Request**:
- URL: `http://127.0.0.1:5000/apps`
- Method: `GET`

**Response**:
```json
[
  {
    "id": 1,
    "app_name": "MyApp",
    "version": "1.0",
    "description": "This is a test app."
  }
]
```

#### 3. **Get App by ID (GET /apps/{id})**

You can get a specific app by its ID (e.g., ID = 1):

**Request**:
- URL: `http://127.0.0.1:5000/get-app/1`
- Method: `GET`

**Response**:
```json
{
  "id": 1,
  "app_name": "MyApp",
  "version": "1.0",
  "description": "This is a test app."
}
```

#### 4. **Delete an App (DELETE /apps/{id})**

To delete the app with ID 1:

**Request**:
- URL: `http://127.0.0.1:5000/get-app/1`
- Method: `DELETE`

**Response**:
```json
{
  "message": "App deleted successfully"
}
```

---

This data should help you test the basic functionality of your API. You can modify the `app_name`, `version`, and `description` fields as needed to add more apps or test different cases.