from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Upgraded database with "keywords" matching the business_type input
SCHEMES_DATABASE = [
    {
        "title": "Startup India Seed Fund Scheme (SISFS)",
        "desc": "Provides critical seed allocation grants up to ₹20 Lakhs for early-stage validation, prototype build-out, and commercial deployment tests.",
        "link": "https://startupindia.gov.in",
        "allowed_budgets": ["mid", "high"],
        "allowed_castes": ["General", "OBC", "SC", "ST"],
        "min_age": 18,
        "max_age": 100,
        "states": ["All"],
        "keywords": ["tech", "technology", "software", "ai", "hardware", "innovation", "medical"],
        "tag": "Universal Central Grant"
    },
    {
        "title": "Pradhan Mantri Mudra Yojana (PMMY)",
        "desc": "Offers structured collateral-free macro credit frameworks split into Shishu, Kishor, and Tarun tiers scaling financial assistance up to ₹10 Lakhs.",
        "link": "https://mudra.org.in",
        "allowed_budgets": ["low", "mid"],
        "allowed_castes": ["General", "OBC", "SC", "ST"],
        "min_age": 18,
        "max_age": 100,
        "states": ["All"],
        # Empty keywords list means it's universal for ALL business types
        "keywords": [], 
        "tag": "Micro Financing"
    },
    {
        "title": "Agri-Clinics and Agri-Business Centres Scheme (ACABC)",
        "desc": "Provides capital subsidies up to 44% for setting up agricultural ventures, farming tech platforms, and cold storage startups.",
        "link": "https://agriclinics.net",
        "allowed_budgets": ["low", "mid", "high"],
        "allowed_castes": ["General", "OBC", "SC", "ST"],
        "min_age": 18,
        "max_age": 60,
        "states": ["All"],
        "keywords": ["agriculture", "agri", "farming", "dairy", "poultry", "food processing"],
        "tag": "Agriculture Subsidy"
    },
    {
        "title": "Venture Capital Fund Scheme for SC/ST Entrepreneurs",
        "desc": "Provides long-term concessional equity financial support and venture validation mechanisms exclusively optimized for SC and ST promoters.",
        "link": "https://ifciltd.com",
        "allowed_budgets": ["mid", "high"],
        "allowed_castes": ["SC", "ST"],
        "min_age": 18,
        "max_age": 100,
        "states": ["All"],
        "keywords": [],
        "tag": "Exclusive Equity Allocation"
    },
    {
        "title": "Silk Samagr-2 (Integrated Silk Development Scheme)",
        "desc": "Assists handloom weavers and textile entrepreneurs with financial assistance, training, and technology scaling upgrades.",
        "link": "https://csb.gov.in",
        "allowed_budgets": ["low", "mid"],
        "allowed_castes": ["General", "OBC", "SC", "ST"],
        "min_age": 18,
        "max_age": 100,
        "states": ["All"],
        "keywords": ["textile", "cloth", "weaving", "garment", "fashion", "silk"],
        "tag": "Textile Industry Support"
    }
]

@app.route('/api/schemes', methods=['POST'])
def get_schemes():
    try:
        data = request.get_json()
        
        user_age = data.get('age')
        user_state = data.get('state')
        user_caste = data.get('caste')
        user_budget = data.get('budget')
        # Clean up the business type text input (lowercase and remove extra spaces)
        user_business_type = data.get('business_type', '').strip().lower()
        
        matched_schemes = []
        
        for scheme in SCHEMES_DATABASE:
            # 1. Match Age
            if not (scheme["min_age"] <= user_age <= scheme["max_age"]):
                continue
                
            # 2. Match Caste
            if user_caste not in scheme["allowed_castes"]:
                continue
                
            # 3. Match Budget
            if user_budget not in scheme["allowed_budgets"]:
                continue
                
            # 4. Match State
            if "All" not in scheme["states"] and user_state not in scheme["states"]:
                continue
                
            # 5. Smart Business Type Keyword Matching
            # If the scheme targets specific industries, check if the user's input matches any keyword
            if scheme["keywords"]:
                is_match = False
                for keyword in scheme["keywords"]:
                    if keyword in user_business_type:
                        is_match = True
                        break
                if not is_match:
                    continue # Skip this scheme if no keywords match the user's input
                
            matched_schemes.append({
                "title": scheme["title"],
                "desc": scheme["desc"],
                "link": scheme["link"],
                "tag": scheme["tag"]
            })
            
        return jsonify({"schemes": matched_schemes}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    

