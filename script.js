const musicFiles = [
    'playlist_audio/Blame It on the Boogie.mp3',
    'playlist_audio/Dancing Queen.mp3',
    'playlist_audio/Heaven Is A Place On Earth - Promo 7 Edit.mp3',
    'playlist_audio/I Will Survive - Remastered.mp3'
];
let currentSongIndex = 0;

const audioElement = document.getElementById('musicPlayer');
const prevButton = document.getElementById('prevBtn');
const nextButton = document.getElementById('nextBtn');

// Function to load and play the current song
function playCurrentSong() {
    audioElement.src = musicFiles[currentSongIndex];
    audioElement.load();
    audioElement.play();
}

// Event listener for the "Next" button
nextButton.addEventListener('click', () => {
    currentSongIndex = (currentSongIndex + 1) % musicFiles.length;
    playCurrentSong();
});

// Event listener for the "Previous" button
prevButton.addEventListener('click', () => {
    currentSongIndex = (currentSongIndex - 1 + musicFiles.length) % musicFiles.length;
    playCurrentSong();
});

// Play the first song when the page loads
playCurrentSong();