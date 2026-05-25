from groq import Groq
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

console = Console()

user_data = {}


def health_analysis():
    """
    Gets user information and asks AI to calculate:
    - BMI
    - maintenance calories
    - suggested calorie intake
    """

    console.print(
        Panel.fit(
            "[bold cyan]HEALTH ANALYSIS[/bold cyan]",
            border_style="cyan"
        )
    )

    age = Prompt.ask("[green]Enter your age[/green]")
    height = Prompt.ask("[green]Enter your height in cm[/green]")
    weight = Prompt.ask("[green]Enter your weight in kg[/green]")

    activity_table = Table(
        title="Daily Activity Levels",
        box=box.ROUNDED,
        border_style="green"
    )

    activity_table.add_column("Level", style="cyan", justify="center")
    activity_table.add_column("Description", style="white")

    activity_table.add_row("1", "Very inactive")
    activity_table.add_row("2", "Lightly active")
    activity_table.add_row("3", "Moderately active")
    activity_table.add_row("4", "Very active")
    activity_table.add_row("5", "Athlete level")

    console.print(activity_table)

    activity = Prompt.ask("[green]Choose activity level (1-5)[/green]")

    prompt = f"""
    The user has:

    Age: {age}
    Height: {height} cm
    Weight: {weight} kg
    Activity Level: {activity}/5

    Calculate:
    1. BMI
    2. BMI Category
    3. Maintenance Calories
    4. Suggested calorie intake

    Rules:
    - If overweight -> calorie deficit
    - If underweight -> calorie surplus
    - If healthy -> maintenance calories

    IMPORTANT INSTRUCTIONS:
    - Show the response in a very clean and organized format
    - Keep the response short and easy to read
    - Do NOT show BMI formulas or calorie calculations
    - Do NOT explain the math
    - Mention only the final values
    - Give a short fitness recommendation at the end
    - Do NOT use markdown
    - Do NOT use ** symbols
    - Do NOT bold headings
    - Use plain clean text only
    """

    with console.status(
        "[bold green]Analyzing your fitness data...[/bold green]"
    ):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional fitness and nutrition coach."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    result = response.choices[0].message.content

    console.print(
        Panel(
            result,
            title="FITNESS REPORT",
            border_style="magenta"
        )
    )

    user_data["age"] = age
    user_data["height"] = height
    user_data["weight"] = weight
    user_data["activity"] = activity


def diet_plan():
    """
    Generates a weekly diet plan using saved user data.
    """

    if not user_data:
        console.print(
            Panel(
                "Please run Health Analysis first.",
                border_style="red"
            )
        )
        return

    console.print(
        Panel.fit(
            "[bold yellow]WEEKLY DIET PLAN[/bold yellow]",
            border_style="yellow"
        )
    )

    goal = Prompt.ask(
        "[green]What is your goal?[/green] (cut/bulk/maintain)"
    )

    prompt = f"""
    Create a detailed 7-day diet plan for:

    Age: {user_data['age']}
    Height: {user_data['height']} cm
    Weight: {user_data['weight']} kg
    Activity Level: {user_data['activity']}/5
    Goal: {goal}

    Requirements:
    - Include breakfast, lunch, dinner, snacks
    - Mention approximate calories
    - High protein meals
    - Budget friendly Indian foods

    IMPORTANT INSTRUCTIONS:
    - Keep the format very clean and easy to read
    - Do NOT use markdown
    - Do NOT use ** symbols
    - Do NOT bold headings
    - Use simple text formatting
    - Separate each day clearly
    """

    with console.status(
        "[bold green]Generating your diet plan...[/bold green]"
    ):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Indian fitness dietician."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    result = response.choices[0].message.content

    console.print(
        Panel(
            result,
            title="7 DAY DIET PLAN",
            border_style="yellow"
        )
    )


def calorie_checker():
    """
    Estimates calories and macros for foods entered by the user.
    """

    console.print(
        Panel.fit(
            "[bold blue]CALORIE CHECKER[/bold blue]",
            border_style="blue"
        )
    )

    food = Prompt.ask(
        "[green]Enter your foods[/green]\n(example: 3 eggs, 1 glass milk, 2 bananas)"
    )

    prompt = f"""
    Estimate calories and macros for:

    {food}

    Return:
    - Total Calories
    - Protein
    - Carbohydrates
    - Fats

    Also give breakdown for each item.

    IMPORTANT INSTRUCTIONS:
    - Keep the response neat and clean
    - Do NOT use markdown
    - Do NOT use ** symbols
    - Do NOT bold headings
    - Use plain simple text
    - Keep spacing readable
    """

    with console.status(
        "[bold green]Calculating calories and macros...[/bold green]"
    ):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a nutrition expert."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    result = response.choices[0].message.content

    console.print(
        Panel(
            result,
            title="CALORIE REPORT",
            border_style="blue"
        )
    )


def show_menu():
    """
    Displays the main menu using rich table.
    """

    table = Table(
        title="AI FITNESS COACH",
        box=box.DOUBLE_EDGE,
        border_style="cyan"
    )

    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Feature", style="white")

    table.add_row("1", "Health Analysis")
    table.add_row("2", "Generate Diet Plan")
    table.add_row("3", "Calorie Checker")
    table.add_row("4", "Exit")

    console.print(table)


def main():

    console.print(
        Panel.fit(
            "[bold green]WELCOME TO AI FITNESS COACH[/bold green]",
            border_style="green"
        )
    )

    while True:

        show_menu()

        choice = Prompt.ask(
            "[bold cyan]Choose an option[/bold cyan]"
        )

        if choice == "1":
            health_analysis()

        elif choice == "2":
            diet_plan()

        elif choice == "3":
            calorie_checker()

        elif choice == "4":

            console.print(
                Panel.fit(
                    "[bold red]Goodbye! Stay Healthy 💪[/bold red]",
                    border_style="red"
                )
            )

            break

        else:
            console.print(
                Panel(
                    "Invalid choice. Please try again.",
                    border_style="red"
                )
            )


if __name__ == "__main__":
    main()
