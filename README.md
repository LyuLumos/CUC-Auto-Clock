# CUC-Auto-Clock
简道云自动打卡

[![CUC-Auto-Clock CI](https://github.com/LyuLumos/CUC-Auto-Clock/actions/workflows/main.yml/badge.svg)](https://github.com/LyuLumos/CUC-Auto-Clock/actions/workflows/main.yml)

## Start

本地运行请首先复制 `info-template.py` 为 `info.py`，在其中添加自己的信息。（该文件不会上传至git）

```bash
python main.py -s StudentNumber -p Password --userid UserID
```

上述的 `UserID` 为「发起者」对应的ID，请进行手机抓包获取。

使用 `python main.py -h` 查看更多用法。

## Attention

(2022-09-08) 简道云打卡新增上传核酸图片，本程序目前不会上传该选项。
(2022=10-05) 简道云更新机制，已进行对应修改，之前的版本不再有效。 

## 持续集成服务 :: Steps

目前使用 `GitHub Action` 已完成初步测试，如有需要请遵照以下步骤：

1. 在 `Setting` > `Secrets` 中添加必要的隐私信息，请联系 @LyuLumos，并使用其计算机添加，以保证信息安全性。
2. 新建个人文件夹 `{user}/`，并仿照 `info.py` 修改自己的 `{user}/info.py`。
3. 在 workflow 配置文件中仿照上文添加自己的任务。

PS. `GitHub.Action.Secrets` 不支持特殊符号，如感叹号 `!` 、百分号 `%`，如有涉及请拆分密码。[GitHub官方文档](https://docs.github.com/en/actions/security-guides/encrypted-secrets#naming-your-secrets)

`{user}/info.py` 对仓库的所有者与协作者公开，请勿上传隐私信息。

## Acknowledgment

A special thanks goes to [Jiahong Shao](https://github.com/1746104160) & [Jie Wu](https://github.com/CreeseWu).
