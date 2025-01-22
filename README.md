# City Travel Itinerary Generator

A Streamlit-based web application that suggests travel itineraries, including places to visit for each day, based on user input for the city and the number of days. The application uses **LangChain** for orchestrating LLM interactions and leverages **Llama3-70B-8192** LLM (provided by Groq) to generate personalized itineraries.

## Features

- **City Input**: Users can enter a city for which they want travel recommendations.
- **Days Input**: Users can specify the number of days for their trip.
- **Dynamic Suggestions**: The application generates a list of places to visit each day of the trip based on the input.
- **Interactive UI**: Built with Streamlit, allowing a smooth and interactive user experience.

## Technologies Used

- **Streamlit**: For building the user interface.
- **LangChain**: To integrate the LLM for generating travel itineraries.
- **Llama3-70B-8192** (Groq): A powerful language model used for generating city travel itineraries.

## Installation

To run this application locally, follow the steps below:

### 1. Clone the repository

```bash
git clone https://github.com/sayan-dg/travel-itinerary-generator.git
cd travel-itinerary-generator
```

### 2. Install required dependencies

Create a virtual environment (optional but recommended) and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Set up Groq LLM API (Optional)

If you are using Groq's Llama3-70B-8192 LLM, ensure you have access to their API, and set up your API keys as instructed in the Groq documentation.

### 4. Run the Streamlit app

Start the application with:

```bash
streamlit run app.py
```

This will open a browser window with the application running locally.

## Usage

1. Open the Streamlit app.
2. Enter the city name in the provided text input field.
3. Specify the number of days you will spend in the city from the selection box.
4. Click "Generate" to receive a list of suggested places to visit for each day of your trip.

## Example

- **City**: Paris
- **Days**: 5

The app will suggest a list of places to visit each day in Paris, customized based on the duration of the trip.

## Contributing

We welcome contributions! Feel free to fork the repository and submit a pull request. If you find any issues or bugs, please open an issue on GitHub.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---
