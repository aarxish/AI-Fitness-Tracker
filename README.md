### AI FITNESS COACH

 (Create a .env file and add your GROQ_API_KEY before running the project.)
 
AI Fitness Coach is a terminal-based Python application that uses artificial intelligence to provide personalized fitness and nutrition assistance. The application allows users to analyze their BMI, estimate calorie requirements, generate weekly diet plans, and check calories and macronutrients for meals using natural language input.

The project was built using Python and integrates the Groq API with the Llama 3.1 model to generate intelligent responses related to health, fitness, and nutrition. The Rich library was used to improve the terminal interface by adding colored tables, panels, loading animations, and a cleaner overall design.

### Project Structure:

project.py
test_project.py
requirements.txt
README.md

The main application logic is located inside project.py.

The program contains three main features.

The first feature is the Health Analysis function. This function asks the user for:

age,
height,
weight,
and activity level.

The information is then sent to the AI model, which analyzes the data and returns:

BMI category,
estimated maintenance calories,
suggested calorie intake,
and fitness recommendations.

The second feature is the Weekly Diet Plan Generator. This function uses the previously stored user information and asks the user whether their goal is to:

cut,
bulk,
or maintain.

The AI then generates a complete 7-day diet plan containing:

breakfast,
lunch,
dinner,
snacks,
calorie estimates,
and high-protein meal suggestions.

The third feature is the Calorie and Macro Checker. This feature allows users to enter meals or food items and receive estimated:

calories,
protein,
carbohydrates,
fats,
and a nutritional breakdown for each food item.

One of the main reasons artificial intelligence was used in this project was to simplify user interaction and input handling. Traditional calorie calculators usually require users to follow strict formats or predefined syntax rules. By using AI, the application can understand natural language input without requiring complicated parsing logic in Python.

For example, the user can enter:

“3 eggs and milk”
“rice chicken coke”
“2 bananas and peanut butter sandwich”

and the AI is still able to understand the request and generate accurate nutritional estimates. This creates a much more flexible and user-friendly experience.

Another advantage of using AI is adaptability. Instead of manually programming hundreds of food rules, calorie databases, and formatting conditions, the AI can dynamically interpret requests and generate organized responses naturally.

The project also uses environment variables through python-dotenv to securely store the API key instead of hardcoding it directly into the source code. This improves security and follows standard development practices.

The test_project.py file contains pytest test cases used to verify user data handling and helper logic inside the application.\


The requirements.txt file contains all required libraries for running the project, including:

groq
rich
python-dotenv
pytest

To install the required libraries:

pip install -r requirements.txt

To run the application:

python project.py

The application was designed to combine artificial intelligence with a clean terminal-based user experience while keeping the program simple, interactive, and easy to use.
