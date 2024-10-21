from flask import Flask, request, jsonify
import subprocess
import psutil
import time

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

    # Jalankan kode dan hitung waktu eksekusi
    try:
        result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        # Hitung waktu eksekusi dan sumber daya yang digunakan
        exec_time = time.time() - start_time
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Kirim hasil eksekusi dan informasi sumber daya ke frontend
    return jsonify({
        'output': output,
        'exec_time': exec_time,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'error': error
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
