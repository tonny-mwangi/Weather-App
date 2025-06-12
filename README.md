# Weather App

This is a simple weather application that fetches live weather data for major cities around the world. The application is structured into a backend and a frontend, allowing for a clear separation of concerns.

## Project Structure

```
weather-app
├── backend
│   ├── app.py
│   └── requirements.txt
├── frontend
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
```

## Backend

The backend is built using Flask, a lightweight WSGI web application framework. It serves as an API to fetch weather data from a third-party weather service.

### Setup Instructions

1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```

## Frontend

The frontend is built using HTML, CSS, and JavaScript. It provides a user interface for users to input city names and view the corresponding weather information.

### Usage Instructions

1. Open `frontend/index.html` in a web browser.
2. Enter the name of a city in the input field and submit the form to fetch the weather data.
3. The weather information will be displayed on the page.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is open-source and available under the MIT License.