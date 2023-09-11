```python
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from transformers import pipeline

nltk.download('stopwords')


class AutonomousWebContentAggregator:
    def __init__(self):
        self.topic_selector = TopicSelector()
        self.web_scraper = WebScraper()
        self.summarizer = Summarizer()
        self.keyword_extractor = KeywordExtractor()
        self.content_generator = ContentGenerator()
        self.media_downloader = MediaDownloader()
        self.seo_optimizer = SeoOptimizer()
        self.content_publisher = ContentPublisher()
        self.user_engagement_analyzer = UserEngagementAnalyzer()

    def run_program(self):
        # Step 1: Topic Selection
        trending_topics = self.topic_selector.identify_trending_topics()
        relevant_topics = self.topic_selector.suggest_relevant_topics(
            trending_topics)

        for topic in relevant_topics:
            # Step 2: Web Scraping
            news_data = self.web_scraper.scrape_news(topic)
            blog_data = self.web_scraper.scrape_blogs(topic)
            social_media_data = self.web_scraper.scrape_social_media(topic)

            # Step 3: Summarization and Keyword Extraction
            summarized_news = self.summarizer.summarize_data(news_data)
            summarized_blogs = self.summarizer.summarize_data(blog_data)
            summarized_social_media = self.summarizer.summarize_data(
                social_media_data)

            news_keywords = self.keyword_extractor.extract_keywords(news_data)
            blog_keywords = self.keyword_extractor.extract_keywords(blog_data)
            social_media_keywords = self.keyword_extractor.extract_keywords(
                social_media_data)

            # Step 4: Content Generation
            generated_content = self.content_generator.generate_content(
                summarized_news, summarized_blogs, summarized_social_media,
                news_keywords, blog_keywords, social_media_keywords
            )

            # Step 5: Multi-media Integration
            multimedia_elements = self.media_downloader.download_multimedia(
                topic)
            content_with_media = self.media_downloader.integrate_multimedia(
                generated_content, multimedia_elements)

            # Step 6: SEO Optimization
            optimized_content = self.seo_optimizer.optimize_content(
                content_with_media, news_keywords + blog_keywords + social_media_keywords)

            # Step 7: Content Publishing and Scheduling
            self.content_publisher.publish_content(optimized_content)

            # Step 8: User Engagement Analysis
            self.user_engagement_analyzer.analyze_engagement()


class TopicSelector:
    def __init__(self):
        self.news_websites = [
            "https://example-news-website.com", "https://another-news-website.com"]
        self.blogs = ["https://example-blog.com", "https://another-blog.com"]
        self.social_media_platforms = [
            "https://twitter.com", "https://facebook.com"]

    def identify_trending_topics(self):
        trending_topics = []

        for website in self.news_websites:
            trending_topics += self.scrape_popular_topics(website)

        for blog in self.blogs:
            trending_topics += self.scrape_popular_topics(blog)

        for platform in self.social_media_platforms:
            trending_topics += self.scrape_popular_topics(platform)

        return trending_topics

    def scrape_popular_topics(self, url):
        trending_topics = []
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            topics = soup.find_all('a', {'class': 'topic-link'})
            for topic in topics:
                trending_topics.append(topic.text)
        return trending_topics

    def suggest_relevant_topics(self, trending_topics):
        return trending_topics[:5]


class WebScraper:
    def scrape_news(self, topic):
        return f"Scraped news data for {topic}"

    def scrape_blogs(self, topic):
        return f"Scraped blog data for {topic}"

    def scrape_social_media(self, topic):
        return f"Scraped social media data for {topic}"


class Summarizer:
    def __init__(self):
        self.summarization_model = pipeline("summarization")

    def summarize_data(self, data):
        summarized_data = self.summarization_model(
            data, max_length=100, min_length=50, do_sample=False)
        return summarized_data[0]["summary_text"]


class KeywordExtractor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def extract_keywords(self, data):
        keywords = []
        tokens = nltk.word_tokenize(data)
        words = [word.lower() for word in tokens if word.isalpha()]
        keywords = [word for word in words if word not in self.stop_words]
        return keywords


class ContentGenerator:
    def generate_content(self, summarized_news, summarized_blogs, summarized_social_media,
                         news_keywords, blog_keywords, social_media_keywords):
        return "Generated content"


class MediaDownloader:
    def download_multimedia(self, topic):
        return ["image1.jpg", "video1.mp4"]

    def integrate_multimedia(self, content, multimedia_elements):
        return content


class SeoOptimizer:
    def optimize_content(self, content, keywords):
        return content


class ContentPublisher:
    def publish_content(self, content):
        pass


class UserEngagementAnalyzer:
    def analyze_engagement(self):
        pass


program = AutonomousWebContentAggregator()
program.run_program()
```
