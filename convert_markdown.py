#!/usr/bin/env python3
import re
import os
import sys
def convert_gitbook_to_mkdocs(content, file_path):
    """Convert GitBook markdown syntax to Material for MkDocs syntax"""
    # Remove frontmatter description (keep it as comment or remove)
    content = re.sub(r'^---\s*\n.*?description:.*?\n---\s*\n', '', content, flags=re.DOTALL)
    # Convert {% hint style="..." %} to !!! admonition
    hint_map = {
        'info': 'info',
        'warning': 'warning',
        'danger': 'danger',
        'success': 'success',
        'tip': 'tip'
    }
    def replace_hint(match):
        style = match.group(1)
        content_text = match.group(2).strip()
        admon_type = hint_map.get(style, 'note')
        return f'!!! {admon_type}\n    {content_text.replace(chr(10), chr(10) + "    ")}'
    content = re.sub(r'{%\s*hint\s+style="([^"]+)"\s*%}(.*?){%\s*endhint\s*%}', replace_hint, content, flags=re.DOTALL)
    # Convert {% tabs %} to Material tabs
    # This is complex, so we'll do a basic conversion
    content = re.sub(r'{%\s*tabs\s*%}', '=== "Tab"', content)
    content = re.sub(r'{%\s*tab\s+title="([^"]+)"\s*%}', r'=== "\1"', content)
    content = re.sub(r'{%\s*endtab\s*%}', '', content)
    content = re.sub(r'{%\s*endtabs\s*%}', '', content)
    # Convert {% code %} blocks
    content = re.sub(r'{%\s*code.*?%}', '', content)
    content = re.sub(r'{%\s*endcode\s*%}', '', content)
    # Convert {% file src="..." %} to download links
    def replace_file(match):
        src = match.group(1)
        filename = os.path.basename(src)
        # Convert .gitbook/assets/ to images/
        new_src = src.replace('.gitbook/assets/', 'images/')
        new_src = new_src.replace('../.gitbook/assets/', '../images/')
        return f'[Download {filename}]({new_src}){{ .md-button }}'
    content = re.sub(r'{%\s*file\s+src="([^"]+)"\s*%}', replace_file, content)
    # Convert image references
    # ![text](<.gitbook/assets/image.png>) to ![text](images/image.png)
    content = re.sub(r'!\[([^\]]*)\]\(<\.gitbook/assets/([^)]+)>\)', r'![\1](images/\2)', content)
    content = re.sub(r'!\[([^\]]*)\]\(\.gitbook/assets/([^)]+)\)', r'![\1](images/\2)', content)
    content = re.sub(r'!\[([^\]]*)\]\(<\.\./\.gitbook/assets/([^)]+)>\)', r'![\1](../images/\2)', content)
    content = re.sub(r'!\[([^\]]*)\]\(\.\./\.gitbook/assets/([^)]+)\)', r'![\1](../images/\2)', content)
    # Convert <img> tags
    content = re.sub(r'<img\s+src="\.gitbook/assets/([^"]+)"', r'<img src="images/\1"', content)
    content = re.sub(r'<img\s+src="\.\./\.gitbook/assets/([^"]+)"', r'<img src="../images/\1"', content)
    # Clean up HTML entities
    content = content.replace('&#x20;', ' ')
    content = content.replace('&#x27;', "'")
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    # Remove GitBook specific divs
    content = re.sub(r'<div[^>]*data-full-width="true"[^>]*>', '', content)
    content = re.sub(r'</div>', '', content)
    # Convert <figure> to simple image
    def replace_figure(match):
        img_tag = match.group(1)
        caption = match.group(2) if match.group(2) else ''
        # Extract src from img tag
        src_match = re.search(r'src="([^"]+)"', img_tag)
        alt_match = re.search(r'alt="([^"]*)"', img_tag)
        if src_match:
            src = src_match.group(1)
            alt = alt_match.group(1) if alt_match else caption
            result = f'![{alt}]({src})'
            if caption:
                result += f'\n\n*{caption}*'
            return result
        return match.group(0)
    content = re.sub(r'<figure>(.*?)<img\s+([^>]+)>(.*?)<figcaption>(.*?)</figcaption>.*?</figure>', 
                     lambda m: replace_figure(m), content, flags=re.DOTALL)
    content = re.sub(r'<figure><img\s+([^>]+)>.*?</figure>', lambda m: replace_figure(m), content, flags=re.DOTALL)
    # Convert <mark> tags to == highlighting ==
    content = re.sub(r'<mark[^>]*>([^<]+)</mark>', r'==\1==', content)
    # Clean up excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Convert broken-reference to actual links (we'll need to fix these manually)
    content = content.replace('(broken-reference)', '(#)')
    return content
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        converted = convert_gitbook_to_mkdocs(content, file_path)
        print(converted)
    else:
        content = sys.stdin.read()
        print(convert_gitbook_to_mkdocs(content, ''))
