from flask import jsonify, render_template


def configure(app):
    @app.route("/")
    def index():
        return "Hello!"

    @app.route("/api")
    def api():
        return jsonify(data={"name": "Alison"})

    @app.route("/langs")
    def langs():
        languages = ["Python", "Bash", "Lua", "Rust"]
        return render_template(
            "index.html", title="Melhores linguagens", linguagens=languages
        )

