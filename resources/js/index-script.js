function getCurrentYear() {
    const now = new Date();
    return now.getFullYear();
}

function getStartOfMostRecentWeek() {
    const now = new Date();
    const dayOfWeek = now.getDay();
    const startOfWeek = new Date(now);

    // If today is Sunday, set the start of the week to today
    if (dayOfWeek === 0) {
        startOfWeek.setDate(now.getDate());
    } else {
        // Calculate Sunday of the current week
        startOfWeek.setDate(now.getDate() - (dayOfWeek - 1));
    }

    return formatDate(startOfWeek);
}

// Formats date in mm/dd/yyyy
function formatDate(date) {
    const day = String(date.getDate());
    const month = String(date.getMonth() + 1);
    const year = date.getFullYear();

    return `${month}/${day}/${year}`;
}

// Update HTML
document.addEventListener('DOMContentLoaded', function() {
    const startOfWeek = getStartOfMostRecentWeek();
    document.getElementById('latest-post').textContent = startOfWeek;
    const copyrightYear = getCurrentYear();
    document.getElementById('copyright-year').textContent = copyrightYear;
});