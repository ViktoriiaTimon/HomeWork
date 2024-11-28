import requests

# POST image

url = "http://127.0.0.1:8080"

upload_url = f'{url}/upload'
image_url = 'https://img.freepik.com/free-psd/macaroon-isolated-transparent-background_191095-35017.jpg'

new_image = requests.get(image_url)
if new_image.status_code == 200:
    with open("new_image.jpg", "wb") as image:
        image.write(new_image.content)

    with open('new_image.jpg', "rb") as image:
        files = {"image": image}
        post_response = requests.post(upload_url, files=files)

    if post_response.status_code == 201:
        image_url = post_response.json().get("image_url")
        print('The image is uploaded successfully', post_response.json().get("image_url"))

# Get uploaded image

image_url = 'http://127.0.0.1:8080/uploads/new_image.jpg'

get_uploaded_image = requests.get('http://127.0.0.1:8080/uploads/new_image.jpg')
if get_uploaded_image.status_code == 200:
    with open('new_image.jpg', 'wb') as test_image:
        test_image.write(get_uploaded_image.content)
        print('File is here')
print(get_uploaded_image.json())

# DELETE image
url = 'http://127.0.0.1:8080/uploads/new_image.jpg'
response = requests.delete(url)

if response.status_code == 200:
    print('File is deleted')
else:
    print('Error while deletion')