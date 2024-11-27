let audio = null;
let isPlaying = false;
let currentSongIndex = 0;



function playSong(title, album, albumCover, singer, songUrl) {
    // ส่งข้อมูลเพลงไปเก็บใน session
    fetch("/teammusic/set_song_session/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({
            'title': title,
            'album': album,
            'albumCover': albumCover,
            'singer': singer,
            'songUrl': songUrl
        })
    }).then(response => {
        if (response.ok) {
            console.log("Song data added to session");
            openPlayer(title, album, albumCover, singer, songUrl);
        } else {
            console.error("Failed to set song in session");
        }
    });
}

function openPlayer(title, album, albumCover, singer, songUrl) {
    document.getElementById("playerSongTitle").textContent = title;
    document.getElementById("playerAlbumInfo").textContent = `${singer} - ${album}`;
    document.getElementById("playerAlbumCover").src = albumCover;

    if (audio) {
        audio.pause();
    }
    audio = new Audio(songUrl);
    audio.play();
    isPlaying = true;

    document.getElementById("playerControl").classList.remove("hidden");
    updatePlayPauseIcon();
}

function togglePlayPause() {
    if (audio) {
        if (isPlaying) {
            audio.pause();
        } else {
            audio.play();
        }
        isPlaying = !isPlaying;
        updatePlayPauseIcon();
    }
}

function updatePlayPauseIcon() {
    const playPauseButton = document.getElementById("playPauseButton");
    const playIcon = `
        <svg class="h-8 w-8 text-white" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="5 3 19 12 5 21 5 3" />
        </svg>
    `;
    const pauseIcon = `
        <svg class="h-8 w-8 text-white" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="6" y="4" width="4" height="16"></rect>
            <rect x="14" y="4" width="4" height="16"></rect>
        </svg>
    `;
    playPauseButton.innerHTML = isPlaying ? pauseIcon : playIcon;
}

function previousSong() {
    currentSongIndex = (currentSongIndex - 1 + songList.length) % songList.length;
    const song = songList[currentSongIndex];
    playSong(song.title, song.album, song.albumCover, song.singer, song.songUrl);
}

function nextSong() {
    currentSongIndex = (currentSongIndex + 1) % songList.length;
    const song = songList[currentSongIndex];
    playSong(song.title, song.album, song.albumCover, song.singer, song.songUrl);
}

// เมื่อหน้าโหลด ให้ดึงข้อมูลเพลงจาก session เพื่อเริ่มต้น player
window.onload = function() {
    fetch("/teammusic/get_song_session/")
        .then(response => response.json())
        .then(data => {
            if (data && !data.error) {
                // หากมีข้อมูลเพลงใน session ให้นำมาเล่น
                playSong(data.title, data.album, data.albumCover, data.singer, data.songUrl);
            }
        })
        .catch(error => console.error("Error loading song from session:", error));
};

function filterSongsMain() {
    const searchTerm = document.getElementById('searchInputMain').value.toLowerCase();
    const songs = document.querySelectorAll('.song-item');

    songs.forEach(song => {
        const titleElement = song.querySelector('.song');
        
        // ตรวจสอบว่า titleElement ไม่ใช่ null
        if (titleElement) {
            const title = titleElement.textContent.toLowerCase();
            song.style.display = title.includes(searchTerm) ? 'flex' : 'none';
        }
    });
}
