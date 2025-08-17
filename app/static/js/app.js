import { properties } from './data.js';
import { PropertyListing } from './listing_module.js';

document.addEventListener('DOMContentLoaded', () => {
    const listingsGrid = document.querySelector('.property-listings'); // Use the existing .property-listings container

    if (listingsGrid) {
        // Clear existing content if any
        listingsGrid.innerHTML = '';

        // Create a div for the grid itself
        const gridContainer = document.createElement('div');
        gridContainer.className = 'listings-grid';

        properties.forEach(property => {
            const listing = new PropertyListing(property);
            gridContainer.appendChild(listing.render());
        });

        listingsGrid.appendChild(gridContainer);
    } else {
        console.error('Listings grid container not found.');
    }
});
