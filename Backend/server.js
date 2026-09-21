const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000;

// Essential security bypass and content parsing configurations
app.use(cors());
app.use(bodyParser.json());

// Master Live Government Schemes Data Dictionary Store
const schemesDatabase = [
    {
        title: "Startup India Seed Fund Scheme (SISFS)",
        desc: "Provides critical seed financing capital up to ₹20 Lakhs for validation of proof of concept, prototype development, and product market deployment. Requires graduation status.",
        link: "https://startupindia.gov.in",
        budgets: ["mid", "high"],
        castes: ["General", "OBC", "SC", "ST"],
        allowedEducation: ["Graduate", "Post Graduate"],
        tag: "Universal Seed Fund"
    },
    {
        title: "Pradhan Mantri Mudra Yojana (PMMY)",
        desc: "Offers straightforward collateral-free business loans scaling up to ₹10 Lakhs to micro setups. Accessible across all basic qualification backgrounds.",
        link: "https://mudra.org.in",
        budgets: ["low", "mid"],
        castes: ["General", "OBC", "SC", "ST"],
        allowedEducation: ["Under Matric", "12th Pass", "Diploma/ITI", "Graduate", "Post Graduate"],
        tag: "Collateral-Free Loan"
    },
    {
        title: "Venture Capital Fund Scheme for SC/ST Entrepreneurs",
        desc: "Provides long-term concessional equity financial support and venture validation mechanisms exclusively optimized for SC and ST promoters holding a minimum technical or school certificate.",
        link: "https://ifciltd.com",
        budgets: ["mid", "high"],
        castes: ["SC", "ST"],
        allowedEducation: ["12th Pass", "Diploma/ITI", "Graduate", "Post Graduate"],
        tag: "SC/ST Venture Support"
    },
    {
        title: "Stand-Up India Funding Mechanism",
        desc: "Mandates greenfield project bank credit facilities between ₹10 Lakhs and ₹1 Crore. Specially reserved to support SC/ST categories or woman-led business units per branch.",
        link: "https://standupmitra.in",
        budgets: ["mid", "high"],
        castes: ["General", "OBC", "SC", "ST"],
        allowedEducation: ["12th Pass", "Diploma/ITI", "Graduate", "Post Graduate"],
        tag: "Marginalized Category Support"
    }
];

// Active Post Router Link
app.post('/api/schemes', (req, res) => {
    try {
        const { age, state, caste, education, businessType, budget } = req.body;

        // Perform Server-Side Array Filtering Logic
        let matched = schemesDatabase.filter(scheme => {
            const budgetMatch = scheme.budgets.includes(budget);
            const casteMatch = scheme.castes.includes(caste);
            const educationMatch = scheme.allowedEducation.includes(education);
            
            return budgetMatch && casteMatch && educationMatch;
        });

        // Generate dynamic state level grant template logic on-the-fly
        matched.push({
            title: `${state} State Institutional Startup Grant`,
            desc: `State-specific administrative funding and workspace policy custom-allocated to accelerate modern local ${businessType || 'business'} enterprise setups running inside ${state}.`,
            link: "https://startupindia.gov.in",
            tag: "State Level Benefit"
        });

        return res.json(matched);

    } catch (error) {
        console.error("API error environment trace:", error);
        return res.status(500).json({ error: "Internal Server Processing Failure" });
    }
});

app.listen(PORT, () => {
    console.log(`🚀 udayamX API Backend operational live at http://localhost:${PORT}`);
});
