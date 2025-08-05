import json
import boto3
import os
import random
from twilio.rest import Client

s3 = boto3.client('s3')

def send_whatsapp_message(message, number):
  try:
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    if not account_sid or not auth_token:
      print("Twilio credentials not set in environment variables.")
      return
    client = Client(account_sid, auth_token)

    from_whatsapp = 'whatsapp:+14155238886'  # Your Twilio Sandbox number
    to_whatsapp = f'whatsapp:{number}'

    client.messages.create(
      body=message,
      from_=from_whatsapp,
      to=to_whatsapp
    )
    print(f"WhatsApp message sent to {number}")
  except Exception as e:
    print(f"Error sending WhatsApp message to {number}: {e}")

def main():
  try:
    bucket_name = 'spanish-to-english-words-ivandagomez'
    object_key = 'spanish_to_german_words.txt'
    # Retrieve the file from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    file_content = response['Body'].read().decode('utf-8')
    words = [line.strip() for line in file_content.split("\n") if line.strip()]
    num_words = 5
    sample_words = random.sample(words, k=min(num_words, len(words)))
    prompt = "🇩🇪 Here are your German words for today:\n"
    for i, word in enumerate(sample_words):
      if word.count("|") != 2:
        print(f"Skipping malformed line: {word}")
        continue
      spanish, german, pronunciation = [w.strip() for w in word.split("|")]
      prompt += f"{i + 1}. {spanish} - {german} ({pronunciation})\n"
    numbers = ["+573024690359"]  # You can add more numbers here
    for number in numbers:
      send_whatsapp_message(prompt, number)
  except Exception as e:
    print(f'Error: {e}')

if __name__ == "__main__":
  main()
