# URL Shortener API

A simple URL shortener API built with Django and Django REST Framework. This project allows users to convert long URLs into shortened codes, and redirects users to the original URL when they visit the shortened link. It also tracks the number of clicks for each shortened link.

## Features

- Shorten long URLs into randomly generated 6-character shortcodes.
- Redirect from shortcode to the original URL.
- Track total clicks for each shortcode.
- REST API to create and list shortened URLs.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite3 (Default database)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd url_shortner
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv myenv
   # On Windows:
   .\myenv\Scripts\activate
   # On macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Create a Short URL

- **URL:** `/api/shortner/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "original_url": "https://www.example.com/very/long/path/to/something"
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "original_url": "https://www.example.com/very/long/path/to/something",
      "shortcode": "aBcD12",
      "clicks": 0,
      "created_at": "2026-07-07T10:00:00Z"
  }
  ```

### 2. List Short URLs

- **URL:** `/api/shortner/`
- **Method:** `GET`
- **Description:** Returns a paginated list of created shortened URLs.

### 3. Redirect to Original URL

- **URL:** `/<shortcode>/`
- **Method:** `GET`
- **Description:** Redirects the user to the `original_url` associated with the `<shortcode>`. For example, visiting `http://127.0.0.1:8000/aBcD12/` redirects to `https://www.example.com/very/long/path/to/something`.

## License

This project is open-source and available under the MIT License.
