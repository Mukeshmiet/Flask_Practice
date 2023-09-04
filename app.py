from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import datetime
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Set the upload folder path
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('camera.html')

@app.route('/capture', methods=['POST'])
def capture():
    image_data_url = request.form.get('image')
    if image_data_url:
        # Decode the base64 data URL to obtain the image data
        image_data = base64.b64decode(image_data_url.split(',')[1])

        # Create an image from the decoded data
        img = Image.open(BytesIO(image_data))

        # Generate a filename with the current date and time
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        filename = f"img_{timestamp}.png"  # Change file extension to 'png'

        # Save the image in PNG format
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(file_path, 'PNG')

        return redirect(url_for('index'))

@app.route('/uploaded_images/<filename>')
def view_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
