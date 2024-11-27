document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        const messageBox = document.getElementById('message-box');
        if (messageBox) {
            messageBox.style.opacity = '0';
            setTimeout(() => { messageBox.style.display = 'none'; }, 1000); // Hide after fade out
        }
    }, 3000); // 5 วินาที
});