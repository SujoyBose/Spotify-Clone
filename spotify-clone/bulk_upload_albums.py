import requests
import os
from time import sleep

base_url = "http://localhost:4000"

albums_data = [
    {
        "name": "Top 50 Global",
        "desc": "Your weekly update of the most played tracks",
        "bgColour": "#2a4365",
        "image_path": "./src/assets/img8.jpg"
    },
    {
        "name": "Top 50 India",
        "desc": "Your weekly update of the most played tracks",
        "bgColour": "#22543d",
        "image_path": "./src/assets/img9.jpg"
    },
    {
        "name": "Trending India",
        "desc": "Your weekly update of the most played tracks",
        "bgColour": "#742a2a",
        "image_path": "./src/assets/img10.jpg"
    },
    {
        "name": "Trending Global",
        "desc": "Your weekly update of the most played tracks",
        "bgColour": "#44337a",
        "image_path": "./src/assets/img16.jpg"
    },
    {
        "name": "Mega Hits",
        "desc": "Your weekly update of the most played tracks",
        "bgColour": "#234e52",
        "image_path": "./src/assets/img11.jpg"
    },
    {
        "name": "Happy Favorites",
        "desc": "Your weekly update of the most played tracks",
        "bgColour": "#744210",
        "image_path": "./src/assets/img15.jpg"
    }
]

def upload_albums():
    print("🚀 Starting bulk album upload...\n")
    
    for i, album in enumerate(albums_data):
        print(f"📀 Uploading {i + 1}/{len(albums_data)}: {album['name']}")
        
        try:
            # Check if file exists
            if not os.path.exists(album['image_path']):
                print(f"❌ Image not found: {album['image_path']}")
                continue
            
            # Prepare form data
            data = {
                'name': album['name'],
                'desc': album['desc'],
                'bgColour': album['bgColour']
            }
            
            files = {
                'image': open(album['image_path'], 'rb')
            }
            
            response = requests.post(
                f"{base_url}/api/album/add",
                data=data,
                files=files,
                timeout=30
            )
            
            files['image'].close()  # Close file handle
            
            result = response.json()
            
            if result.get('success'):
                print(f"✅ Successfully uploaded: {album['name']}")
            else:
                print(f"❌ Failed to upload {album['name']}: {result.get('message', 'Unknown error')}")
                
        except Exception as error:
            print(f"❌ Error uploading {album['name']}: {str(error)}")
        
        # Add delay between uploads
        if i < len(albums_data) - 1:
            sleep(1)  # 1 second delay
    
    print("\n🎉 Bulk upload completed!")

if __name__ == "__main__":
    upload_albums()
