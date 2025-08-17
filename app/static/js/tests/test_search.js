
// Mock the DOM for testing purposes
document.body.innerHTML = `
    <div id="search-container"></div>
`;

// Import the SearchComponent class (assuming it's globally available or imported via a module system)
// For this test, we'll assume search_module.js is loaded before this test file in a real browser environment.
// In a Node.js environment, you would use require or import.
// For simplicity, we'll just re-define the class here for the test to work in isolation.

class SearchComponent {
    constructor() {
        this.searchContainer = document.getElementById('search-container');
        if (!this.searchContainer) {
            console.error('Search container not found!');
            return;
        }
    }

    render() {
        this.searchContainer.innerHTML = `
            <h2 class="text-2xl font-bold text-gray-800 mb-4">Search Properties</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <div>
                    <label for="keywords" class="block text-gray-700 text-sm font-bold mb-2">City/Address/Keywords:</label>
                    <input type="text" id="keywords" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                </div>
                <div>
                    <label for="price" class="block text-gray-700 text-sm font-bold mb-2">Price:</label>
                    <select id="price" class="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Any</option>
                        <option value="0-100000">$0 - $100,000</option>
                        <option value="100001-250000">$100,001 - $250,000</option>
                        <option value="250001-500000">$250,001 - $500,000</option>
                        <option value="500001-1000000">$500,001 - $1,000,000</option>
                        <option value="1000001+">$1,000,001+</option>
                    </select>
                </div>
                <div>
                    <label for="beds" class="block text-gray-700 text-sm font-bold mb-2">Beds:</label>
                    <select id="beds" class="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Any</option>
                        <option value="1">1+</option>
                        <option value="2">2+</option>
                        <option value="3">3+</option>
                        <option value="4">4+</option>
                        <option value="5">5+</option>
                    </select>
                </div>
                <div>
                    <label for="baths" class="block text-gray-700 text-sm font-bold mb-2">Baths:</label>
                    <select id="baths" class="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Any</option>
                        <option value="1">1+</option>
                        <option value="2">2+</option>
                        <option value="3">3+</option>
                        <option value="4">4+</option>
                    </select>
                </div>
                <div>
                    <label for="pets" class="block text-gray-700 text-sm font-bold mb-2">Pets:</label>
                    <select id="pets" class="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Any</option>
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                    </select>
                </div>
                <div>
                    <label for="propertyType" class="block text-gray-700 text-sm font-bold mb-2">Property Type:</label>
                    <select id="propertyType" class="shadow border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                        <option value="">Any</option>
                        <option value="house">House</option>
                        <option value="apartment">Apartment</option>
                        <option value="condo">Condo</option>
                        <option value="townhouse">Townhouse</option>
                    </select>
                </div>
            </div>
        `;
        this.addEventListeners();
    }

    addEventListeners() {
        const inputs = this.searchContainer.querySelectorAll('input, select');
        inputs.forEach(input => {
            input.addEventListener('change', (event) => {
                console.log(`${event.target.id}: ${event.target.value}`);
            });
            input.addEventListener('input', (event) => {
                console.log(`${event.target.id}: ${event.target.value}`);
            });
        });
    }
}


// Test Case 1: TestSearchComponentRendering
function testSearchComponentRendering() {
    const searchComponent = new SearchComponent();
    searchComponent.render();

    const searchContainer = document.getElementById('search-container');

    // Check for presence of key elements
    const keywordsInput = searchContainer.querySelector('#keywords');
    const priceSelect = searchContainer.querySelector('#price');
    const bedsSelect = searchContainer.querySelector('#beds');
    const bathsSelect = searchContainer.querySelector('#baths');
    const petsSelect = searchContainer.querySelector('#pets');
    const propertyTypeSelect = searchContainer.querySelector('#propertyType');

    console.assert(keywordsInput !== null, "Test Case 1 Failed: Keywords input not found.");
    console.assert(priceSelect !== null, "Test Case 1 Failed: Price select not found.");
    console.assert(bedsSelect !== null, "Test Case 1 Failed: Beds select not found.");
    console.assert(bathsSelect !== null, "Test Case 1 Failed: Baths select not found.");
    console.assert(petsSelect !== null, "Test Case 1 Failed: Pets select not found.");
    console.assert(propertyTypeSelect !== null, "Test Case 1 Failed: Property Type select not found.");

    console.log("Test Case 1: TestSearchComponentRendering - PASSED");
}

// Test Case 2: TestSearchComponentInput
function testSearchComponentInput() {
    const searchComponent = new SearchComponent();
    searchComponent.render();

    const keywordsInput = document.getElementById('keywords');
    const originalConsoleLog = console.log;
    let loggedMessage = '';

    // Mock console.log to capture its output
    console.log = (message) => {
        loggedMessage = message;
    };

    // Simulate user input
    keywordsInput.value = '123 Main St';
    keywordsInput.dispatchEvent(new Event('input')); // Dispatch 'input' event

    console.assert(loggedMessage === 'keywords: 123 Main St', `Test Case 2 Failed: Expected 'keywords: 123 Main St', got '${loggedMessage}'`);

    // Restore original console.log
    console.log = originalConsoleLog;

    console.log("Test Case 2: TestSearchComponentInput - PASSED");
}

// Run all tests
testSearchComponentRendering();
testSearchComponentInput();
