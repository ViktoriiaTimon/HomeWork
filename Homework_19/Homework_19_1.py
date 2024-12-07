import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    photos = response.json().get("photos", [])

    for index, photo in enumerate(photos[:2]):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content

        filename = f"mars_photo{index + 1}.jpg"
        with open(filename, "wb") as f:
            f.write(img_data)

        print(f'Photo was saved successfully {filename}')

print(response.json())