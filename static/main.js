const header = document.querySelector('.sticky-header');

// Get the offset position of the header
const sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function stickyHeader() {
    if (window.pageYOffset > sticky) {
        header.classList.add('sticky');
    } else {
        header.classList.remove('sticky');
    }
}

// When the user scrolls the page, execute stickyHeader
window.onscroll = function() {
    stickyHeader();
};