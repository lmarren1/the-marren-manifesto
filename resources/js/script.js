function getCurrentYear() {
    const now = new Date();
    return now.getFullYear();
}

function getStartOfMostRecentWeek() {
    const now = new Date();
    const dayOfWeek = now.getDay();
    const startOfWeek = new Date(now);

    // Calculate the difference from Sunday
    const daysToSubtract = dayOfWeek; // 0 for Sunday, 1 for Monday, etc.
    
    // Set the date to the most recent Sunday
    startOfWeek.setDate(now.getDate() - daysToSubtract);
    
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