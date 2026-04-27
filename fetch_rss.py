import feedparser
import json
import os

# Fuentes de Inteligencia (Partners)
FEEDS = {
    "sophos_threat": "https://news.sophos.com/en-us/category/threat-research/feed/",
    "sophos_ops": "https://news.sophos.com/en-us/category/security-operations/feed/",
    "ms_cloud": "https://azure.microsoft.com/en-us/updates/feed/",        # <--- Microsoft Cloud
    "gcp_cloud": "https://blog.google/products/google-cloud/rss/",      # <--- Google Cloud
    "aws_news": "https://aws.amazon.com/about-aws/whats-new/recent/feed/",# <--- AWS
    "ms_security": "https://www.microsoft.com/en-us/msrc/blog/feed"      # <--- MS Security
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
