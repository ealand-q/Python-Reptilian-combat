# Python 爬虫练习

本仓库保存 Python、requests、数据采集和可视化学习 Notebook。各示例依赖及运行顺序请查看 Notebook；第三方网站接口可能已经变化。

## 会话配置

登录态从本机环境变量 `SCRAPER_COOKIE` 读取。运行某个网站的示例前，在本机设置该网站的 Cookie，再启动 Jupyter。不同网站需分别配置，禁止提交 Cookie、令牌或本机环境文件。环境变量为空时，请求使用空 Cookie，需要登录的示例不会取得授权数据。

## 数据与安全

历史中的硬编码 Cookie 已替换，Notebook 运行输出与执行元数据已清除，抓取的用户昵称、评论及博文表格已移除。旧会话需要在相应网站退出或撤销才能失效。

提交前运行 `python scripts/check_sensitive_data.py`，并使用 Gitleaks 扫描完整 Git 历史。不要将真实抓取数据或运行输出提交到仓库。

本次整理未新增开源许可证；仓库公开与授予开源许可是不同事项。
