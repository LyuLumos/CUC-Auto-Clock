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

## DEBUGGING!

`loginsso` > `aes.encrypt(password, salt)` 需要重新抓包验证，暂时无法调用。 