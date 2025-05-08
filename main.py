import markdown
from bs4 import BeautifulSoup

# 读取 HTML 模板文件
with open('blog.html', 'r', encoding='utf-8') as file:
    template = file.read()

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(template, 'html.parser')

# 定义章节列表
chapters = [
    {
        "filename": "第0章：前言.md",
        "id": "chapter0"
    },
    {
        "filename": "第1章：游戏介绍.md",
        "id": "chapter1"
    },
    {
        "filename": "第2章：写在最后.md",
        "id": "chapter2"
    }
]

# 遍历每个章节
for chapter in chapters:
    try:
        # 读取 Markdown 文件
        with open(chapter["filename"], 'r', encoding='utf-8') as file:
            md_content = file.read()

        # 将 Markdown 内容转换为 HTML
        html_content = markdown.markdown(md_content)

        # 找到对应的章节元素
        chapter_element = soup.find(id=chapter["id"])

        if chapter_element:
            # 清空原有的章节内容
            for child in chapter_element.find_all():
                child.decompose()

            # 将 HTML 内容添加到章节元素中
            chapter_element.extend(BeautifulSoup(html_content, 'html.parser').contents)
        else:
            print(f"未找到 ID 为 {chapter['id']} 的元素。")
    except FileNotFoundError:
        print(f"未找到文件：{chapter['filename']}")

# 将修改后的 HTML 保存到文件
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("HTML 文件已生成：index.html")