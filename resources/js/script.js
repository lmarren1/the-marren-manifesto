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
    // Update start of week if element exists
    const latestPostElement = document.getElementById('latest-post');
    if (latestPostElement) {
        const startOfWeek = getStartOfMostRecentWeek();
        latestPostElement.textContent = startOfWeek;
    }

    // Update copyright year
    const copyrightYearElement = document.getElementById('copyright-year');
    if (copyrightYearElement) {
        const copyrightYear = getCurrentYear();
        copyrightYearElement.textContent = copyrightYear;
    }
});