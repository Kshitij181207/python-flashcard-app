import json
from pathlib import Path

DATA_FILE = Path("flashcards.json")


def load_cards():
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_cards(cards):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(cards, file, indent=2)


def add_cards(cards):
    while True:
        question = input("\nWrite a question (or press Enter to stop adding): ").strip()

        if not question:
            break

        answer = input("Write its answer: ").strip()

        if not answer:
            print("Answer can't be blank.")
            continue

        cards.append({"question": question, "answer": answer})
        save_cards(cards)
        print("Card saved!")


def study_cards(cards):
    if not cards:
        print("\nYou don't have any flashcards yet. Add some first.")
        return

    score = 0

    for card in cards:
        input(f"\nQuestion: {card['question']}\nPress Enter to reveal the answer...")
        print(f"Answer: {card['answer']}")

        result = input("Did you get it right? (y/n): ").strip().lower()
        if result == "y":
            score += 1

    print(f"\nYou got {score} out of {len(cards)} right.")


def delete_card(cards):
    if not cards:
        print("\nThere are no cards to delete.")
        return

    print("\nCards:")
    for number, card in enumerate(cards, start=1):
        print(f"{number}. {card['question']}")

    choice = input("Enter the number to delete (or press Enter to cancel): ").strip()

    if not choice:
        print("Delete cancelled.")
        return

    if not choice.isdigit():
        print("Please enter a card number.")
        return

    card_number = int(choice)

    if card_number < 1 or card_number > len(cards):
        print("That number doesn't match a card.")
        return

    removed_card = cards.pop(card_number - 1)
    save_cards(cards)
    print(f"Deleted: {removed_card['question']}")


def main():
    cards = load_cards()

    while True:
        print("\n=== Flashcard App ===")
        print("1. Add cards")
        print("2. Study cards")
        print("3. Delete a card")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_cards(cards)
        elif choice == "2":
            study_cards(cards)
        elif choice == "3":
            delete_card(cards)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()