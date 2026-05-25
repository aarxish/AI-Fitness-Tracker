### AI FITNESS TRACKER 

## Description

AI Fitness Coach is a terminal-based Python application that uses artificial intelligence to provide personalized fitness and nutrition assistance. The application allows users to analyze their BMI, estimate calorie requirements, generate weekly diet plans, and check calories and macronutrients for meals using natural language input.

The project was built using Python and integrates the Groq API with the Llama 3.1 model to generate intelligent responses related to health, fitness, and nutrition. The Rich library was used to improve the terminal interface by adding colored tables, panels, loading animations, and a cleaner overall design.

## Project Structure
project.py
test_project.py
requirements.txt
README.md

## Health Analysis

This feature asks the user for:
age
height
weight
activity level

The information is then sent to the AI model, which returns:

BMI category
estimated maintenance calories
suggested calorie intake
fitness recommendations

## Weekly Diet Plan Generator

This feature uses the previously stored user information and asks the user whether their goal is to:
cut
bulk
maintain

The AI then generates a complete 7-day diet plan containing:

breakfast
lunch
dinner
snacks
calorie estimates
high-protein meal suggestions

## Calorie and Macro Checker

This feature allows users to enter meals or food items and receive estimated:

calories
protein
carbohydrates
fats
nutritional breakdowns for each item
## Why AI Was Used

One of the main reasons artificial intelligence was used in this project was to simplify user interaction and input handling.

Traditional calorie calculators usually require users to follow strict formats or predefined syntax rules. By using AI, the application can understand natural language input without requiring complicated parsing logic in Python.

For example, the user can enter:

"3 eggs and milk"
"rice chicken coke"
"2 bananas and peanut butter sandwich"

and the AI is still able to understand the request and generate nutritional estimates correctly.

This makes the application significantly more flexible and user-friendly.

Another advantage of using AI is adaptability. Instead of manually programming hundreds of food rules, calorie databases, and formatting conditions, the AI dynamically interprets requests and generates organized responses naturally.

## Libraries Used
### Groq

Used for AI inference and response generation.

### Rich

Used to create a cleaner and more interactive terminal interface.

### python-dotenv

Used to securely load environment variables from a .env file.

### pytest

Used for testing the project.

## Installation

Install all required libraries using:

pip install -r requirements.txt
## Environment Variables

Create a .env file in the project root directory and add:

GROQ_API_KEY=your_api_key_here

This keeps the API key secure and prevents it from being hardcoded into the source code.

## Running The Project

Run the application using:

python project.py
## Testing

Run tests using:

pytest test_project.py
## Design Choices

The application was designed to combine artificial intelligence with a clean terminal-based user experience while keeping the program simple, interactive, and easy to use.

The Rich library was chosen because it significantly improves the appearance of terminal applications through:

colored text
tables
panels
loading animations

The Groq API was selected because it provides fast and free AI inference that integrates easily with Python.

Environment variables were used to securely store the API key instead of exposing it publicly inside the source code.
