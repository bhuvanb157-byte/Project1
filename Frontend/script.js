// ==========================================
// PRODUCTION BACKEND ENDPOINT CONFIGURATION
// ==========================================
const USE_REAL_BACKEND = true; 
const BACKEND_API_URL = "https://udyamx-8jth.onrender.com/api/schemes"; // Change to your live domain link when hosted (e.g., https://udayamx.com)

// Clean view navigation matrix routing switches
function navigateTo(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.add('hidden');
        page.classList.remove('fade-in');
    });
    
    const targetPage = document.getElementById(pageId);
    if (targetPage) {
        targetPage.classList.remove('hidden');
        setTimeout(() => {
            targetPage.classList.add('fade-in');
        }, 50);
    }
}

// Processing Client-Side Parameters and Generating Card View Clusters
function handleFormSubmit(event) {
    event.preventDefault();
    
    const caste = document.getElementById('caste').value;
    const state = document.getElementById('state').value;
    const education = document.getElementById('education').value;
    const budget = document.getElementById('budget').value;
    const business = document.getElementById('businessType').value;
    const age = document.getElementById('age').value;

    const filterContainer = document.getElementById('activeFilters');
    filterContainer.innerHTML = `
        <span class="badge">Age: ${age}</span>
        <span class="badge">State: ${state}</span>
        <span class="badge">Category: ${caste}</span>
        <span class="badge">Education: ${education}</span>
        <span class="badge">Industry: ${business}</span>
        <span class="badge">Budget: ${budget}</span>
    `;

    const resultsContainer = document.getElementById('schemesList');
    resultsContainer.innerHTML = '<div class="no-results">Searching live central and state portals... Please wait.</div>';

    function displayResults(schemesArray) {
        resultsContainer.innerHTML = '';
        if (!schemesArray || schemesArray.length === 0) {
            resultsContainer.innerHTML = `<p class="no-results">No specific specialized schemes found matching your profile configuration rules.</p>`;
            return;
        }
        schemesArray.forEach(scheme => {
            const card = document.createElement('div');
            card.className = 'scheme-card';
            card.innerHTML = `
                <div class="card-header">
                    <h3>${scheme.title}</h3>
                    <span class="card-tag">${scheme.tag}</span>
                </div>
                <p>${scheme.desc}</p>
                <a href="${scheme.link}" target="_blank" class="apply-link">Official Portal →</a>
            `;
            resultsContainer.appendChild(card);
        });
    }

    if (USE_REAL_BACKEND) {
        // REAL LIVE BACKEND API CONECTION ROUTINE
        fetch(BACKEND_API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ age, state, caste, education, businessType, budget })
        })
        .then(res => {
            if(!res.ok) throw new Error("Server responded with error status");
            return res.json();
        })
        .then(data => displayResults(data))
        .catch(err => {
            console.error("Database pipeline connection failure:", err);
            resultsContainer.innerHTML = `<p class="no-results" style="color: #ef4444;">⚠️ Backend Connection Failed. Ensure your Node.js terminal app is running server processes on port 5000!</p>`;
        });
    }

    navigateTo('resultsPage');
}
