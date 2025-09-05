from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome!</title>
        <style>
            body {
                background: linear-gradient(to right, #4facfe, #00f2fe);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                font-family: Arial, sans-serif;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.7);  /* Dark semi-transparent background */
                padding: 40px;
                border-radius: 20px;
                color: white;  /* White text for contrast against dark background */
            }
            h1 {
                font-size: 2.5em;
                margin-bottom: 20px;
                color: #FFD700;  /* Gold color for heading for extra contrast */
            }
            p {
                font-size: 1.2em;
                margin: 10px 0;
            }
            .highlight {
                color: #FF6B6B;  /* Coral color for important text */
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 Hi Buddy!</h1>
            <p>Hey buddy, hope you're doing well!</p>
            <p>This is my <span class="highlight">Best Version </span> deployment! 🚀</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
