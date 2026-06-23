from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    result_html = ""
    if request.method == "POST":
        product = request.form.get("product", "")
        result = product
        result_html = f'<div class="result"><strong>You searched for:</strong> {product}</div>'

    return f"""
    <html>
    <head>
        <title>Canon G7X Stock Watch</title>
        <style>
            body {{
                font-family: Georgia, serif;
                background-color: #fff0f5;
                color: #3a3a3a;
                max-width: 600px;
                margin: 60px auto;
                padding: 0 20px;
            }}
            h1 {{
                color: #c2185b;
                font-size: 2em;
                margin-bottom: 5px;
            }}
            p {{
                color: #666;
            }}
            input[type="text"] {{
                padding: 10px;
                border: 2px solid #f48fb1;
                border-radius: 8px;
                font-size: 1em;
                width: 260px;
                outline: none;
            }}
            input[type="text"]:focus {{
                border-color: #c2185b;
            }}
            button {{
                padding: 10px 20px;
                background-color: #e91e8c;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 1em;
                cursor: pointer;
                margin-left: 8px;
            }}
            button:hover {{
                background-color: #c2185b;
            }}
            .result {{
                margin-top: 20px;
                background: #fce4ec;
                border-left: 4px solid #e91e8c;
                padding: 12px 16px;
                border-radius: 6px;
            }}
        </style>
    </head>
    <body>
        <h1>Canon G7X Stock Watch</h1>
        <p>Track Canon G7X availability across major retailers.</p>
        <form method="POST">
            <label>Enter a product to track:</label><br><br>
            <input type="text" name="product" placeholder="e.g. Canon G7X" />
            <button type="submit">Search</button>
        </form>
        {result_html}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
