import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()

client = genai.Client()

# The program tries these models in order if one is busy
MODELS = ["gemini-3.5-flash", "gemini-flash-latest"]


def ask_ai(prompt):
    for attempt in range(3):
        for model in MODELS:
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                return response.text
            except errors.APIError as e:
                print(f"{model} failed (error {e.code}). Trying again...")
        time.sleep(5 * (attempt + 1))
    return "Sorry, the AI is too busy right now. Please try again in a few minutes."


def make_plan(topics, days, hours_per_day):
    prompt = f"""You are a friendly study coach helping a student who has fallen behind.

Topics they missed:
{topics}

Days available: {days}
Study hours per day: {hours_per_day}

Create a day-by-day catch-up plan. Rules:
- Put the most important and most foundational topics first.
- Give each day a clear goal and 2-3 specific tasks.
- Keep each day within the hours available.
- End each day with a 5-minute review.
- Use simple language.
"""
    return ask_ai(prompt)


if __name__ == "__main__":
    print("Type one missed topic per line. Press Enter on an empty line when finished.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    topics = "\n".join(lines)
    days = input("How many days do you have? ")
    hours = input("How many hours can you study per day? ")

    print("\nMaking your plan...\n")
    print(make_plan(topics, days, hours))