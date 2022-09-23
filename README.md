# CUC-Auto-Clock
简道云自动打卡


## Start

本地运行请首先复制 `info-template.py` 为 `info.py`，在其中添加自己的信息。（该文件不会上传至git）

```bash
python main.py -s StudentNumber -p Password --userid UserID
```

关于上述的 `UserID`，强烈建议手动抓包，对应简道云打卡的 `发起者` 项，默认使用ljy的UserID（不建议）

使用 `python main.py -h` 查看更多用法。

## Attention

(2022-09-08) 简道云打卡新增上传核酸图片，本程序目前不会上传该选项。

## 持续集成服务 :: Steps

目前使用 `GitHub Action` 已完成初步测试，如有需要请遵照以下步骤：

1. 在 `Setting` > `Secrets` 中添加必要的隐私信息，请联系 @LyuLumos，并使用其计算机添加，以保证信息安全性。
2. 新建个人文件夹 `{user}/`，并仿照 `info.py` 修改自己的 `{user}/info.py`。
3. 在 workflow 配置文件中仿照上文添加自己的任务。
PS. `GitHub.Action.Secrets` 不支持特殊符号，如感叹号 `!` 、百分号 `%`，如有涉及请拆分密码。[GitHub官方文档](https://docs.github.com/en/actions/security-guides/encrypted-secrets#naming-your-secrets)

## Acknowledgment

A special thanks goes to [Jiahong Shao](https://github.com/1746104160) & [Jie Wu](https://github.com/CreeseWu).
