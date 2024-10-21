from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code')

    # Simpan kode di file sementara
    with open('temp_code.py', 'w') as f:
        f.write(code)

    # Jalankan kode menggunakan subprocess
    try:
        result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    if error:
        return jsonify({'output': output, 'error': error}), 400
    else:
        return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
