
# AI Website Summary Generator

## Overview
AI Website Summary Generator is a Streamlit app that reads the content of any website URL and provides a short, clear summary along with key topics. It's useful for getting quick insights without reading everything. Ideal for market research, competitive analysis, or content briefs.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Web Scraping**: BeautifulSoup, Requests
- **AI Summarization**: OpenAI GPT-4 API
- **Environment Management**: python-dotenv

## Screenshot
![Screenshot](screenshot.png)  
*A screenshot of the app interface where users can input a URL and receive an AI-generated summary.*

## Getting Started (Local Development)
1. **Clone the repo**  
```bash
git clone https://github.com/your-username/ai-website-summary-generator.git
cd ai-website-summary-generator
```

2. **Set up your environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. **Add your OpenAI API key**  
Create a `.env` file in the root directory and add:  
```
OPENAI_API_KEY=your_api_key_here
```

4. **Run the app**  
```bash
streamlit run app.py
```

## Deployment
This app is deployed on Streamlit Cloud. You can access it here:  
[https://website-summary.streamlit.app](https://website-summary.streamlit.app)

## Use Case
- **Content Creators**: Quickly generate content briefs.
- **Researchers**: Summarize long articles or reports.
- **Marketers**: Understand competitor websites fast.
- **Students**: Summarize educational content.

---
Created and maintained by [Your Name].
