# 苏州大学计算机爱好者协会 2023魔盒挑战
本项目是一个简易的问卷系统，问卷可以根据结构化数据自动生成。

## 开发环境搭建

### 环境要求
- Python >= 3.9
- [Git](https://git-scm.com/)

### 环境配置
首先使用页面右上角的Fork按钮在自己的账户中创建该仓库的分支。

然后将仓库拉取到本地，其中`<userid>`应该是你的GitHub用户名：
```bash
$ git clone https://github.com/<userid>/pandora-2023-questionnaire.git
$ cd pandora-2023-questionnaire
```

使用python-venv创建并激活虚拟环境（参见[官方文档](https://docs.python.org/zh-cn/3/library/venv.html)）
```bash
$ python -m venv ./venv
> .\venv\Scripts\activate     # for Windows
$ source ./venv/bin/activate # for Linux
```

安装依赖：
```bash
(venv)$ pip install -r requirements.txt
```

安装Git Hooks（用于commit的前处理）：
```bash
(venv)$ pre-commit install
```

### 运行示例
以正常模式启动：
```bash
(venv)$ flask run
```
以调试（debug）模式启动
```bash
(venv)$ flask run --debug
```

启动后使用浏览器访问 http://127.0.0.1:5000 即可（这是默认地址，请查看上条指令的命令行输出以获得实际的地址）。

### 提交代码

首先将你更改的文件加入stage，`<filepath>`替换为文件路径，切记不要加入多余的文件。
```bash
$ git add <filepath>
```
然后创建commit，`<message>`替换为提交信息，即你做了什么更改，中英文皆可。
```bash
$ git commit -m "<message>"
```
在这一步会运行commit前检查，可能你会看到这样的信息，也就是代码检查工具[ruff](https://github.com/charliermarsh/ruff)报错，说明你的代码中有些地方不符合代码规范，这时你需要修改相应的文件。在本例中，错误出在`service/submit.py`这个文件的第26行过长（Line too long），在添加换行符后重新运行上面的commit指令即可。**代码检查与代码规范对于代码的可读性和可维护性至关重要**，在大项目中可以减少所谓“屎山代码”的存在，所以不要嫌麻烦哦。
```raw
ruff.....................................................Failed
- hook id: ruff
- exit code: 1

service/submit.py:26:75: E501 Line too long (97 > 88 characters)
Found 1 error.
```
注：在你编写完代码之后也可以在命令行执行`ruff check .`来运行代码检查

如果你遇到这个也需要重新运行commit
```raw
Trim Trailing Whitespace..............................Failed
- hook id: trailing-whitespace
- exit code: 1
- files were modified by this hook

Fixing ...
```

成功提交commit之后，回到你的账户下本仓库的分支（通常是在`https://github.com/<userid>/pandora-2023-questionnaire`），在标题下方可以看到
> This branch is 1 commit ahead, n commits behind sumsc-caa/pandora-2023-questionnaire:main.

右侧是按钮`Contribute`与`Sync Fork`，**前者点开之后可以向本仓库提交Pull Request**；后者的作用是让你的分支与本仓库同步，如果你在完成了一个任务之后要开发别的任务，请点击这个按钮。

### 相关资源
- flask库官方文档：https://flask.palletsprojects.com/
- jinja2库中文文档：https://docs.jinkan.org/docs/jinja2/
- sqlite3库官方中文文档：https://docs.python.org/zh-cn/3/library/sqlite3.html
- SQLite官网：https://www.sqlite.org/index.html
- HTML参考：https://developer.mozilla.org/zh-CN/docs/Web/HTML
- CSS参考：https://developer.mozilla.org/zh-CN/docs/Web/CSS
- Bootstrap官方文档：https://getbootstrap.com/docs/5.2/getting-started/introduction/
