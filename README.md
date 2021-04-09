<h1 align="center">LztApi</h1>
<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Repo size" src="https://img.shields.io/github/repo-size/Infqq/lztapi">
    <img alt="issues" src="https://img.shields.io/github/issues/Infqq/lztapi">
</p>

## Установка
1) С помощью установщика pip из GitHub: 
   
   ```sh
   pip3 install https://github.com/Infqq/lztapi/archive/main.zip --upgrade
   ```

### Пример использования

```python
from lztapi import lztapi

api = lztapi("token")

print(api.userfind('InfinityJQ'))
```

### Доступные методы
- userfind
- threads
- profilePosts
- posts
- conversations
- threadInfo
- conversation
- notifications
- pages
- pagesById
- new_post
