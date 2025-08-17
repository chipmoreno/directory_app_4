class PropertyListing {
    constructor(property) {
        this.property = property;
    }

    render() {
        const card = document.createElement('div');
        card.className = 'bg-white rounded-lg shadow-md overflow-hidden listing-card';

        // Image
        const img = document.createElement('img');
        img.src = this.property.image;
        img.alt = this.property.address;
        img.className = 'w-full h-48 object-cover';
        card.appendChild(img);

        const contentDiv = document.createElement('div');
        contentDiv.className = 'p-4';

        // Title/Link (Address)
        const titleLink = document.createElement('a');
        titleLink.href = '#'; // Placeholder link
        titleLink.className = 'block text-xl font-bold text-gray-800 hover:text-blue-600 mb-2';
        titleLink.textContent = this.property.address;
        contentDiv.appendChild(titleLink);

        // Price
        const priceBold = document.createElement('b');
        priceBold.className = 'text-2xl text-green-600 mb-2 block';
        priceBold.textContent = `$${this.property.price.toLocaleString()}`;
        contentDiv.appendChild(priceBold);

        // Beds and Baths
        const bedsBathsDiv = document.createElement('div');
        bedsBathsDiv.className = 'text-gray-600 text-sm mb-2';
        bedsBathsDiv.textContent = `${this.property.beds} Beds | ${this.property.baths} Baths | ${this.property.sqft} sqft`;
        contentDiv.appendChild(bedsBathsDiv);

        // Truncated Description
        const descriptionP = document.createElement('p');
        descriptionP.className = 'text-gray-700 text-base mb-4';
        descriptionP.textContent = this.property.description.substring(0, 130) + (this.property.description.length > 130 ? '...' : '');
        contentDiv.appendChild(descriptionP);

        // Buttons
        const buttonContainer = document.createElement('div');
        buttonContainer.className = 'flex space-x-2';

        const callButton = document.createElement('button');
        callButton.className = 'bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded';
        callButton.textContent = 'Call';
        buttonContainer.appendChild(callButton);

        const messageButton = document.createElement('button');
        messageButton.className = 'bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded';
        messageButton.textContent = 'Send Message';
        buttonContainer.appendChild(messageButton);

        export class PropertyListing {
    constructor(property) {
        this.property = property;
    }

    render() {
        const card = document.createElement('div');
        card.className = 'bg-white rounded-lg shadow-md overflow-hidden listing-card';

        // Image
        const img = document.createElement('img');
        img.src = this.property.image;
        img.alt = this.property.address;
        img.className = 'w-full h-48 object-cover';
        card.appendChild(img);

        const contentDiv = document.createElement('div');
        contentDiv.className = 'p-4';

        // Title/Link (Address)
        const titleLink = document.createElement('a');
        titleLink.href = '#'; // Placeholder link
        titleLink.className = 'block text-xl font-bold text-gray-800 hover:text-blue-600 mb-2';
        titleLink.textContent = this.property.address;
        contentDiv.appendChild(titleLink);

        // Price
        const priceBold = document.createElement('b');
        priceBold.className = 'text-2xl text-green-600 mb-2 block';
        priceBold.textContent = `${this.property.price.toLocaleString()}`;
        contentDiv.appendChild(priceBold);

        // Beds and Baths
        const bedsBathsDiv = document.createElement('div');
        bedsBathsDiv.className = 'text-gray-600 text-sm mb-2';
        bedsBathsDiv.textContent = `${this.property.beds} Beds | ${this.property.baths} Baths | ${this.property.sqft} sqft`;
        contentDiv.appendChild(bedsBathsDiv);

        // Truncated Description
        const descriptionP = document.createElement('p');
        descriptionP.className = 'text-gray-700 text-base mb-4';
        descriptionP.textContent = this.property.description.substring(0, 130) + (this.property.description.length > 130 ? '...' : '');
        contentDiv.appendChild(descriptionP);

        // Buttons
        const buttonContainer = document.createElement('div');
        buttonContainer.className = 'flex space-x-2';

        const callButton = document.createElement('button');
        callButton.className = 'bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded';
        callButton.textContent = 'Call';
        buttonContainer.appendChild(callButton);

        const messageButton = document.createElement('button');
        messageButton.className = 'bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded';
        messageButton.textContent = 'Send Message';
        buttonContainer.appendChild(messageButton);

        const bookmarkButton = document.createElement('button');
        bookmarkButton.className = 'bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded';
        bookmarkButton.textContent = 'Bookmark';
        buttonContainer.appendChild(bookmark);

        contentDiv.appendChild(buttonContainer);
        card.appendChild(contentDiv);

        return card;
    }
}


        contentDiv.appendChild(buttonContainer);
        card.appendChild(contentDiv);

        return card;
    }
}
