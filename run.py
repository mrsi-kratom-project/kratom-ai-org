from flask import Flask, jsonify, render_template, current_app
from app import app

@app.route('/')
def home():
    # This will print the path in your terminal console
    print(f"Template folder: {current_app.template_folder}")
    print(f"Root path: {current_app.root_path}")
    return render_template('index.html')

@app.route('/api/network')
def get_network():
    # Placeholder for your NetworkX logic
    return jsonify({"message": "NetworkX data will go here"})

if __name__ == '__main__':
    # Use 0.0.0.0 so the container is accessible from outside 
    app.run(host='0.0.0.0', port=5000, debug=True)