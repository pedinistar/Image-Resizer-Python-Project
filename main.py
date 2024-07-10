import PIL
from PIL import Image
from tkinter.filedialog import askopenfilename

# Open a file dialog to select an image file
file_path = askopenfilename(title="Select an image file")

# Check if a file was selected
if file_path:
    try:
        # Open the selected image file
        img = PIL.Image.open(file_path)
        
        # Get the original dimensions of the image
        width, height = img.size
        
        # Resize the image to 100x100 pixels using the LANCZOS filter
        img = img.resize((100, 100), PIL.Image.LANCZOS)
        
        # Save the resized image as 'Img.jpeg'
        img.save('Img.jpeg')
        
        print("Image resized and saved as 'Img.jpeg'")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No file selected.")
