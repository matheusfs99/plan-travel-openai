from services.travel import Travel
from flask import Flask, request

app = Flask(__name__)


@app.route("/plan", methods=["POST"])
def plan_travel():
    data = request.get_json(force=True)
    travel = Travel(
        start_date=data["start_date"],
        end_date=data["end_date"],
        destination=data["destination"]
    )
    return travel.plan()


if __name__ == "__main__":
    app.run()
