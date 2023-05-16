# Quote Bot

Quote Bot is a Discord bot that automatically sends a random quote along with a related image to a specified text channel every 12 hours. It uses the [discord.py](https://discordpy.readthedocs.io/) library for interacting with Discord and the [requests](https://docs.python-requests.org/) library for fetching quotes and images from the internet.

## Features

- Fetches a random quote from [Quotable API](https://www.quotable.io/)
- Fetches a related image from [Unsplash API](https://unsplash.com/developers)
- Sends the quote and image as an embed message in a specified text channel
- Supports mentioning a specific role when sending the quote and image

## Installation

1. Make sure you have Python 3.6 or higher installed. You can check your Python version by running `python --version` in your terminal.
2. Clone this repository and navigate to the project directory. `git clone https://github.com/yourusername/quote-bot.git`
4. Then `cd quote-bot`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Replace the placeholders with your actual Discord bot token, Unsplash API key, text channel ID, and role ID.
7. python bot.py

# Configuration
To customize the bot's behavior, you can modify the following variables in the quote_bot.py file:

*TOKEN:* Your Discord bot token (string)

*TEXT_CHANNEL_ID:* The text channel ID where the bot should send messages (integer)

*UNSPLASH_ACCESS_KEY:* Your Unsplash API key (string)

*ROLE_ID:* The role ID that the bot should mention when sending messages (integer)

# License
This project is licensed under the MIT License.
