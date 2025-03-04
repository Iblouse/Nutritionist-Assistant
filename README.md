<img src="https://github.com/Iblouse/Nutritionist-Assistant/blob/main/DietApp.png" width="600"/>

Diet Advisor App is a web application designed to provide detailed nutritional analysis and advice based on images of food items. Users can upload images of their meals, and the app, powered by generative AI, will analyze the food items, calculate total calories, and provide insights on the nutritional content and healthiness of the food.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [License](#license)

## Project Overview

Diet Advisor App leverages the power of generative AI to offer personalized nutritional advice. Users can upload an image of their meal, and the app will provide a detailed breakdown of the calorie content and nutritional value of each food item. It will also suggest ways to make the meal healthier if necessary.

## Features

- **Image Upload**: Users can upload images of their meals in various formats (JPEG, PNG, WebP).
- **Nutritional Analysis**: The app analyzes the uploaded image to identify food items and calculates their calorie content.
- **Health Advice**: Provides suggestions to improve the nutritional value of meals.
- **User-Friendly Interface**: Intuitive and easy-to-use interface built with Streamlit.

## Installation

To run the Diet Advisor App locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Iblouse/Nutritionist-Assistant.git
    cd Nutritionist-Assistant
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory.
    - Add the following line with your Google API key:
      ```env
      GOOGLE_API_KEY=your_google_api_key_here
      ```

5. **Run the app**:
    ```bash
    streamlit run nutrition_app.py 
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Upload an image of your meal using the file uploader.
3. Click the "Tell me about this food" button to receive detailed nutritional analysis and health advice.

## Project Structure

```
youtube-content-summarizer/
│
├── .env                # Environment variables
├── requirements.txt    # Required Python packages
├── nutrition_app.py      # Main application code
└─- README.md           # Project documentation
```

## Technology Stack

- **Python**: The main programming language used for the app.
- **Streamlit**: Framework for building the web app interface.
- **Pillow**: Library for image processing.
- **google-generativeai**: Library for interacting with Google's generative AI models.
- **dotenv**: Library for loading environment variables from a `.env` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
