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
    from routes.words import bp as words_routes_bp
    from routes.word_quiz import bp as  word_quiz_routes_bp
    from routes.letter_drawing import bp as letter_drawing_bp
    from routes.story import bp as story_routes_bp
    from routes.sentences import bp as sentences_bp
    from routes.echo_writer import bp as echo_writer_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(describe_bp, url_prefix="/describe")
    app.register_blueprint(math_bp, url_prefix="/math")
    app.register_blueprint(letter_bp, url_prefix="/letter")
    app.register_blueprint(lesson_bp, url_prefix="/letter_lesson")
    app.register_blueprint(letter_exercises_bp, url_prefix="/letter_exercise")
    app.register_blueprint(words_routes_bp, url_prefix="/words")
    app.register_blueprint(word_lesson_bp, url_prefix="/word_lesson")
    app.register_blueprint(word_quiz_routes_bp, url_prefix="/word_quiz")
    app.register_blueprint(letter_drawing_bp, url_prefix="/letter_drawing")
    app.register_blueprint(story_routes_bp, url_prefix="/story")
    app.register_blueprint(sentences_bp, url_prefix="/sentences")
    app.register_blueprint(echo_writer_bp, url_prefix="/echo_writer")
    
    app.secret_key = os.urandom(24)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
