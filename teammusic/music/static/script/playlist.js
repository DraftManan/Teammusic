const optionsButton = document.getElementById('optionsButton');
const optionsMenu = document.getElementById('optionsMenu');
const optionsContainer = document.getElementById('optionsContainer');

// Show or hide menu on button click
optionsButton.addEventListener('click', (event) => {
    event.stopPropagation(); // Prevent click from reaching the document
    optionsMenu.classList.toggle('hidden');
});

// Close menu when clicking outside of it
document.addEventListener('click', (event) => {
    const isClickInside = optionsContainer.contains(event.target);
    if (!isClickInside) {
        optionsMenu.classList.add('hidden');
    }
});

// Keep menu open when hovering over it or the button
optionsContainer.addEventListener('mouseenter', () => {
    optionsMenu.classList.remove('hidden');
});


function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById('imagePreview');
    const uploadIcon = document.getElementById('uploadIcon');

    if (input.files && input.files[0]) {
      const reader = new FileReader();
      
      reader.onload = function(e) {
        preview.src = e.target.result;
        preview.classList.remove('hidden');  // แสดงภาพตัวอย่าง
        uploadIcon.classList.add('hidden');  // ซ่อนไอคอน SVG
      };
      
      reader.readAsDataURL(input.files[0]);
    }
  }


function openModal() {
    document.getElementById("songModal").classList.remove("hidden");
}

// ฟังก์ชันปิดโมดาล
function closeModal() {
    document.getElementById("songModal").classList.add("hidden");
}

function filterSongs() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const songs = document.querySelectorAll('.song-item');

    songs.forEach(song => {
        const titleElement = song.querySelector('.song-title');
        
        // ตรวจสอบว่า titleElement ไม่ใช่ null
        if (titleElement) {
            const title = titleElement.textContent.toLowerCase();
            song.style.display = title.includes(searchTerm) ? 'flex' : 'none';
        }
    });
}

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

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert("Link copied to clipboard!");
    }, function(err) {
        console.error("Could not copy text: ", err);
    });
}

