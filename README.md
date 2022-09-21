# CUC-Auto-Clock
简道云自动打卡


## Start

在 `info.py` 中更改自己的信息，并将 `main.py` 中的 `info.py` 修改为自己的配置文件。

也可以在命令行中补全

```bash
python main.py -s StudentNumber -p Password
```

使用 `python main.py -h` 查看更多用法。

## 持续集成服务

目前使用 `GitHub Action` 已完成初步测试，如有需要请自行修改。

## Acknowledgment

A special thanks goes to [Jiahong Shao](https://github.com/1746104160) & [Jie Wu](https://github.com/CreeseWu).

## Attention

(2022-09-08) 简道云打卡新增上传核酸图片，本程序目前不会上传该选项。

## Steps

1. 在 `Setting` > `Secrets` 中添加必要的安全信息，请联系 @LyuLumos，并使用其计算机添加，以保证信息安全性。
2. 新建个人文件夹 `{user}/`，并仿照 `info.py` 修改自己的 `{user}/info.py`。
2. 在 workflow 配置文件中仿照上文添加自己的任务。