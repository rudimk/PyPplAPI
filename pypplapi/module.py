import requests as r

class Agent:

    # Define agent attributes.

    agent_id = None
    agent_id_str = None
    country_tld = None
    country_name = None
    dob = None
    age = None
    sex = None
    income = None
    religion = None
    internet = None
    language = None
    latitude = None
    longitude = None
    openness = None
    conscientiousness = None
    agreeableness = None
    extraversion = None
    neuroticism = None

    # A constructor that calls the pplapi random agent endpoint, and initializes an agent object.

    def __init__(self):
        response = r.get('http://pplapi.com/random.json')
        raw_data = response.json()
        self.agent_id = raw_data['id']
        self.agent_id_str = raw_data['id_str']
        self.country_tld = raw_data['country_tld']
        self.country_name = raw_data['country_name']
        self.dob = raw_data['date_of_birth']
        self.age = raw_data['age']
        self.sex = raw_data['sex']
        self.income = raw_data['income']
        self.religion = raw_data['religion']
        self.internet = raw_data['internet']
        self.language = raw_data['language']
        self.latitude = raw_data['latitude']
        self.longitude = raw_data['longitude']
        self.openness = raw_data['openness']
        self.conscientiousness = raw_data['conscientiousness']
        self.agreeableness = raw_data['agreeableness']
        self.extraversion = raw_data['extraversion']
        self.neuroticism = raw_data['neuroticism']

