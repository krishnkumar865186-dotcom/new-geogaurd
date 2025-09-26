from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML template (inline for demo)
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GeoGuard Compliance Checker</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }
        .container { max-width: 700px; margin: auto; background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
        h1 { text-align: center; color: #2c3e50; }
        textarea, input { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #ccc; }
        button { background: #3498db; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #2980b9; }
        .result { margin-top: 20px; padding: 15px; border-radius: 5px; background: #ecf0f1; }
    </style>
</head>
<body>
    <div class="container">
        <h1>GeoGuard Compliance Checker</h1>
        <form method="POST">
            <label>Feature Title:</label>
            <input type="text" name="title" required>
            
            <label>Description:</label>
            <textarea name="description" required></textarea>
            
            <label>PRD:</label>
            <textarea name="prd" required></textarea>
            
            <label>TRD:</label>
            <textarea name="trd" required></textarea>
            
            <button type="submit">Run Compliance Check</button>
        </form>

        {% if result %}
        <div class="result">
            <h3>Compliance Report:</h3>
            <p><strong>Status:</strong> {{ result['status'] }}</p>
            <p><strong>Issues Found:</strong></p>
            <ul>
                {% for issue in result['issues'] %}
                <li>{{ issue }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

def fake_compliance_check(title, description, prd, trd):
    """Dummy function to simulate compliance analysis"""
    issues = []
    if "location" in description.lower():
        issues.append("Potential location tracking concern.")
    if "data" in prd.lower():
        issues.append("Check for user data compliance (GDPR/CCPA).")
    if not issues:
        return {"status": "Compliant ✅", "issues": ["No major issues found."]}
    else:
        return {"status": "Review Needed ⚠️", "issues": issues}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        prd = request.form.get("prd")
        trd = request.form.get("trd")
        result = fake_compliance_check(title, description, prd, trd)
    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
