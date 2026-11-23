# 相关输入约束下的算子融合与区间证书

`data/record.json` 是 相关输入约束下的算子融合与区间证书 使用的本地合成交换样本。数组按 JSON 的下标顺序排列。本文的坐标、单位和枚举约定与该记录配套。记录中如果有 `scale` 或 `limits`，对应同一输入协议的部署规格。

参数变量落在命名的闭区间，offsets 是源张量对标识变量的仿射系数。标识包含归属批次，同一键共享同一实数。关系未知时为该处引入独立变量且保持原边界。nodes 依次记录输出、操作、父节点、参数。linear 参数是稀疏 [出,入,权重] 和标量偏置，relu 为 max(0,x)，clamp 给下限上限。决策在下界大于等于阈值时明确放行，上界严格小于阈值时明确回看，中间为不能决定。

## 读取样本

使用 Python 3.11 或 3.12，并在虚拟环境安装锁定依赖。读取入口返回原始记录。作为命令运行时，它会列出各顶层输入项目以及 NumPy 版本。

```sh
python -m pip install -r requirements.txt
python -m bounded_fusion_input
python -m unittest discover -s tests -v
```

测试读取交换样本，核对其中的张量尺寸、标识与数据约定。
