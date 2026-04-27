import feedparser
import json
import os

# Fuentes de Inteligencia (Partners)
FEEDS = {
    "sophos_threat": "https://news.sophos.com/en-us/category/threat-research/feed/",
    "sophos_ops": "https://news.sophos.com/en-us/category/security-operations/feed/",
    "ms_cloud": "https://azure.microsoft.com/en-us/updates/feed/",
    "gcp_cloud": "https://blog.google/products/google-cloud/rss/",
    "aws_news": "https://aws.amazon.com/about-aws/whats-new/recent/feed/",
    "ms_security": "https://www.microsoft.com/en-us/msrc/blog/feed",
    "veeam_intel": "https://www.veeam.com/blog/feed",
    "suse_news": "https://www.suse.com/c/feed/",
    "bradcom_tech": "https://www.broadcom.com/blog/rss",
    "broadcom_vmware": "https://blogs.vmware.com/feed"
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
