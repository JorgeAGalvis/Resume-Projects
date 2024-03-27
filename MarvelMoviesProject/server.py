from flask import Flask
from flask import render_template, redirect, url_for
from flask import Response, request, jsonify

# Video: https://youtu.be/dLkiGniT1l0

app = Flask(__name__)

# auto increment the id 
movie_id = 11

data = {
    "1": {
        "id": "1",
        "title": "Captain America: The First Avenger",
        "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR9mEP82JfY12jfFuNrRbGQwWMa4iQqHmvnud38iG_Tc5cs91uG",
        "trailer":"https://www.youtube.com/embed/JerVrbLldXw",
        "year": "2011",
        "summary": "Steve Rogers, a frail but determined young man, undergoes a super-soldier transformation during World War II, becoming Captain America and leading the fight against Hydra and the Red Skull.",
        "runtime":"2h 4m",
        "director": ["Joe Johnston"],
        "budget": "$140,000,000",
        "stars": ["Chris Evans", "Hayley Atwell", "Sebastian Stan", "Tommy Lee Jones", "Hugo Weaving"],
        "score": "6.9",
        "genres": ["Action", "War", "Drama"], 
        "similar": ["3", "11"], 
        "rating":"PG-13"
    },
    "2": {
        "id": "2",
        "title": "Avengers: Infinity War",
        "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRL8EPSWPqTOpTYOPOE12gXoFrhXqCRu4wkcUI-CoEalqLhZDQg",
        "trailer":"https://www.youtube.com/embed/QwievZ1Tx-8",
        "year": "2018",
        "summary": "Captain America joins forces with Iron Man, Thor, Hulk, Black Widow, and Hawkeye to form the Avengers, a team of superheroes assembled to save the world from the threat of Loki and his alien army.",
        "runtime":"2h 29m",
        "director": ["Anthony Russo", "Joe Russo"],
        "budget": "$321,000,000",
        "stars": ["Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Scarlett Johansson", "Mark Ruffalo"],
        "score": "8.4",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "similar": ["4"], 
        "rating":"PG-13"
    },
    "3": {
        "id": "3",
        "title": "Captain America: The Winter Soldier",
        "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS3_h4fl5l7FFJpW1uIEIPzduLOomGEiS_s-tXK42bDy5X8v3k6",
        "trailer":"https://www.youtube.com/embed/7SlILk2WMTI",
        "year": "2014",
        "summary": "Captain America teams up with Black Widow and Falcon to uncover a conspiracy within S.H.I.E.L.D. while facing a mysterious assassin known as the Winter Soldier, who has a personal connection to Steve Rogers.",
        "runtime":"2h 16m",
        "director": ["Anthony Russo", "Joe Russo"],
        "budget": "$177,000,000",
        "stars": ["Chris Evans", "Scarlett Johansson", "Anthony Mackie", "Sebastian Stan", "Samuel L. Jackson"],
        "score": "7.7",
        "genres": ["Action", "Sci-Fi", "Thriller"],
        "similar": ["1", "11"],
        "rating":"PG-13"
    },
    "4": {
        "id": "4",
        "title": "Avengers: Endgame",
        "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQIgtoVIPZ7Gfavhuq_Q5CQQP82t1oaClm6UMKzP4qEqnmPmt8e",
        "trailer":"https://www.youtube.com/embed/TcMBFSGVi1c",
        "year": "2019",
        "runtime":"3h 1m",
        "summary": "Captain America, along with the remaining Avengers, embarks on a time-traveling mission to undo the devastating effects of Thanos' snap and restore balance to the universe.",
        "director": ["Anthony Russo", "Joe Russo"],
        "budget": "$356,000,000",
        "stars": ["Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo", "Scarlett Johansson"],
        "score": "8.4",
        "genres": ["Adventure", "Sci-Fi", "Thriller"],
        "similar": ["2"],
        "rating":"PG-13"
    },
    "5": {
        "id": "5",
        "title": "Black Panther",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2EvJxM6r1R2ZOnSev6hqzT9nfW8Y0CRPN1mWHaQzOrd9EGPIh",
        "trailer":"https://www.youtube.com/embed/xjDjIWPwcPU",
        "year": "2018",
        "runtime":"2h 41m",
        "summary": "T'Challa, the newly crowned king of Wakanda, must defend his nation and the Black Panther mantle when an old adversary challenges him, putting the fate of Wakanda and the world at risk.",
        "director": ["Ryan Coogler"],
        "budget": "$200,000,000",
        "stars": ["Chadwick Boseman", "Michael B. Jordan", "Lupita Nyong'o", "Danai Gurira", "Letitia Wright"],
        "score": "7.3",
        "genres": ["Action", "Adventure", "Sci-Fi", "Thriller"],
        "similar": ["4", "2"],
        "rating":"PG-13"
    },
    "6": {
        "id": "6",
        "title": "Thor: Ragnarok",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9Z2q1PovL0sLiR3te8fAROw9XCmv-Ep7E76ZWPgfTmvG5qfAo",
        "trailer":"https://www.youtube.com/embed/ue80QwXMRHg",
        "year": "2017",
        "runtime":"2h 10m",
        "summary": "Thor finds himself imprisoned on the other side of the universe and must race against time to stop the ruthless Hela from destroying Asgard and its civilization.",
        "director": ["Taika Waititi"],
        "budget": "$180,000,000",
        "stars": ["Chris Hemsworth", "Tom Hiddleston", "Cate Blanchett", "Mark Ruffalo", "Jeff Goldblum"],
        "score": "7.9",
        "genres": ["Action", "Adventure", "Sci-Fi", "Thriller"],
        "similar": ["4", "2"],
        "rating":"PG-13"
    },
    "7": {
        "id": "7",
        "title": "Guardians of the Galaxy",
        "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTHwG1tMhgfeajy6fxnYWICp46rZM5mfU1_bGkLBfy6AOTON2Jc",
        "trailer":"https://www.youtube.com/embed/d96cjJhvlMA",
        "year": "2014",
        "summary": "A group of intergalactic misfits, including Star-Lord, Gamora, Drax, Rocket, and Groot, come together to protect a powerful orb from falling into the hands of the villainous Ronan the Accuser.",
        "runtime":"2h 2m",
        "director": ["James Gunn"],
        "budget": "$170,000,000",
        "stars": ["Chris Pratt", "Zoe Saldana", "Dave Bautista", "Vin Diesel", "Bradley Cooper"],
        "score": "8.0",
        "genres": ["Action", "Adventure", "Comedy"],
        "similar": ["4", "2"],
        "rating":"PG-13"
    },
    "8": {
        "id": "8",
        "title": "Doctor Strange",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-TSpra_ikBAnws76-47V0sSvFZrsYrUMaA1FwDxTzGpShcWhl",
        "trailer":"https://www.youtube.com/embed/HSzx-zryEgM",
        "year": "2016",
        "summary": "Dr. Stephen Strange, a brilliant but arrogant surgeon, seeks mystical help after a car accident robs him of his skills. He discovers a hidden world of magic and alternate dimensions, becoming the Sorcerer Supreme.",
        "runtime":"1h 55m",
        "director": ["Scott Derrickson"],
        "budget": "$165,000,000",
        "stars": ["Benedict Cumberbatch", "Chiwetel Ejiofor", "Rachel McAdams", "Benedict Wong", "Mads Mikkelsen"],
        "score": "7.5",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "similar": ["4", "2"],
        "rating":"PG-13"
    },
    "9": {
        "id": "9",
        "title": "Spider-Man: Homecoming",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRAui4j_CP5JitmzERck2NTzo3pgk7OWDttnMIAn3EQjAzLUqA",
        "trailer":"https://www.youtube.com/embed/rk-dF1lIbIg",
        "year": "2017",
        "summary": "Peter Parker balances life as a high school student and his superhero alter ego Spider-Man. When the Vulture emerges as a new villain, Spider-Man must navigate the challenges of being a hero and a teenager.",
        "runtime":"2h 13m",
        "director": ["Jon Watts"],
        "budget": "$175,000,000",
        "stars": ["Tom Holland", "Michael Keaton", "Zendaya", "Robert Downey Jr.", "Marisa Tomei"],
        "score": "7.4",
        "genres": ["Action", "Adventure", "Sci-Fi"], 
        "similar": ["11","4", "2"],
        "rating":"PG-13"
    },
    "10": {
        "id": "10",
        "title": "Captain Marvel",
        "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTvwUrWZA7dCe_ggg96fG625dfkSMopojxVqCQAuFBff88WdpV5",
        "trailer":"https://www.youtube.com/embed/Z1BCujX3pw8",
        "year": "2019",
        "summary": "Vers, a Kree warrior with no memory of her past, discovers her true identity as Carol Danvers, aka Captain Marvel. As she unlocks her powers, she becomes a key player in the cosmic battle between the Kree and Skrull races.",
        "runtime":"2h 4m",
        "director": ["Anna Boden", "Ryan Fleck"],
        "budget": "$152,000,000",
        "stars": ["Brie Larson", "Samuel L. Jackson", "Ben Mendelsohn", "Jude Law", "Annette Bening"],
        "score": "6.8",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "similar": ["4"], 
        "rating":"PG-13"
    },
    "11": {
        "id": "11",
        "title": "Captain America: Civil War",
        "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQDUT2z23nP902Vj41WXoDBqHFrcKPqUVOuXMzjRUjJcMCbvnDn",
        "trailer":"https://www.youtube.com/embed/dKrVegVI0Us",
        "year": "2016",
        "summary": "Political involvement in the Avengers' affairs causes a rift between Captain America and Iron Man.",
        "runtime":"2h 28m",
        "director": ["Anthony Russo", "Joe Russo"],
        "budget": "$250,000,000",
        "stars": ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson", "Sebastian Stan", "Anthony Mackie"],
        "score": "7.8",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "similar": ["1", "3"], 
        "series":["1", "3", "11"],
        "rating":"PG-13"
    }
}

