import requests
from parser import parse_conversation

BASE_URL = "http://127.0.0.1:8000/chat"

for i in range(1, 11):

    file_name = f"C{i}.md"

    print("=" * 80)
    print(file_name)
    print("=" * 80)

    turns = parse_conversation(file_name)

    messages = []

    for turn in turns:

        messages.append({
            "role": "user",
            "content": turn["user"]
        })

        response = requests.post(
            BASE_URL,
            json={
                "messages": messages
            }
        )

        result = response.json()

        print("\nUSER:")
        print(turn["user"])

        print("\nASSISTANT:")
        print(result["reply"])

        print("\nRecommendations:")

        if result["recommendations"]:

            for rec in result["recommendations"]:
                print("-", rec["name"])

        else:
            print("None")

        print("End:", result["end_of_conversation"])

        messages.append({
            "role": "assistant",
            "content": result["reply"]
        })