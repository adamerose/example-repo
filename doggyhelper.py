import requests

def identify_breed(image_path):
        
    # Define the URL of the API endpoint
    url = 'http://doggyhelper.com/api/upload'

    # Open the file in binary mode
    with open(image_path, 'rb') as f:
        # Define the files parameter for the POST request
        # This includes the name the server expects for the file, the file object, and the content type
        files = {'file': ('image.jpg', f, 'image/jpeg')}

        # Send the POST request
        response = requests.post(url, files=files)

    # Print the response from the server
    print(response.text)
