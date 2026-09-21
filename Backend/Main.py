const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000;

// Security and parser middleware arrays
app.use(cors());
app.use(bodyParser.json());

// Master production database array inside server storage memory
const schemesDatabase = [
    {
        title: "Startup India Seed Fund Scheme (SISFS)",
        desc: "Provides critical seed financing capital up to ₹20 Lakhs for validation of proof of concept, prototype engineering, and initial trial releases. Requires minimum Graduate qualification status.",
        link: "https://startupindia.gov.in",
        budgets: ["mid", "high"],
        castes: ["General", "OBC", "SC", "ST", "EWS", "Minority"],
        minEducationTier: ["Graduate", "Post Graduate"],
        deadline: "31-Mar-2027",
        tag: "Universal Seed Fund"
    },
    {
        title: "Pradhan Mantri Mudra Yojana (PMMY)",
        desc: "Offers straightforward collateral-free business loans up to ₹10 Lakhs. Open to all educational levels.",
        link: "https://mudra.org.in",
        budgets: ["low", "mid"],
        castes: ["General", "OBC", "SC", "ST", "EWS", "Minority"],
        minEducationTier: ["Under Matric", "12th Pass", "Diploma/ITI", "Graduate", "Post Graduate"],
        deadline: "Open All Year",
        tag: "Collateral-Free Loan"
    },
    {
        title: "Stand-Up India Scheme",
        desc: "Mandates bank credit facilities between ₹10 Lakhs and ₹1 Crore. Specially reserved to support SC/ST categories or woman-led business units per branch.",
        link: "https://standupmitra.in",
        budgets: ["mid", "high"],
        castes: ["General", "OBC", "SC", "ST", "EWS", "Minority"],
        minEducationTier: ["12th Pass", "Diploma/ITI", "Graduate", "Post Graduate"],
        deadline: "31-Dec-2026",
        tag: "Marginalized Category Support",
        isSpecialField: true
    },
    {
        title: "Venture Capital Fund Scheme for SC Entrepreneurs",
        desc: "Long-term concessional equity financial support and asset acceleration mechanisms optimized directly for Scheduled Caste business owners.",
        link: "https://ifciltd.com",
        budgets: ["mid", "high"],
        castes: ["SC"],
        minEducationTier: ["Diploma/ITI", "Graduate", "Post Graduate"],
        deadline: "15-Nov-2026",
        tag: "SC Venture Support"
    },
    {
        title: "National Minorities Development Support (NMDFC)",
        desc: "Offers low-interest business micro-loans and working capital specifically provisioned for young entrepreneurs from minority backgrounds.",
        link: "http://nmdfc.org",
        budgets: ["low", "mid"],
        castes: ["Minority"],
        minEducationTier: ["Under Matric", "12th Pass", "Diploma/ITI", "Graduate", "Post Graduate"],
        deadline: "Open All Year",
        tag: "Minority Priority Credit"
    }
];

// POST API route to handle demographic sorting matching rules
app.post('/api/schemes', (req, res) => {
    try {
        const { age, gender, caste, education, state, businessType, budget } = req.body;

        // Execute Server-Side Processing Criteria
        let matchedSchemes = schemesDatabase.filter(scheme => {
            const budgetMatch = scheme.budgets.includes(budget);
            const casteMatch = scheme.castes.includes(caste);
            const educationMatch = scheme.minEducationTier.includes(education);
            
            if (scheme.isSpecialField) {
                return budgetMatch && educationMatch && (caste === "SC" || caste === "ST" || gender === "Female");
            }
            return budgetMatch && casteMatch && educationMatch;
        });

        // Generate custom state localized results array template inside dataset response packet
        matchedSchemes.push({
            title: `${state} State Institutional Startup Grant`,
            desc: `State-specific administrative funding platform custom-allocated to accelerate modern local ${businessType || 'business'} frameworks established here in ${state}.`,
            link: "https://startupindia.gov.incontent/sih/en/state-startup-policies.html",
            deadline: "31-Jan-2027",
            tag: "State Level Benefit"
        });

        return res.json(matchedSchemes);

    } catch (error) {
        console.error("Server Pipeline Error:", error);
        return res.status(500).json({ error: "Internal Server Processing Failure" });
    }
});

app.listen(PORT, () => {
    console.log(`🚀 udayamX API Backend operational at http://localhost:${PORT}`);
});
