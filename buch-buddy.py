import openai
import os

# Set up OpenAI API key
with open('OPENAI_API_KEY.txt', 'r') as f:
    api_key = f.read().strip()

openai.api_key = api_key

def get_book_recommendations(genre, sub_genre, age_recommendation, vulgarity_rating, adult_interactions_rating):
    prompt = f"Find books that match the following criteria:\n\nGenre: {genre}\nSub-genre: {sub_genre}\nAge Recommendation: {age_recommendation}\nVulgarity Rating: {vulgarity_rating}\nAdult Interactions Rating: {adult_interactions_rating}\n\nRecommended books:\n\n"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.8,
    )

    recommended_books = response.choices[0].text.strip()

    return recommended_books


if __name__ == "__main__":
    genre = input("Enter the genre: ")
    sub_genre = input("Enter the sub-genre: ")
    age_recommendation = input("Enter the age recommendation: ")
    vulgarity_rating = input("Enter the vulgarity rating (1-10): ")
    adult_interactions_rating = input("Enter the adult interactions rating (1-10): ")

    recommendations = get_book_recommendations(genre, sub_genre, age_recommendation, vulgarity_rating, adult_interactions_rating)

    print("\nHere are your recommended books:\n")
    print(recommendations)

