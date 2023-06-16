#import dependencies

#import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func ,inspect
import psycopg2
from config import password
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#create connection
engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5433/IMDB")



# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# State the available routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"enter the name of TV show at the url to get results for the show  eg. /api/v1.0/Breaking Bad<br/>"
        f'<br/>'
        f"/api/v1.0/TV/<br/>"
        f"enter the name of Actor at the url to get results for the actor eg./api/v1.0/Zendaya<br/>"
        f"<br/>"
        f"/api/v1.0/Actor/<br/>"
        )

@app.route("/api/v1.0/TV/<TV>")
def tvshow(TV):
    #global title,nomination,actor,award
    # reflect an existing database into a new model
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    # Save references to each table
    title = Base.classes.title
    imdb_top_250 = Base.classes.imdb_top_250
    category = Base.classes.category
    award = Base.classes.award
    nomination = Base.classes.nomination
    actor = Base.classes.actor
    network = Base.classes.network
    session = Session(engine)
    
# Perform a query to retrieve the show
    result = session.query(title.title,nomination.year,actor.actor,award.award).\
        filter(imdb_top_250.title_id == title.title_id).\
        filter(title.title_id == nomination.title_id).\
        filter(actor.actor_id == nomination.actor_id).\
        filter(award.award_id == nomination.award_id).\
        filter(title.title ==TV).\
        filter(nomination.winner==True).all()
                    
    session.close()
#create an empty list to get all the key value pairs from the above query results by looping and appending the list
    result_list = []
    for title,year,actor,award in result:
        result_dict = {}
        result_dict['Title'] = title
        result_dict['Year'] = year
        result_dict['Actor'] = actor
        result_dict['Award'] = award
        result_list.append(result_dict)

    return jsonify(result_list)


@app.route("/api/v1.0/Actor/<Actor>")

def actors(Actor):
    #global title,nomination,actor,award,category,imdb_top_250
    # reflect an existing database into a new model
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    # Save references to each table
    title = Base.classes.title
    imdb_top_250 = Base.classes.imdb_top_250
    category = Base.classes.category
    award = Base.classes.award
    nomination = Base.classes.nomination
    actor = Base.classes.actor
    network = Base.classes.network
    session = Session(engine)
    results = session.query(title.title,nomination.year,actor.actor,award.award,category.category,imdb_top_250.rank,imdb_top_250.rating).\
        filter(imdb_top_250.title_id == title.title_id).\
        filter(title.title_id == nomination.title_id).\
        filter(actor.actor_id == nomination.actor_id).\
        filter(award.award_id == nomination.award_id).\
        filter(category.category_id == nomination.category_id).\
        filter(actor.actor == Actor).\
        filter(nomination.winner==True).all()
    session.close()

    actor_list = []
    for title,year,actor,award,category,rank,rating in results:
        actor_dict = {}
        actor_dict['Title'] = title
        actor_dict['Year'] = year
        actor_dict['Actor'] = actor
        actor_dict['Award'] = award
        actor_dict['Category'] = category
        actor_dict['Rank'] = rank
        actor_dict['Rating'] = rating
        actor_list.append(actor_dict)

    return jsonify(actor_list)
    
if __name__ == '__main__':
    app.run(debug=True)