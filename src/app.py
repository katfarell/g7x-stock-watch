from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        product = request.form.get("product", "")
        result = f"<p><strong>You searched for:</strong> {product}</p>"

    return f"""
    <h1>Canon G7X Stock Watch</h1>
    <p>Track Canon G7X availability across major retailers.</p>
    <form method="POST">
        <label>Enter a product to track:</label><br><br>
        <input type="text" name="product" placeholder="e.g. Canon G7X" />
        <button type="submit">Search</button>
    </form>
    {result}
    """

if __name__ == "__main__":
    app.run(debug=True)
