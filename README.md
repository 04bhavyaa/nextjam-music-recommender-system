## NextJam: Music Recommender System

This project involves creating a website that offers personalized song recommendations based on user inputs, such as their current mood or responses to a simple genre-exploration survey. The system integrates machine learning for personalized recommendations and utilizes the Spotify API to fetch song details like artist, album, and song previews.

### High-Level Workflow

1. User Interaction:
   - Users visit the website and either:
   - Select their current mood (e.g., happy, relaxed, energetic).
   - Complete a short survey about their music preferences and genre interests.
   - Based on their input, the backend will process the data and provide top 10 song recommendations.
2. Machine Learning Component:
   - The system will have a recommendation engine that matches user input with songs that fit the chosen mood or genre profile.
   - The system can use either a simple content-based filtering approach (matching music features like tempo, genre) or a collaborative filtering model based on existing user data.
3. Spotify Integration:
   - The backend will use the Spotify API to fetch song details like artist name, album cover, and song previews.
   - These details will be displayed to the user as part of the recommendations.
4. Frontend:
   - The frontend will present the user interface (UI) where users can input their preferences.
   - After submission, the UI will display the top 10 recommended songs, complete with album artwork, artist names, and preview links to listen to the songs.
