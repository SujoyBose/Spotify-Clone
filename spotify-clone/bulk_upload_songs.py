import requests
import os
from time import sleep

base_url = "http://localhost:4000"

songs_data = [
    {
        "name": "Song One",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img1.jpg",
        "audio_path": "./src/assets/song1.mp3"
    },
    {
        "name": "Song Two",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img2.jpg",
        "audio_path": "./src/assets/song2.mp3"
    },
    {
        "name": "Song Three",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img3.jpg",
        "audio_path": "./src/assets/song3.mp3"
    },
    {
        "name": "Song Four",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img4.jpg",
        "audio_path": "./src/assets/song1.mp3"
    },
    {
        "name": "Song Five",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img5.jpg",
        "audio_path": "./src/assets/song2.mp3"
    },
    {
        "name": "Song Six",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img14.jpg",
        "audio_path": "./src/assets/song3.mp3"
    },
    {
        "name": "Song Seven",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img7.jpg",
        "audio_path": "./src/assets/song1.mp3"
    },
    {
        "name": "Song Eight",
        "desc": "Put a smile on your face with these happy tunes",
        "album": "none",
        "image_path": "./src/assets/img12.jpg",
        "audio_path": "./src/assets/song2.mp3"
    }
]

def upload_songs():
    print("🎵 Starting bulk song upload...\n")
    
    for i, song in enumerate(songs_data):
        print(f"🎵 Uploading {i + 1}/{len(songs_data)}: {song['name']}")
        
        try:
            # Check if files exist
            if not os.path.exists(song['image_path']):
                print(f"❌ Image not found: {song['image_path']}")
                continue
                
            if not os.path.exists(song['audio_path']):
                print(f"❌ Audio not found: {song['audio_path']}")
                continue
            
            # Prepare form data
            data = {
                'name': song['name'],
                'desc': song['desc'],
                'album': song['album']
            }
            
            files = {
                'image': ('image.jpg', open(song['image_path'], 'rb'), 'image/jpeg'),
                'audio': ('audio.mp3', open(song['audio_path'], 'rb'), 'audio/mpeg')
            }
            
            response = requests.post(
                f"{base_url}/api/song/add",
                data=data,
                files=files,
                timeout=60  # 60 second timeout for large audio files
            )
            
            # Close file handles
            files['image'][1].close()
            files['audio'][1].close()
            
            result = response.json()
            
            if result.get('success'):
                print(f"✅ Successfully uploaded: {song['name']}")
            else:
                print(f"❌ Failed to upload {song['name']}: {result.get('message', 'Unknown error')}")
                
        except Exception as error:
            print(f"❌ Error uploading {song['name']}: {str(error)}")
        
        # Add delay between uploads to avoid overwhelming server
        if i < len(songs_data) - 1:
            sleep(2)  # 2 second delay
    
    print("\n🎉 Bulk song upload completed!")

def check_files():
    """Check if all required files exist before starting upload"""
    print("🔍 Checking if all files exist...")
    missing_files = []
    
    for song in songs_data:
        if not os.path.exists(song['image_path']):
            missing_files.append(f"Image: {song['image_path']}")
        if not os.path.exists(song['audio_path']):
            missing_files.append(f"Audio: {song['audio_path']}")
    
    if missing_files:
        print("\n❌ Missing files found:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all files exist before running the upload.")
        return False
    else:
        print("✅ All files found!")
        return True

def test_server_connection():
    """Test if the server is running"""
    try:
        response = requests.get(f"{base_url}/api/album/list", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running and accessible")
            return True
        else:
            print(f"❌ Server responded with status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to server: {str(e)}")
        return False

if __name__ == "__main__":
    print("🎵 Song Bulk Upload Script")
    print("=" * 50)
    
    # Test server connection
    if not test_server_connection():
        print("\nMake sure your backend server is running on http://localhost:5000")
        exit(1)
    
    # Check if files exist
    if not check_files():
        exit(1)
    
    # Confirm before starting
    confirm = input("\nDo you want to start the bulk upload? (y/N): ")
    if confirm.lower() in ['y', 'yes']:
        upload_songs()
    else:
        print("Upload cancelled.")