banner_data = {
    "title":"Explore the Marvel Cinematic Universe", 
    "description":"Captivating trailers, directors, cast members, and more",
    "image":"https://images.squarespace-cdn.com/content/v1/51b3dc8ee4b051b96ceb10de/1556641213747-YJ8F0ER0GAZFKU0FJRSJ/did-you-notice-that-the-opening-credits-of-avengers-endgame-only-included-the-surviving-heroes-social.jpg?format=2500w", 
    "alt":"marvel banner"
}

@app.route('/')
def home(): 
    global data
    global banner_data
    top_movies = sorted(data.values(), key=lambda x: float(x["score"]), reverse=True)[:3]
    return render_template('home.html', top_movies=top_movies, banner_data=banner_data)
      

@app.route('/search')
def search():
    query = request.args.get('search-input', '').strip().lower()
    if not query: 
        return render_template('search.html', search_result=[], query=query)

    global data
    filtered_by_title = [movie for movie in data.values() if query in movie["title"].lower().strip()]
    filtered_by_director = [movie for movie in data.values() if any(query.lower() in director.lower() for director in movie["director"])]
    filtered_by_star = [movie for movie in data.values() if any(query.lower() in star.lower() for star in movie["stars"])]
    filtered_by_genre = [movie for movie in data.values() if any(query.lower() in star.lower() for star in movie["genres"])]

    return render_template('search.html', 
                           filtered_by_title=filtered_by_title, 
                           filtered_by_director=filtered_by_director,
                           filtered_by_star=filtered_by_star,
                           filtered_by_genre=filtered_by_genre,
                           query=query)

