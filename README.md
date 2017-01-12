# PyPplAPI
A Python wrapper around pplapi | http://pplapi.com

## Why?
I'm interested in cliodynamics, and there are a lot of cooperative games I'd like to model using human traits. Pplapi has some
brilliant data points, and I figured having a Python wrapper around it made a lot of sense.

## Installatioh

Grab it off PyPI:
```pip install pypplapi```

## Usage

To create a random agent, simply instantiate an `Agent` object:

```python
import pypplapi

agent = pypplapi.Agent()
```

You can inspect the agent:

```python
>>> dir(agent)
['__doc__', '__init__', '__module__', 'age', 'agent_id', 'agent_id_str', 'agreeableness', 'conscientiousness', 'country_name', 'country_tld', 'dob', 'extraversion', 'income', 'internet', 'language', 'latitude', 'longitude', 'neuroticism', 'openness', 'religion', 'sex']
```

If the need arises, you can always get a dictionary from the `agent` instance:

```python
>>> agent.__dict__
{'agent_id_str': u'DJG-gQw', 'language': u'local dialect', 'religion': u'Muslim', 'country_tld': u'id', 'age': 4, 'internet': False, 'longitude': 119.80829503859, 'sex': u'Female', 'dob': u'2013-01-07', 'extraversion': 0.6680558038576523, 'neuroticism': 0.736599089686382, 'agreeableness': -0.6777542230076916, 'agent_id': 3141190018, 'conscientiousness': 1.9636977350197746, 'income': 5303, 'country_name': u'Indonesia', 'openness': 1.769827633226628, 'latitude': -5.298874128938844}
```

Right now, it's not possible to instantiate a random sample set of agents - I plan to add that soon.