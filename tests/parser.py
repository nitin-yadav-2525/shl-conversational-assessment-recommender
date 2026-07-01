import os
import re


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def parse_conversation(filename):

    file_path = os.path.join(BASE_DIR, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    turns = []

    pattern = r"\*\*User\*\*(.*?)\*\*Agent\*\*(.*?)(?=(### Turn|\Z))"

    matches = re.findall(pattern, text, re.S)

    for match in matches:

        user_text = match[0].replace(">", "").strip()

        agent_text = match[1].strip()

        turns.append({
            "user": user_text,
            "agent": agent_text
        })

    return turns


if __name__ == "__main__":

    data = parse_conversation("C1.md")

    for i, turn in enumerate(data, start=1):

        print("=" * 70)
        print(f"TURN {i}")
        print("=" * 70)

        print("\nUSER:\n")
        print(turn["user"])

        print("\nEXPECTED AGENT:\n")
        print(turn["agent"])