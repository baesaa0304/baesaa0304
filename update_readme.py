import feedparser
import os

# 티스토리 RSS 피드 URL
RSS_FEED_URL = 'https://baesaa0304.tistory.com/rss'
MAX_POSTS = 5

def fetch_latest_posts():
    feed = feedparser.parse(RSS_FEED_URL)
    posts = []
    for entry in feed.entries[:MAX_POSTS]:
        title = entry.title
        link = entry.link
        published = entry.published
        posts.append(f'- [{title}]({link}) - {published}')
    return posts

def update_readme(posts):
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 최신 블로그 포스트 업데이트
    start_marker = '<!-- START BLOG POSTS -->'
    end_marker = '<!-- END BLOG POSTS -->'
    
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)
    
    if start_index == -1 or end_index == -1:
        print('Blog post markers not found in README.md.')
        return
    
    new_content = (content[:start_index + len(start_marker)] +
                   '\n'.join(posts) +
                   content[end_index:])
    
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == '__main__':
    posts = fetch_latest_posts()
    update_readme(posts)
