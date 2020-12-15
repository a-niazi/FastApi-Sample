from pydantic import BaseModel, Field


class Person(BaseModel):
	name: str = Field(..., description="Name")
	family: str = Field(..., description="family")
	birthdate: int = Field(..., description="birthdate")
	address: str = Field(..., description="address")
	telephone: str = Field(..., description="telephone")
	email: str = Field(..., description="email")

	class Config:
		schema_extra = {
			"example": {
				"name": 'Amir',
				"family": 'Niazi',
				"birthdate": '1990',
				"address": '',
				"telephone": '',
				"email": 'amir.niazi.2010@gmail.com'
			}
		}

