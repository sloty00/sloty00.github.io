import feedparser
import json
import os

# Fuentes de Inteligencia (Partners)
FEEDS = {
    "sophos_threat": "https://news.sophos.com/en-us/category/threat-research/feed/",
    "sophos_ops": "https://news.sophos.com/en-us/category/security-operations/feed/",
    "aws_news": "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
}

def fetch_signals():
    all_news = []
    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # Solo las 3 más frescas por fuente
            all_news.append({
                "source": source,
                "title": entry.title,
                "link": entry.link,
                "date": entry.published if 'published' in entry else ""
            })
    
    # Asegurar que el directorio _data existe
    if not os.path.exists('_data'):
        os.makedirs('_data')
        
    with open('_data/soc_feed.json', 'w', encoding='utf-8') as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_signals()
