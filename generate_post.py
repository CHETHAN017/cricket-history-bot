import datetime
import json
import random

def load_data():
    with open("cricket_history.json", "r") as f:
        return json.load(f)

def generate_caption(event):
    return f"🏏 On this day in {event['year']}, {event['event']} #Cricket #OnThisDay"

def main():
    data = load_data()
    today = datetime.datetime.now().strftime("%m-%d")
    events = data.get(today, [])

    if not events:
        print("No events found for today.")
        return

    event = random.choice(events)
    caption = generate_caption(event)

    with open("today_post.txt", "w") as f:
        f.write(caption)
    print("Post generated:", caption)

if __name__ == "__main__":
    main()

