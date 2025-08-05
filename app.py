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
    from routes.describe import bp as describe_bp
    from routes.math import bp as math_bp
    from routes.letter import bp as letter_bp
    from routes.letter_lesson import bp as lesson_bp
    from routes.letter_exercises import letter_exercises_bp
    from routes.word_lesson import bp as word_lesson_bp
    from routes.word_exercise import bp as word_exercise_bp
    from routes.letter_drawing import bp as letter_drawing_bp
    from routes.story import bp as story_routes_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(describe_bp, url_prefix="/describe")
    app.register_blueprint(math_bp, url_prefix="/math")
    app.register_blueprint(letter_bp, url_prefix="/letter")
    app.register_blueprint(lesson_bp, url_prefix="/letter_lesson")
    app.register_blueprint(letter_exercises_bp, url_prefix="/letter_exercise")
    app.register_blueprint(word_lesson_bp, url_prefix="/word_lesson")
    app.register_blueprint(word_exercise_bp, url_prefix="/word_exercise")
    app.register_blueprint(letter_drawing_bp, url_prefix="/letter_drawing")
    app.register_blueprint(story_routes_bp, url_prefix="/story")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
