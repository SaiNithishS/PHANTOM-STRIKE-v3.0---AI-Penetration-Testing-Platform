from flask import Flask, request, jsonify
from flask_cors import CORS
import zipfile
import json
import io
from azure.identity import AzureCliCredential
from azure.ai.projects import AIProjectClient

app = Flask(__name__)
CORS(app)

ENDPOINT = " " #enter your project endpoint
AGENT1_NAME = "" #enter agent1 name eg:consultant
AGENT2_NAME = "" #enter agent1 name eg:remediation

def parse_json(text):
    try:
        return json.loads(text)
    except:
        s = text.find('{')
        e = text.rfind('}')
        if s > -1 and e > s:
            try:
                return json.loads(text[s:e+1])
            except:
                pass
    return {"raw_text": text}

def extract_zip(zip_bytes):
    file_text = ""
    skip = [
        'node_modules', '.git',
        '.min.js', 'package-lock',
        '.png', '.jpg', '.gif',
        '.ico', '.woff', '.ttf'
    ]
    priority = [
        'auth', 'login', 'password',
        'api', 'route', 'controller',
        'db', 'database', 'query',
        'config', 'setting', 'env',
        'app', 'main', 'index', 'server'
    ]
    with zipfile.ZipFile(
            io.BytesIO(zip_bytes)) as zf:
        files = []
        for name in zf.namelist():
            if zf.getinfo(name).is_dir():
                continue
            if any(s in name.lower()
                   for s in skip):
                continue
            pri = next(
                (i for i, p in
                 enumerate(priority)
                 if p in name.lower()),
                99
            )
            files.append((pri, name))
        files.sort(key=lambda x: x[0])
        for _, name in files:
            if len(file_text) > 20000:
                break
            try:
                content = zf.read(
                    name).decode(
                    'utf-8', errors='ignore')
                chunk = content[:2000]
                file_text += (
                    f"\n\n### {name}\n{chunk}")
            except:
                pass
    return file_text

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})

@app.route('/analyse', methods=['POST'])
def analyse():
    try:
        zip_file = request.files.get('file')
        if not zip_file:
            return jsonify({
                'error': 'No file uploaded'
            }), 400

        filename = zip_file.filename
        print(f"\n[SERVER] Analysing: {filename}")

        print("[SERVER] Extracting ZIP...")
        zip_bytes = zip_file.read()
        file_text = extract_zip(zip_bytes)
        print(f"[SERVER] {len(file_text)} chars")

        print("[SERVER] Connecting to Foundry...")
        credential = AzureCliCredential()
        project_client = AIProjectClient(
            endpoint=ENDPOINT,
            credential=credential
        )
        openai_client = \
            project_client.get_openai_client()
        print("[SERVER] Connected!")

        print("[SERVER] Running Agent 1...")
        r1 = openai_client.responses.create(
            input=[{
                "role": "user",
                "content": (
                    "Analyse this code and "
                    "return findings as JSON "
                    "only. No markdown. "
                    "No explanation.\n\n"
                    + file_text
                )
            }],
            extra_body={
                "agent_reference": {
                    "name": AGENT1_NAME,
                    "type": "agent_reference"
                }
            }
        )
        reply1 = r1.output_text
        result1 = parse_json(reply1)
        n = result1.get(
            "executive_summary", {}
        ).get("total_findings", 0)
        print(f"[SERVER] Findings: {n}")

        print("[SERVER] Running Agent 2...")
        r2 = openai_client.responses.create(
            input=[{
                "role": "user",
                "content": (
                    "Generate fix plans for "
                    "these findings as JSON "
                    "only. No markdown. "
                    "No explanation.\n\n"
                    + reply1
                )
            }],
            extra_body={
                "agent_reference": {
                    "name": AGENT2_NAME,
                    "type": "agent_reference"
                }
            }
        )
        reply2 = r2.output_text
        result2 = parse_json(reply2)
        print("[SERVER] COMPLETE")

        return jsonify({
            "pentest": result1,
            "remediation": result2,
            "target": filename
        })

    except Exception as e:
        print(f"[SERVER] ERROR: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("PHANTOM STRIKE BACKEND")
    print("Running at http://localhost:5001")
    print("Make sure az login is done")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5001,
            debug=False)
