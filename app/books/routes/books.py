from flask import Flask, render_template, request, redirect, url_for
import requests


def books():
    """
    Render the 'Otterbrook's Books' page.
    Fetches book data from Google Books API based on user query.
    """
    books = []
    no_results = False
    error = None

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        sort_by = request.form.get('sort_by', 'rating_desc')

        # Validate query
        if not query or len(query) < 2:
            error = "Please enter a search query with at least 2 characters."
        else:
            url = f"https://www.googleapis.com/books/v1/volumes?q={query}&projection=full&maxResults=15&key=API_KEY_HERE"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if "items" in data:
                    for item in data["items"]:
                        volume_info = item.get("volumeInfo", {})
                        image_links = volume_info.get("imageLinks", {})
                        books.append({
                            "title": volume_info.get("title", "No title available"),
                            "authors": volume_info.get("authors", ["Unknown"]),
                            "publisher": volume_info.get("publisher", "Unknown"),
                            "published_date": volume_info.get("publishedDate", "Unknown"),
                            "description": volume_info.get("description", "No description available"),
                            "page_count": volume_info.get("pageCount", "Unknown"),
                            "categories": volume_info.get("categories", []),
                            "average_rating": volume_info.get("averageRating", 0),
                            "ratings_count": volume_info.get("ratingsCount", 0),
                            "image": image_links.get("thumbnail", ""),
                            "preview_link": volume_info.get("previewLink", "#"),
                            "info_link": volume_info.get("infoLink", "#"),
                        })

                    # Apply sorting (similar logic as before)
                    books.sort(key=lambda x: x["average_rating"], reverse=(sort_by == "rating_desc"))
                    # Add sorting for other criteria...
                else:
                    no_results = True
            else:
                no_results = True

    return render_template("books.html", title="Otterbrook's Books", books=books, no_results=no_results, error=error)