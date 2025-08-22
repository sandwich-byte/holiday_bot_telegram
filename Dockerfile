FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY bot_script.py .
COPY holiday_list.json .
COPY flavor_text.json .

# Run the bot
CMD ["python", "bot_script.py"]
