# 6-1. Person
person = {
    'first_name': 'John',
    'last_name': 'Pecoraro',
    'age': 19,
    'city': 'Howell'
}

print("First name:", person['first_name'])
print("Last name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])


# 6-2. Favorite Numbers
favorite_numbers = {
    'Alice': 7,
    'Bob': 12,
    'Charlie': 3,
    'Diana': 9,
    'Ethan': 5
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


# 6-3. Glossary
glossary = {
    'variable': 'A named storage location for data.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'An ordered collection of items in Python.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A block of code that performs a specific task when called.'
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")


# 6-4. Glossary 2
glossary = {
    'variable': 'A named storage location for data.',
    'loop': 'A way to repeat a block of code multiple times.',
    'list': 'An ordered collection of items in Python.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A block of code that performs a specific task when called.',
    'tuple': 'An immutable ordered collection of items.',
    'set': 'An unordered collection of unique items.',
    'boolean': 'A data type that can be either True or False.',
    'string': 'A sequence of characters.',
    'integer': 'A whole number, positive or negative.'
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}")


# 6-5. Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers mentioned:")
for river in rivers.keys():
    print(river.title())

print("\nCountries mentioned:")
for country in rivers.values():
    print(country.title())


# 6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_to_poll = ['jen', 'sarah', 'mike', 'phil', 'anna']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take the favorite languages poll!")


# 6-7. People
person1 = {
    'first_name': 'John',
    'last_name': 'Pecoraro',
    'age': 19,
    'city': 'Howell'
}

person2 = {
    'first_name': 'Sarah',
    'last_name': 'Miller',
    'age': 22,
    'city': 'New York'
}

person3 = {
    'first_name': 'Alex',
    'last_name': 'Brown',
    'age': 25,
    'city': 'Boston'
}

people = [person1, person2, person3]

for person in people:
    print("\nPerson Info:")
    for key, value in person.items():
        print(f"{key.title()}: {value}")


# 6-8. Pets
pet1 = {'animal': 'dog', 'owner': 'Jake'}
pet2 = {'animal': 'cat', 'owner': 'Lily'}
pet3 = {'animal': 'parrot', 'owner': 'Tom'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nPet Info:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")


# 6-9. Favorite Places
favorite_places = {
    'Alice': ['Paris', 'New York', 'London'],
    'Bob': ['Tokyo', 'Sydney'],
    'Charlie': ['Rome']
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")


# 6-10. Favorite Numbers (multiple numbers per person)
favorite_numbers = {
    'Alice': [7, 11],
    'Bob': [12, 42],
    'Charlie': [3, 8, 15],
    'Diana': [9],
    'Ethan': [5, 99]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")


# 6-11. Cities
cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the city of lights.'
    },
    'new york': {
        'country': 'usa',
        'population': '8.5 million',
        'fact': 'Famous for Times Square and Broadway.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'World’s most populous metropolitan area.'
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")


# 6-12. Extensions (extending the cities program)
cities_extended = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the city of lights.',
        'founded': '3rd century BC',
        'landmark': 'Eiffel Tower'
    },
    'new york': {
        'country': 'usa',
        'population': '8.5 million',
        'fact': 'Famous for Times Square and Broadway.',
        'founded': '1624',
        'landmark': 'Statue of Liberty'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'World’s most populous metropolitan area.',
        'founded': '1457',
        'landmark': 'Tokyo Tower'
    }
}

print("\nExtended Cities Info:")
for city, info in cities_extended.items():
    print(f"\n{city.title()}:")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")
