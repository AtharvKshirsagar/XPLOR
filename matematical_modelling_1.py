def calculate_city_score(city_answers):
    city_values = {
        'Mumbai': 3,
        'Bangalore': 2,
        'Delhi': 2,
        'Other': 1
    }
    total_city_score = sum(city_values.get(answer, 0) for answer in city_answers)
    weighted_city_score = total_city_score / len(city_answers)
    return weighted_city_score

def calculate_mountains_beaches_score(mountains_beaches_answers):
    mountains_beaches_values = {
        'Beaches': 3,
        'Mountains': 1
    }
    total_mountains_beaches_score = sum(mountains_beaches_values.get(answer, 0) for answer in mountains_beaches_answers)
    weighted_mountains_beaches_score = total_mountains_beaches_score / len(mountains_beaches_answers)
    return weighted_mountains_beaches_score

def calculate_baking_party_score(baking_party_answers):
    baking_party_values = {
        'Baking': 3,
        'Hosting': 2
    }
    total_baking_party_score = sum(baking_party_values.get(answer, 0) for answer in baking_party_answers)
    weighted_baking_party_score = total_baking_party_score / len(baking_party_answers)
    return weighted_baking_party_score

def calculate_books_podcasts_score(books_podcasts_answers):
    books_podcasts_values = {
        'Podcasts': 3,
        'Books': 1
    }
    total_books_podcasts_score = sum(books_podcasts_values.get(answer, 0) for answer in books_podcasts_answers)
    weighted_books_podcasts_score = total_books_podcasts_score / len(books_podcasts_answers)
    return weighted_books_podcasts_score

def calculate_rollercoaster_skydiving_score(rollercoaster_skydiving_answers):
    rollercoaster_skydiving_values = {
        'Roller Coaster': 3,
        'Skydiving': 1
    }
    total_rollercoaster_skydiving_score = sum(rollercoaster_skydiving_values.get(answer, 0) for answer in rollercoaster_skydiving_answers)
    weighted_rollercoaster_skydiving_score = total_rollercoaster_skydiving_score / len(rollercoaster_skydiving_answers)
    return weighted_rollercoaster_skydiving_score

def calculate_art_gallery_street_festival_score(art_gallery_street_festival_answers):
    art_gallery_street_festival_values = {
        'Art all the way': 3,
        'Street Stuff': 1
    }
    total_art_gallery_street_festival_score = sum(art_gallery_street_festival_values.get(answer, 0) for answer in art_gallery_street_festival_answers)
    weighted_art_gallery_street_festival_score = total_art_gallery_street_festival_score / len(art_gallery_street_festival_answers)
    return weighted_art_gallery_street_festival_score

def calculate_opera_comedy_show_score(opera_comedy_show_answers):
    opera_comedy_show_values = {
        'Opera': 3,
        'Comedy': 1
    }
    total_opera_comedy_show_score = sum(opera_comedy_show_values.get(answer, 0) for answer in opera_comedy_show_answers)
    weighted_opera_comedy_show_score = total_opera_comedy_show_score / len(opera_comedy_show_answers)
    
    return weighted_opera_comedy_show_score

def classify_person(ses_score, disc_score, city_score, mountains_beaches_score, baking_party_score,
                    books_podcasts_score, rollercoaster_skydiving_score, art_gallery_street_festival_score,
                    opera_comedy_show_score):
    
    ses_ranges = {
        (0, 1.5): 'Growing class',
        (1.5, 2.5): 'Middle class',
        (2.5, 3.5): 'Upper middle class',
        (3.5, 5): 'Upper class'
    }
    
    disc_ranges = {
        (0, 1.5): 'dominance',
        (1.5, 2.5): 'influence',
        (2.5, 3.5): 'steadiness',
        (3.5, 5): 'conscientiousness'
    }
    
    ses_category = next(category for (start, end), category in ses_ranges.items() if start <= ses_score < end)
    disc_category = next(category for (start, end), category in disc_ranges.items() if start <= disc_score < end)
    
    return ses_category, disc_category

# Example usage
city_answers = ['Mumbai', 'Delhi', 'Other']
mountains_beaches_answers = ['Beaches', 'Mountains']
baking_party_answers = ['Baking', 'Hosting']
books_podcasts_answers = ['Podcasts', 'Books']
rollercoaster_skydiving_answers = ['Roller Coaster', 'Skydiving']
art_gallery_street_festival_answers = ['Art all the way', 'Street Stuff']
opera_comedy_show_answers = ['Opera', 'Comedy']

city_score = calculate_city_score(city_answers)
mountains_beaches_score = calculate_mountains_beaches_score(mountains_beaches_answers)
baking_party_score = calculate_baking_party_score(baking_party_answers)
books_podcasts_score = calculate_books_podcasts_score(books_podcasts_answers)
rollercoaster_skydiving_score = calculate_rollercoaster_skydiving_score(rollercoaster_skydiving_answers)
art_gallery_street_festival_score = calculate_art_gallery_street_festival_score(art_gallery_street_festival_answers)
opera_comedy_show_score = calculate_opera_comedy_show_score(opera_comedy_show_answers)

# Calculate the average scores
ses_score = (city_score + mountains_beaches_score) / 2
disc_score = (baking_party_score + books_podcasts_score + rollercoaster_skydiving_score + art_gallery_street_festival_score + opera_comedy_show_score) / 5

ses_category, disc_category = classify_person(ses_score, disc_score, city_score, mountains_beaches_score, baking_party_score,
                    books_podcasts_score, rollercoaster_skydiving_score, art_gallery_street_festival_score,
                    opera_comedy_show_score)

print(f"Socio-economic status category: {ses_category}")
print(f"DISC personality category: {disc_category}")

