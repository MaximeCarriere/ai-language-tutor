import os
from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), "templates"),
        static_folder=os.path.join(os.getcwd(), "static"),
    )

    # --- Register blueprints ---
    from routes.home import bp as home_bp
    from routes.vocab import bp as vocab_bp
    from routes.describe import bp as describe_bp
    from routes.math import bp as math_bp
    from routes.letter import bp as letter_bp
    from routes.letter_lesson import bp as lesson_bp
    from routes.letter_exercises import letter_exercises_bp

    app.register_blueprint(home_bp)  # root
    app.register_blueprint(vocab_bp, url_prefix="/vocab")
    app.register_blueprint(describe_bp, url_prefix="/describe")
    app.register_blueprint(math_bp, url_prefix="/math")
    app.register_blueprint(letter_bp, url_prefix="/letter")
    app.register_blueprint(lesson_bp, url_prefix="/letter_lesson")
    app.register_blueprint(letter_exercises_bp, url_prefix="/letter_exercise")  # makes /letter_exercise

    return app


if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(debug=True)
