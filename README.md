# Spotify Clone

This is a **Full Stack Spotify Clone Application** built using the **MERN Stack** (MongoDB, Express.js, React.js, Node.js). It allows users to stream music, view albums, and offers an admin panel to manage albums and songs.

## Features

### Admin Page
- **Create Albums**: Admin can create albums and manage album details.
- **Add Songs**: Admin can add songs to specific albums.
- **Remove Songs**: Admin can remove songs from the albums.
- **Album Management**: Admin has full control over albums and song lists.

### Frontend Application
- **View Albums**: Users can view a list of albums created on the platform.
- **Stream Music**: Users can listen to songs from the albums directly.
- **Responsive UI**: Built using React, ensuring an interactive and smooth experience across devices.

## Technologies Used
- **Frontend**: React.js
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Audio Streaming**: Custom integration for music streaming.

## Installation & Setup

### Prerequisites
Make sure you have the following installed:
- **Node.js** (v14 or higher)
- **npm** (Node Package Manager)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/spotify-clone.git
   cd spotify-clone
   ```

2. **Install Backend Dependencies**

   Navigate to the backend directory and install the required dependencies:

   ```bash
   cd spotify-backend
   npm install
   ```

3. **Install Frontend Dependencies**

   Navigate to the frontend directory and install the required dependencies:

   ```bash
   cd ../spotify-frontend
   npm install
   ```

4. **Start the Backend Server**

   After setting up the backend dependencies and `.env` file, navigate to the `spotify-backend` folder and start the server:

   ```bash
   cd spotify-backend
   npm run server
   ```

   This will start the backend server. By default, the backend server should be running at [http://localhost:5000](http://localhost:5000).

5. **Start the Frontend Application**

   After setting up the frontend dependencies, navigate to the `spotify-frontend` folder and run the React application:

   ```bash
   cd ../spotify-frontend
   npm dev
   ```

   This will start the React app. By default, the frontend application should be running at [http://localhost:3000](http://localhost:3000).
