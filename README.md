# Telegram Holiday Bot

A Telegram bot that sends daily holiday reminders with personalized flavor text.

## Features

- Sends daily holiday messages based on `holiday_list.json`
- Uses randomized flavor text from `flavor_text.json`
- Automated deployment via GitHub Actions
- Supports both direct Python execution and Docker containers

## Setup

### Prerequisites
- Python 3.11+
- Telegram Bot Token (from @BotFather)
- Telegram Chat/Channel ID where messages will be sent

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your bot token from BotFather
   - `TELEGRAM_CHAT_ID`: Target chat/channel ID
4. Run: `python bot_script.py`

## GitHub Actions Deployment

### Setup Secrets
In your GitHub repository, go to Settings > Secrets and Variables > Actions and add:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: The chat/channel ID where messages should be sent

### Deployment Options

#### 1. Simple Python Deployment (Recommended)
Uses `.github/workflows/deploy.yml`:
- Runs daily at 9:00 AM UTC
- Can be triggered manually
- Runs on every push to main branch
- Simple Python execution without containers

#### 2. Docker Deployment
Uses `.github/workflows/deploy-docker.yml`:
- Builds and runs the bot in a Docker container
- Good for more complex deployments
- Only runs on push to main (not on schedule)

### Getting Your Chat ID
To find your chat/channel ID:
1. Add your bot to the chat/channel
2. Send a message mentioning the bot
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Look for the `chat` object and copy the `id` value

### Scheduling
The bot runs automatically daily at 9:00 AM UTC. You can:
- Change the schedule in the workflow YAML files
- Trigger manually from the Actions tab
- Modify the cron expression for different timing

## File Structure
- `bot_script.py`: Main bot logic
- `holiday_list.json`: Holiday database
- `flavor_text.json`: Random message templates
- `requirements.txt`: Python dependencies
- `.github/workflows/`: GitHub Actions workflows
- `Dockerfile`: Container configuration

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request