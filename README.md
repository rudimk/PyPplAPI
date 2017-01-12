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

```
import pypplapi

agent = pypplapi.Agent()
```