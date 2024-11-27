
function removeSong(playlistId, songId) {
    fetch(`/teammusic/playlist/${playlistId}/remove_song/${songId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  // ใช้ CSRF token เพื่อความปลอดภัย
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.reload()
        } else {
            alert(data.message);  // แสดงข้อความผิดพลาด
        }
    })
    .catch(error => console.error('Error:', error));
}