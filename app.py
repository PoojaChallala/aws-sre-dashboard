from flask import Flask, render_template, g
import time

app = Flask(__name__)

request_count = 0
response_time = 0
error_count = 0
start_time = time.time()

@app.before_request
def count_requests():
    global request_count

    request_count += 1
    g.start_time = time.perf_counter()

@app.after_request
def after_request(response):
    global response_time
    global error_count

    elapsed_time = time.perf_counter() - g.start_time
    response_time = elapsed_time * 1000

    if response.status_code >= 400:
        error_count += 1

    response.headers["X-Process-Time"] = f"{response_time:.2f}"

    return response

@app.route("/")
def home():
    if request_count > 0:
        error_rate = (error_count / request_count) * 100
    else:
        error_rate = 0

    uptime = time.time() - start_time

    return render_template(
        "index.html",
        request_count=request_count,
        response_time=round(response_time, 2),
        error_rate=round(error_rate, 2),
        uptime=round(uptime, 2)
    )

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/test-error")
def test_error():
    return "Something went wrong!", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)