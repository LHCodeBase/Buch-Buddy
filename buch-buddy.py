#!/usr/bin/env python3

# TODO ensure no duplicates // result doesn't contain prompt
# TODO check for duplictes
    # TODO if duplicates, query user and run fresh funcion on the answer.
# TODO Ensure numbered metrics are being returned.
# TODO Ensure books actually exist
# TODO Ensure results are books only. No comic books or manga currently.


import openai
import os
import json

# Set some variables
book_type = "title" # title, author, series

# Set up OpenAI API key
with open('OPENAI_API_KEY.txt', 'r') as f:
    api_key = f.read().strip()

openai.api_key = api_key

def get_book_recommendations(genre, sub_genre, vulgarity_rating, adult_interactions_rating):
    prompt = f"Find books that match the following criteria:\n\nGenre: {genre}\nSub-genre: {sub_genre}\nVulgarity Rating: {vulgarity_rating}\nAdult Interactions Rating: {adult_interactions_rating}\n\nRecommended books:\n\n"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.8,
    )

    recommended_books = response.choices[0].text.strip()
    print(f" recommended books: {recommended_books}")

    return recommended_books

def get_book_properties(*book_name):
    prompt = f"For the book title, series or author {book_name}: Return json for the following keys:name, genre, sub_genre, vulgarity_rating (1-10),adult_interactions_rating (1-10)"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.4,
    )

    print(response)
    print(response.choices[0].text.strip())
    #return response.choices[0].text.strip()
    return response

def book2json(book_name): # TODO Rename me
    # TODO Make this return a list with the dictionary name being the book title.
    # or redo it with decorators
    book_json = json.loads(
        json.dumps(
            get_book_properties(book_name),
            default=lambda x: x.__dict__
        )
    )
    # Get text to convert to dict. ["choices"][0]["text"].replace("\n",",")
    return book_json

    

if __name__ == "__main__":
    pass
    #book_name = input("Enter a book name: ")
    #get_book_properties(book_name)

#    genre = input("Enter the genre: ")
#    sub_genre = input("Enter the sub-genre: ")
#    age_recommendation = input("Enter the age recommendation: ")
#    vulgarity_rating = input("Enter the vulgarity rating (1-10): ")
#    adult_interactions_rating = input("Enter the adult interactions rating (1-10): ")

#    recommendations = get_book_recommendations(genre, sub_genre, age_recommendation, vulgarity_rating, adult_interactions_rating)

#    print("\nHere are your recommended books:\n")
#    print(recommendations)

