function getWeather() {
    const city = document.getElementById('cityInput').value;
    fetch(`http://127.0.0.1:5000/weather?city=${encodeURIComponent(city)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('weatherResult').innerText = data.error;
            } else {
                document.getElementById('weatherResult').innerHTML = `
                    <h2>Weather in ${data.city}</h2>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Description: ${data.description}</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Wind Speed: ${data.wind_speed} km/h</p>
                `;
            }
        })
        .catch(() => {
            document.getElementById('weatherResult').innerText = "Error fetching weather data.";
        });
}