from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
VALID_USERNAME = "e23cseu0435"
VALID_PASSWORD = "Ravioli@0099"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('login'))


# ✅ NEW: Route for the CSET109 documents page
@app.route('/cset109')
def cset109():
    return render_template('cset109.html')

@app.route('/cset109/tutorials')
def cset109_tutorials():
    return render_template('cset109_tutorials.html', tutorial_count=14)

@app.route('/uploads/cset109/tutorials/<filename>')
def download_cset109_tutorial(filename):
    tutorial_path = os.path.join(UPLOAD_FOLDER, 'cset109', 'tutorials')
    return send_from_directory(tutorial_path, filename, as_attachment=True)

@app.route('/cset109/ppts')
def cset109_ppts():
    print("✅ Entered /cset109/ppts route")
    return render_template('cset109_ppts.html', ppt_count=13)

@app.route('/uploads/cset109/ppts/<filename>')
def download_cset109_ppt(filename):
    ppt_path = os.path.join(UPLOAD_FOLDER, 'cset109', 'ppts')
    return send_from_directory(ppt_path, filename, as_attachment=True)

@app.route('/cset102')
def cset102():
    return render_template('cset102.html')

@app.route('/cset102/pdfs')
def cset102_pdfs():
    print("✅ Entered /cset102/pdfs route")
    return render_template('cset102_pdfs.html', pdf_count=12)

@app.route('/uploads/cset102/ppts/<filename>')
def download_cset102_pdf(filename):
    pdf_path = os.path.join(UPLOAD_FOLDER, 'cset102', 'pdfs')
    return send_from_directory(pdf_path, filename, as_attachment=True)

@app.route('/cset102/tutorials')
def cset102_tutorials():
    return render_template('cset102_tutorials.html', tutorial_count=10)

@app.route('/uploads/cset102/tutorials/<filename>')
def download_cset102_tutorial(filename):
    tutorial_path = os.path.join(UPLOAD_FOLDER, 'cset102', 'tutorials')
    return send_from_directory(tutorial_path, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
