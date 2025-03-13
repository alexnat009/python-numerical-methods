import json

school = {
    "school": "UC Berkeley",
    "address": {
        "city": "Berkeley",
        "state": "California",
        "postal": "94720"
    },

    "list": [
        "student 1",
        "student 2",
        "student 3"
    ],

    "array": [1, 2, 3]
}
json.dump(school, open('data/school.json', 'w'))

my_school = json.load(open('data/school.json', 'r'))
print(my_school)