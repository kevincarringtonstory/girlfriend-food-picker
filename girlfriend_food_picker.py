import anthropic
import csv
from datetime import datetime
import os

# Set up the Anthropic client
ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"  # Replace with your actual API key
MODEL_NAME = "claude-3-5-sonnet-20240620"
CLIENT = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def get_input(prompt):
    return input(prompt)

def save_results_to_csv(results, filename):
    """Save the girlfriend food picker results to a CSV file."""
    fieldnames = ["Timestamp", "Girlfriend's Name", "Mood", "Hunger Level", "Dietary Restrictions", 
                  "Time of Day", "Occasion", "Food Suggestions", "Response to Girlfriend"]
    
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

# Gather information about girlfriend
girlfriend_name = get_input("What's your girlfriend's name? ")
mood = get_input("How would you describe her current mood? ")
hunger_level = get_input("On a scale of 1-10, how hungry is she? ")
dietary_restrictions = get_input("Any dietary restrictions or preferences? ")
time_of_day = get_input("What time of day is it? (e.g., morning, afternoon, evening) ")
occasion = get_input("Is there any special occasion? (If none, just press Enter) ")

# Create a prompt template for food suggestions
prompt_template = f"""
Based on the following information about {girlfriend_name}, suggest 3 food options that she might enjoy:

- Current mood: {mood}
- Hunger level (1-10): {hunger_level}
- Dietary restrictions/preferences: {dietary_restrictions}
- Time of day: {time_of_day}
- Special occasion (if any): {occasion}

Please consider her mood, hunger level, and any dietary restrictions when making suggestions. For each suggestion, provide a brief explanation of why it might be a good choice given the circumstances.

Format your response as follows:
1. [Food suggestion 1]: [Brief explanation]
2. [Food suggestion 2]: [Brief explanation]
3. [Food suggestion 3]: [Brief explanation]
"""

# Send the prompt to Claude and get the response
response = CLIENT.messages.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": prompt_template}],
    max_tokens=4000
)

# Print Claude's food suggestions
print("\nClaude's food suggestions:")
print(response.content[0].text)

# Generate a response to say to the girlfriend
girlfriend_response_prompt = f"""
Based on the following information about {girlfriend_name} and the food suggestions provided, generate a 2-3 sentence response that the user could say to their girlfriend to suggest getting food together:

- Current mood: {mood}
- Hunger level (1-10): {hunger_level}
- Time of day: {time_of_day}
- Special occasion (if any): {occasion}

Food suggestions:
{response.content[0].text}

The response should be casual and loving, considerate of her mood and hunger level, and reference one or more of the food suggestions.
"""

girlfriend_response = CLIENT.messages.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": girlfriend_response_prompt}],
    max_tokens=300
)

# Print the generated response
print("\nSuggested response to your girlfriend:")
print(girlfriend_response.content[0].text)

# Prepare the results and save them
results = [{
    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Girlfriend's Name": girlfriend_name,
    "Mood": mood,
    "Hunger Level": hunger_level,
    "Dietary Restrictions": dietary_restrictions,
    "Time of Day": time_of_day,
    "Occasion": occasion,
    "Food Suggestions": response.content[0].text,
    "Response to Girlfriend": girlfriend_response.content[0].text
}]

save_results_to_csv(results, "girlfriend_food_picker_results.csv")
print("\nResults have been saved to girlfriend_food_picker_results.csv")

# Check if the file was created successfully
if os.path.exists("girlfriend_food_picker_results.csv"):
    print(f"File successfully created. Size: {os.path.getsize('girlfriend_food_picker_results.csv')} bytes")
else:
    print("File was not created. Check your write permissions in this directory.")

# Print the absolute path of the saved file
print(f"Absolute path of the saved file: {os.path.abspath('girlfriend_food_picker_results.csv')}")