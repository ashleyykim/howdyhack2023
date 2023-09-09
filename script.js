const musicFiles = [
    { title: 'Blame It on the Boogie', url: 'playlist_audio/Blame It on the Boogie.mp3' },
    { title: 'Dancing Queen', url: 'playlist_audio/Dancing Queen.mp3' },
    { title: 'Heaven Is A Place On Earth', url: 'playlist_audio/Heaven Is A Place On Earth - Promo 7 Edit.mp3' }
];
let currentSongIndex = 0;

const audioElement = document.getElementById('musicPlayer');
const prevButton = document.getElementById('prevBtn');
const nextButton = document.getElementById('nextBtn');
const songTitleElement = document.getElementById('songTitle');

// Function to load and play the current song
function playCurrentSong() {
    const currentSong = musicFiles[currentSongIndex];
    audioElement.src = currentSong.url;
    audioElement.load();
    audioElement.play();
    songTitleElement.textContent = currentSong.title; // Update song title
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

// Update the song title while the song is playing
audioElement.addEventListener('timeupdate', () => {
    // Check if audio is playing and has a duration
    if (!audioElement.paused && audioElement.duration) {
        songTitleElement.textContent = musicFiles[currentSongIndex].title;
    }
});

// Play the first song when the page loads
playCurrentSong();