# Girlfriend Food Picker

Girlfriend Food Picker is a Python script that helps you suggest food options for your girlfriend based on her current mood, hunger level, and other factors. It uses Anthropic's Claude language model to generate personalized food suggestions and a response to communicate these suggestions to your girlfriend.

## Features

- Gathers information about your girlfriend's current state (mood, hunger level, etc.)
- Generates 3 food suggestions tailored to the provided information
- Creates a personalized response to suggest the food options to your girlfriend
- Saves the results to a CSV file for future reference

## Prerequisites

- Python 3.x
- Anthropic API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/kevincarringtonstory/girlfriend-food-picker.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Anthropic API key:

- Create a `.env` file in the project directory
- Add your API key to the `.env` file in the following format:

```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

1. Run the script:

```bash
python girlfriend_food_picker.py
```

2. Follow the prompts to enter information about your girlfriend's current state.

3. The script will generate food suggestions and a personalized response.

4. Results will be displayed in the console and saved to a CSV file named `girlfriend_food_picker_results.csv`.

## Example

Here's an example of how to use the Girlfriend Food Picker:

```
What's your girlfriend's name? Emma
How would you describe her current mood? Tired but excited
On a scale of 1-10, how hungry is she? 7
Any dietary restrictions or preferences? Vegetarian
What time of day is it? (e.g., morning, afternoon, evening) Evening
Is there any special occasion? (If none, just press Enter) Date night

Claude's food suggestions:
1. Vegetarian sushi platter: A variety of colorful and flavorful vegetarian sushi rolls would be perfect for a special date night. The light, fresh flavors can help energize Emma without being too heavy, and the interactive nature of sharing sushi can be fun and romantic.

2. Gourmet vegetarian pizza: A delicious, customized vegetarian pizza with premium toppings like artichokes, sun-dried tomatoes, and truffle oil could satisfy Emma's hunger while still feeling special for the occasion. The comfort food aspect might help with her tiredness, too.

3. Mediterranean mezze spread: A selection of small vegetarian dishes like hummus, falafel, dolmas, and grilled vegetables would offer variety and excitement for your date night. The protein-rich options can help boost Emma's energy, and the shareable nature of the meal can make for a intimate dining experience.

Suggested response to your girlfriend:
Hey Emma, I know you're feeling a bit tired but also excited for our date night. How about we treat ourselves to something special that'll satisfy your hunger and give you a little energy boost? I was thinking we could go for a vegetarian sushi platter or maybe a gourmet veggie pizza with some fancy toppings. What do you think? It'll be a perfect way to relax and enjoy our evening together.

Results have been saved to girlfriend_food_picker_results.csv
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