@app.route('/view/<id>')
def view(id=None):
    global data
    movie = data[id]

    similar_movies = [data[similar_movie] for similar_movie in movie['similar']]

    return render_template("view.html", movie=movie, similar_movies=similar_movies)


@app.route('/add')
def add(): 
    global data 
    similar_movies = [movie['title'] for movie in data.values()]
    return render_template("add.html", similar_movies=similar_movies)


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie(): 
    json_data = request.get_json()  # this is the new movie

    global data 
    global movie_id 

    movie_id += 1 
    new_movie_id = movie_id

    json_data["id"] = str(new_movie_id) #add the id to the received JSON new movies
    data[str(new_movie_id)] = json_data # append the new movie to the data 

    return jsonify(data[str(new_movie_id)]) #return the new movie 


@app.route('/edit/<id>')
def edit(id=None): 
    global data 
    movie_to_edit = data[id]
    
    similar_movies_to_edit = [data[similar_movie] for similar_movie in movie_to_edit['similar']]
    similar_movies = [movie['title'] for movie in data.values()]
    return render_template("edit.html", movie_to_edit=movie_to_edit, similar_movies_to_edit=similar_movies_to_edit, similar_movies=similar_movies)


@app.route('/edit_movie', methods=['GET', 'POST'])
def edit_movie():
    json_data = request.get_json()
    global data 
    data[json_data["id"]] = json_data
    return jsonify(data[json_data["id"]])

if __name__ == '__main__': 
        app.run()

