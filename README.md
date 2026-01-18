# Scrapper_exp2

A web scraping and data visualization project that collects quotes from the web and provides an interactive dashboard for analysis.

## 📋 Project Structure

```
Scrapper_exp2/
├── scrapper.py              # Web scraping module
├── dashboard.py             # Streamlit interactive dashboard
├── logger.py                # Logging configuration
├── visualiz.py              # Visualization utilities
├── eda_visualization.py      # Exploratory data analysis
├── requirements.txt         # Project dependencies
├── scraped_data.csv         # Collected quote data
└── data/                    # Data directory
```

## 🎯 Features

- **Web Scraping**: Collects quotes from quotes.toscrape.com using BeautifulSoup
- **Data Processing**: Cleans and processes scraped data using Pandas
- **Sentiment Analysis**: Analyzes sentiment of quotes using TextBlob
- **Interactive Dashboard**: Streamlit-based dashboard with filters and visualizations
- **Word Cloud Generation**: Visual representation of frequently used words
- **Logging**: Comprehensive logging for data collection process

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Installation

1. Clone or navigate to the project directory:
```bash
cd Scrapper_exp2
```

2. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

## 📦 Dependencies

- **requests** - HTTP library for web requests
- **beautifulsoup4** - HTML/XML parsing
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **nltk** - Natural language processing
- **pymongo** - MongoDB database driver
- **matplotlib** - Plotting library
- **seaborn** - Statistical data visualization
- **networkx** - Network analysis
- **scikit-learn** - Machine learning library
- **textblob** - Text processing and sentiment analysis
- **streamlit** - Web app framework
- **plotly** - Interactive visualizations
- **flask** - Web framework
- **wordcloud** - Word cloud generation

## 💻 Usage

### Run Data Scraper
```bash
python scrapper.py
```
This will scrape quotes from the website and save them to `data/scraped_data.csv`.

### Launch Interactive Dashboard
```bash
python -m streamlit run dashboard.py
```
Open your browser and navigate to `http://localhost:8501` to access the interactive dashboard with filters and visualizations.

### Exploratory Data Analysis
```bash
python eda_visualization.py
```
Generates visualization and analysis of the collected data.

## 📊 Data

The scraped data includes:
- **quote**: The quote text
- **author**: Author of the quote
- **tags**: Associated tags/categories
- **page**: Source page number

## 🔧 Configuration

Logging is configured in `logger.py`. Adjust logging levels and format as needed for your use case.

## 📝 Notes

- The scraper targets quotes.toscrape.com (a free practice website)
- Sentiment analysis is performed on cleaned text
- The dashboard provides real-time filtering by sentiment and author
- Data is stored in CSV format for easy access and portability

## 🤝 Contributing

Feel free to modify and extend the project for your needs!

## 📄 License

This is an experimental project for learning web scraping and data visualization.
