# Image Resizer

This Python Project allows you to select an image file, resize it to 100x100 pixels, and save it as `Img.jpeg`. The script uses the `PIL` library from `Pillow` and the `tkinter` library to open a file dialog for selecting the image.

## Requirements

- Python 3.x
- Pillow library

You can install the Pillow library using pip:

```bash
pip install Pillow
```

## Usage

1. **Clone the Repository or Download the Script**

   Clone this repository to your local machine or download the script file.

2. **Run the Script**

   Open a terminal or command prompt and navigate to the directory containing the script. Run the script using Python:

   ```bash
   python main.py
   ```

3. **Select an Image File**

   A file dialog will open, allowing you to select an image file from your computer.

4. **Image Resizing and Saving**

   The selected image will be resized to 100x100 pixels and saved as `Img.jpeg` in the same directory as the script.


## Notes

- Ensure you have the required dependencies installed.
- The script will only work with image files supported by the Pillow library.
- If no file is selected, the script will print "No file selected" and exit.


## Acknowledgements

- [Pillow Library](https://python-pillow.org/)
- [Tkinter Library](https://docs.python.org/3/library/tkinter.html)
