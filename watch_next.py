# Load SpaCy and its library
import spacy
nlp = spacy.load('en_core_web_md')

def watch_next(description):
    # Create a dictionary when keys are the titles and values are descriptions 
    descriptions_dict = {
        "Movie A" : "When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
        "Movie B" : "After the death of Superman, several new people present themselves as possible successors.",
        "Movie C" : "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
        "Movie D" : "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
        "Movie E" : "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
        "Movie F" : "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
        "Movie G" : "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
        "Movie H" : "A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
        "Movie I" : "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in town.",
        "Movie J" : "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney.",   
    }
    
    # Create a NLP object for the desciption which was taken in before
    model_descript = nlp(description)
    # Generate keys list and create a list of similarities between the model descript and other descripts in the dict
    keys = descriptions_dict.keys()
    similarity_list = []
    # Loop over the description dict keys to populate the similarity list
    for movie in keys:
        similarity = nlp(descriptions_dict[movie]).similarity(model_descript)
        similarity_list.append(similarity)
    # Loop again the keys list, then find the key having the max similarity. Print the title (key) out with the description nicely.  
    for movie in keys:
        if max(similarity_list) == nlp(descriptions_dict[movie]).similarity(model_descript):
            print(f"After Planet Hulk, the movie should be watched next is: {movie}, with the description is: {descriptions_dict[movie]}")
    
# Input the description to compare and run the function
desciption_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
watch_next(desciption_to_compare)