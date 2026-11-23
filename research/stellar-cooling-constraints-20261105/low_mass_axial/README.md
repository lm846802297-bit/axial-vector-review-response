# 低质量轴矢量超新星计算包

本目录汇总低质量轴矢量 $A'$ 超新星辐射的数学推导与数值分析文档。计算程序、输入剖面和机器可读结果已存在于本研究目录的规范位置；本包通过相对链接统一索引，不复制第二份源码或数据，避免产生分叉版本。

## 文档

- [完整解析推导与数值结果](detailed_derivation_and_results.md)
- [数学推导](mathematical_derivation.md)
- [数值结果](numerical_results.md)

## 计算程序

### Moving-muon 局域微观核

- [moving-muon 半康普顿振幅与产生/吸收核](../finite_mixing/moving_muon_compton.py)
- [热缪子半康普顿与 dimuon 热积分入口](../finite_mixing/thermal_response_scan.py)
- [dimuon 产生/逆衰变积分](../finite_mixing/thermal_dimuon.py)
- [共享碰撞率与衰变率](../rates.py)

### 固定剖面超新星冷却扫描

- [扫描入口](../run_scan.py)
- [径向传播、光学深度与逃逸积分](../transport.py)
- [局域产生、吸收和衰变率](../rates.py)

### 原始单 VEV 模型映射

- [单 VEV 轴矢量参数映射](../../stellar-cooling-original-uv-model-20261105/single_vev_axial_mapping.py)

## 输入数据

- [SFHo-18.8 数字化径向剖面](../data/sfho188_digitized.csv)

## 原始数值结果

### 局域 moving-muon 热积分

- [极化分辨热响应结果](../finite_mixing/outputs/thermal_response_scan.json)

该结果包含中心与中间半径的局域半康普顿响应、三个极化态、$\mu^-$/$\mu^+$ 分辨结果及积分收敛检查。它是局域微观率，不是径向积分后的 SN1987A 逃逸光度。

### 固定剖面冷却扫描

- [轴矢量质量–耦合扫描](../outputs/axial.json)
- [高阶收敛结果](../outputs/convergence.json)
- [数值验证汇总](../outputs/numerical_validation.json)

这些结果是固定剖面 ballistic cooling benchmark。它们尚未使用上述 moving-muon 极化分辨核完成全径向输运更新。

## 计算入口

从仓库根目录运行局域 moving-muon 热响应扫描：

\`\`\`bash
python research/stellar-cooling-constraints-20261105/finite_mixing/thermal_response_scan.py
\`\`\`

固定剖面冷却扫描的参数由对应 JSON 中的 \`config\` 和 \`couplings\` 记录。入口程序为 \`research/stellar-cooling-constraints-20261105/run_scan.py\`。

## 结果状态

- 已完成：轴流 Ward identity/Goldstone 标度推导、moving-muon 局域半康普顿积分、极化分辨热率及局域数值收敛检查。
- 已有：固定剖面 ballistic 质量–耦合冷却扫描及其高阶积分验证。
- 尚未完成：将 moving-muon 半康普顿产生核与逆过程吸收核同时接入完整径向输运，并重新提取最终 trapping 边界。

因此，本文中的低质量耦合下界标度有解析和局域数值支持；由现有固定剖面扫描映射得到的 $v_s$ 排除区间仍是条件性结果，不应标记为 moving-muon 修正后的最终超新星限制。
