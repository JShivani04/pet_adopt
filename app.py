from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory pet data
pets = [
    {"id": 1, "name": "Bella", "type": "Dog", "age": "2 years", "description": "Friendly golden retriever", "adopted": False},
    {"id": 2, "name": "Luna", "type": "Cat", "age": "1 year", "description": "Calm and cuddly", "adopted": False},
]

@app.route('/')
def home():
    available_pets = [pet for pet in pets if not pet['adopted']]
    return render_template('index.html', pets=available_pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        pet_type = request.form['type']
        age = request.form['age']
        description = request.form['description']

        new_pet = {
            "id": len(pets) + 1,
            "name": name,
            "type": pet_type,
            "age": age,
            "description": description,
            "adopted": False
        }
        pets.append(new_pet)
        return redirect(url_for('home'))
    return render_template('add_pet.html')

@app.route('/adopt/<int:pet_id>', methods=['GET', 'POST'])
def adopt_pet(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if not pet:
        return "Pet not found", 404

    if request.method == 'POST':
        pet['adopted'] = True
        return redirect(url_for('home'))

    return render_template('adopt_pet.html', pet=pet)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

