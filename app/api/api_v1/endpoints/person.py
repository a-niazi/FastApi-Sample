from fastapi import APIRouter, Body, Depends
from typing import List
from ....models.person import Person

router = APIRouter()

persons = []


@router.post('/add')
async def add(data: Person):
	received = data.dict()
	persons.append({
		"name": received['name'],
		"family": received['family'],
		"birthdate": received['birthdate'],
		"address": received['address'],
		"telephone": received['telephone'],
		"email": received['email']
	})
	return {'person with name {} added'.format(received['name'])}


# http://127.0.0.1:8000/getcars
@router.get('/getall', response_model=List[Person])
async def index():
	return persons
