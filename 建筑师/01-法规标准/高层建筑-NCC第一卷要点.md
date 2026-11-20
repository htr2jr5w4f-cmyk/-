# 高层建筑-NCC第一卷要点

适用州：全国（重点 QLD）｜资料核对日期：2026-11-20｜状态：大部分已核实（条款逐条对照 ncc.abcb.gov.au 的 NCC 2022 Volume One 在线原文），少数待证实

## 摘要
本文整理一栋布里斯班 20 层左右的混合用途大楼（Class 2 公寓 + Class 7a 地下停车 + Class 5/6 底商，可能带 Class 9）要用到的 NCC 2022 Volume One 条款。截至 2026-11-20，昆州仍执行 NCC 2022；NCC 2025 在昆州 2027-05-01 才生效 [S1][S2]。内容覆盖：建筑分类（Part A6）、Type of construction 与 FRL（C2D2、Specification 5）、effective height 定义和 25 m 阈值（喷淋、烟感、应急电梯、EWIS、消防控制中心、楼梯加压）、疏散（Part D2）、无障碍（Part D4 + Premises Standards）、能效（Section J，Class 2 公寓按 NatHERS 平均 7 星 / 单户不低于 6 星）、隔声（NCC 2022 是 **Part F7**，不是 F5，F5 是层高）、防水（F1D5、F2D2）和冷凝（Part F8），最后讲 DtS 与 Performance Solution 的关系、fire engineering 的法定流程（A2G2(4)）。
对省钱的用处：①在方案阶段就把高度控制在 25 m effective height 的上面还是下面，会整体改变消防系统配置，是最大的成本分水岭之一；②Type A 各类别的 FRL 不同（Class 2 是 90 分钟，Class 5/7a 是 120 分钟，Class 6 是 180 分钟），合理安排各类别所在楼层和防火分隔可以少做高 FRL 构件；③用 Performance Solution 替代 DtS 往往能省钱（例如减少楼梯或延长疏散距离），但必须走完整的 fire engineering 流程并转介 Queensland Fire and Rescue（QFR）审查（见 `高层建筑-规划审批与消防审查.md`）。

> 核对方式：第二轮网络放行后，本文所有 NCC 条款都直接从 ncc.abcb.gov.au「NCC 2022 Volume One Online」各 Part 页面读取（在线版为已纳入修订的现行文本）。条款号用 NCC 2022 新编号（如 C2D2），括号里可注明 2019 版旧编号（如 C1.1），便于对照旧图纸和旧报告。NCC 2025 的条款编号可能变化，2027-05-01 以后的项目要重新核对。

---

## 1. 版本和昆州的特殊规定

| 项目 | 内容 | 来源 | 状态 |
|---|---|---|---|
| 昆州现行版本 | NCC 2022（Volume One = BCA Class 2–9） | [S1][S2] | 已核实 |
| NCC 2025 在昆州 | 2027-05-01 起采用，无过渡期栏目（N/A） | [S2] | 已核实 |
| 按哪一版审批 | 由 Building Act 1975 (Qld) s36、s37 决定（申请获批时有效的版本；修订前已提交申请等情况可沿用旧版），详见 `NCC现行版本与住宅要求.md` | [S3] | 已核实（见该文件） |
| NCC 2022 Volume One 昆州变体（Schedule 7） | 只涉及 Part B1（结构）、Part G1（小型结构和构件）、Part G5（bushfire prone areas）和参考文件 | [S4] | 已核实 |
| 昆州其他法规 | NCC 的昆州附注说明：影响建筑设计、施工、性能的法定技术要求都集中在 Building Act 1975 及其下的规章、规范和标准中；**Class 2 建筑的能效还受 Queensland Development Code MP 4.1 – Sustainable buildings 约束** | [S5] | 已核实（附注原文）；MP 4.1 现行内容待证实 |

⚠ 州差异：NCC Volume One 中有大量 NSW、VIC、SA、TAS、WA 的变体（例如 VIC 禁止用 Performance Solution 来证明可燃外墙合规，A2G2(5)）。本文只写全国通用条款和昆州情况，其他州的变体不适用于布里斯班项目 [S6]。

---

## 2. 建筑分类（Part A6）

| 类别 | NCC 2022 条款 | 定义要点 | 来源 |
|---|---|---|---|
| Class 2 | A6G3 | 含两个或以上 sole-occupancy unit（SOU）的建筑，每个 SOU 是独立住所。住宅单元上下叠放时一定是 Class 2 或 Class 3，不可能是 Class 1 | [S7] |
| Class 4 | A6G5 | Class 5–9 建筑里唯一的一套住宅（如看守人公寓）；Class 2 里不能有 Class 4 | [S7] |
| Class 5、6、7a、9 | A6G6–A6G10（条款号按在线目录顺序，标题见原文） | 5 = 办公；6 = 零售/餐饮等；7a = 停车库；9 = 公共建筑（9a 医疗、9b 集会/学校/托儿、9c 养老） | [S7] 条款号对应待逐条复核 |
| 小面积附属用途 | A6G1 | 某层不同用途的部分小于该层面积 10% 时，可按该层其他部分的类别归类；但实验室、Class 9b 托儿中心、Class 2/3/4 部分不能用这条豁免。plant room、机房、电梯机房按其所在部分的类别 | [S7] |
| 混合用途 | C2D4（多类别建筑）、A6G1 | 一栋楼可同时有多个类别，每个部分按其类别适用要求；类别之间的防火分隔见 C3D9、C3D10 | [S8][S9] |

典型 20 层混合大楼：地下室 Class 7a 停车 → 地面层 Class 6 商铺 / Class 5 办公 → 上部 Class 2 公寓（屋顶可能有公共活动区，属于 Part G6 occupiable outdoor area）。

---

## 3. Type of construction 与 FRL（Part C2、Specification 5）

### 3.1 Type 的确定：C2D2 和 Table C2D2（2019 版 C1.1）[S8]

| Rise in storeys | Class 2、3、9 | Class 5、6、7、8 |
|---|---|---|
| 4 层或以上 | A | A |
| 3 | A | B |
| 2 | B | C |
| 1 | C | C |

- Type A 防火能力最强，Type C 最弱 [S8]。20 层大楼一律是 **Type A**。
- **Rise in storeys 的计算（C2D3）**：取外墙任一处地面以上的最大层数，加上屋顶空间内的楼层。不计入的有：顶部只放暖通、电梯设备、水箱等设备的楼层；部分埋在地下、顶棚底面高出外墙处平均完成地面不超过 1 m 的楼层（外墙超过 12 m 长时，取地面最低的 12 m 段平均）。面积超过 200 m² 或超过所在房间面积 ⅓（取小者）的夹层要算一层 [S8]。所以地下室通常不计入 rise in storeys。
- C2D5 允许混合 Type（mixed types of construction），C2D6 是两层 Class 2/3/9c 的放宽，与高层无关 [S8]。

### 3.2 Type A 的 FRL（Specification 5，S5C11，Tables S5C11a–g）[S10]

FRL 写法为「结构稳定性 / 完整性 / 隔热性」（分钟）。下表摘自原文，只列高层最常用的几项：

| 构件 | Class 2、3 或 4 部分 | Class 5、7a 或 9 | Class 6 |
|---|---|---|---|
| 承重外墙，距 fire-source feature < 1.5 m（Table S5C11a） | 90/90/90 | 120/120/120 | 180/180/180 |
| 承重外墙，1.5 m 至 < 3 m | 90/60/60 | 120/90/90 | 180/180/120 |
| 承重外墙，≥ 3 m | 90/60/30 | 120/60/30 | 180/120/90 |
| 非承重外墙 < 1.5 m（Table S5C11b） | –/90/90 | –/120/120 | –/180/180 |
| 非承重外墙 ≥ 3 m | –/–/– | –/–/– | –/–/– |
| 外露承重柱（Table S5C11c） | 90/–/– | 120/–/– | 180/–/– |
| Common wall 和 fire wall（Table S5C11d） | 90/90/90 | 120/120/120 | 180/180/180 |
| 承重内墙：防火电梯井和楼梯井（Table S5C11e） | 90/90/90 | 120/120/120 | 180/120/120 |
| 承重内墙：公共走廊 / SOU 之间 | 90/90/90 | 120/–/– | 180/–/– |
| 非承重内墙：防火电梯井和楼梯井（Table S5C11f） | –/90/90 | –/120/120 | –/120/120 |
| 非承重内墙：公共走廊 / SOU 之间 | –/60/60 | –/–/– | –/–/– |
| 楼板（Table S5C11g） | 90/90/90 | 120/120/120 | 180/180/180 |
| 屋面（Table S5C11g） | 90/60/30 | 120/60/30 | 180/60/30 |
| 其他承重内墙、梁、桁架、柱 | 90/–/– | 120/–/– | 180/–/– |

其他要点 [S10]：
- 需要完整性和隔热性的内墙要做到上层楼板底面（或符合要求的屋面 / 耐火吊顶）为止（S5C11(1)(b)）。
- Type A 中承重内墙和承重 fire wall（含承重竖井）只能用混凝土、砌体、fire-protected timber 或其组合；用 fire-protected timber 有前提：effective height 不超过 25 m、全楼喷淋（不能是 FPAA101D/H 系统）、空腔内保温不燃、按 Specification 9 设空腔防火隔断（S5C11(2)）。所以 20 层楼的核心筒基本是混凝土。
- S5C12 起还有 Type A 楼板等的放宽条款（例如喷淋建筑的部分放宽），用之前逐条读原文。
- Class 7a 停车库与上部 Class 2 之间的楼板，按「不同楼层的不同类别分隔」C3D10 处理 [S9]。

### 3.3 不燃要求和外墙（C2D10、C2D12、Specification 8）[S8][S11]

- **C2D10(1)**：Type A 或 B 建筑中，**外墙和 common wall（含饰面层、龙骨、保温等全部构件）**、电梯坑地面与框架、需要防火的非承重内墙，必须不燃（non-combustible）[S8]。
- C2D10(2)：Type A 建筑中非承重的电梯井、通风井、管井、垃圾井等竖井必须不燃 [S8]。
- C2D10(4) 列出可以例外的小部件，例如垫片、密封胶、玻璃、宽度不超过 50 mm 的缝隙填充、油漆涂层等；C2D10(5) 列出本身就算不燃的材料（混凝土、钢、砌体、铝、AAC、石材、陶瓷、铜锌铅等）；C2D10(6) 列出可在要求不燃处使用的材料（石膏板、纤维水泥板、表层可燃涂层 ≤1 mm 且 Spread-of-Flame Index 为 0 的预涂金属板、各层都不燃且胶层符合限值的复合板等）[S8]。
- C2D12「Performance of external walls in fire」和 Specification 8：外墙防火性能的测试路线（AS 5113）[S8][S11]。Specification 8 的具体验收标准：本文未逐条摘录，待证实。
- A5G8：铝复合板（ACP）的标识要求 [S12]。
- 昆州另有可燃外墙的行政规定（Building Regulation 2021 的 Safer Buildings 程序、2019 年起昆州禁止在部分建筑上使用 PE 芯 ACP），见 `高层建筑-规划审批与消防审查.md` 第 6 节。

---

## 4. Effective height 与各高度阈值

**定义（Schedule 1 Definitions）**：effective height 是 rise in storeys 计算中最低一层楼面与最高一层楼面之间的垂直距离（如果顶层只放暖通、电梯设备、水箱或类似设备，则不计顶层）[S13]。注意：量的是「楼面到楼面」，不是建筑总高；最低一层是「计入 rise in storeys 的最低层」，所以不计入的地下室不算。

| 阈值 | 要求 | 条款 | 来源 |
|---|---|---|---|
| 施工中 effective height 达到 12 m | 每层被上部楼板或屋面覆盖的楼层（最上面 2 层除外）的消火栓和消防卷盘要能用；要求设置的 booster 接口要装好；每层每个出口或临时楼梯旁至少放一个适用 A、B、C 类火和电气火的灭火器 | E1D16 | [S14] |
| effective height > 12 m（不需要应急电梯时） | 客梯服务 12 m 以上楼层的，至少一部客梯要有担架空间（净空不小于 600 mm 宽 × 2000 mm 长 × 1400 mm 高） | E3D3 | [S15] |
| Class 2/3：rise in storeys ≥ 4 且 effective height ≤ 25 m | 全楼喷淋（按 Specification 17 和 Specification 18，可用住宅型喷淋系统） | E1D6 | [S14] |
| **任何部分 effective height > 25 m** | **全楼喷淋**，包括混合用途建筑中的 open-deck 停车库；独立的 open-deck 停车库建筑和 ≤200 m² 的 Class 8 变电站除外 | E1D5 | [S14] |
| > 25 m | Class 2/3 部分须设符合 Specification 20 的自动烟感报警系统 | E2D5 | [S16] |
| > 25 m | 至少一部应急电梯，设在符合 C3D11 的防火井道中；有两部及以上客梯服务同一楼层时，至少两部应急电梯，不同井道时每个井道至少一部 | E3D5 | [S15] |
| > 25 m | 每层至少 2 个出口（另加 horizontal exit） | D2D3(2) | [S17] |
| > 25 m | 安装 emergency warning and intercom system（EWIS，AS 1670.4） | E4D9 | [S18] |
| > 25 m | 设消防控制中心（按 Specification 19）；Class 6–9 总楼面面积超过 18 000 m² 也要设 | E1D15 | [S14] |
| 服务 25 m 以上楼层的防火楼梯 | 自动加压送风（AS 1668.1），或按 D3D6 设开敞通道/阳台；服务超过 2 层不计入 rise in storeys 的地下层的防火楼梯也要 | E2D4 | [S16] |
| effective height > 75 m | 应急电梯额定载重不低于 600 kg（无担架设施）或 900 kg（有担架设施） | E3D5(4) | [S15] |
| 楼面面积 > 500 m² 且距消防站沿道路不超过 50 km（站内有能使用消火栓的设备） | 设消火栓系统（AS 2419.1） | E1D2 | [S14] |
| Class 2、3、5 | 不适用消防卷盘条款（E1D3(1)）；Class 6、7a 等其他部分仍按 E1D3 设置 | E1D3 | [S14] |
| Class 7a（非 open-deck） | 一个防火分区停放超过 40 辆车时须喷淋 | E1D9 | [S14] |
| Class 7a 机械通风 | 按 AS 1668.2 机械通风的 Class 7a（含地下室）须符合 AS 1668.1 第 5.5 条 | E2D12 | [S16] |
| Class 6 | 防火分区面积超过 3 500 m² 或体积超过 21 000 m³ 时须喷淋 | E1D8 | [S14] |

25 m 阈值的理由（E1D5 解释性说明）：25 m 是消防云梯和其他灭火救援设备的有效工作高度 [S14]。

**Section C、D、E 的结构**（按在线目录）[S6]：
- Section C Fire resistance：C1（性能要求 C1P1–C1P9）、C2 Fire resistance and stability（Type of construction）、C3 Compartmentation and separation（防火分区、外墙开口竖向分隔 C3D7、电梯井 C3D11、设备分隔 C3D13、供电 C3D14、Class 2/3 公共走廊 C3D15）、C4 Protection of openings；Specifications 5–13。
- Section D Access and egress：D1（性能要求）、D2 Provision for escape、D3 Construction of exits、D4 Access for people with a disability；Specifications 14–16。
- Section E Services and equipment：E1 Fire fighting equipment、E2 Smoke hazard management、E3 Lift installations、E4 Visibility in an emergency, exit signs and warning systems；Specifications 17–25（17 喷淋、18 不超过 25 m 的 Class 2/3、19 消防控制中心、20 烟感报警、21 排烟、22 排烟排热窗、23 住宅消防系统、24 电梯、25 自发光出口标志）。

---

## 5. 疏散（Part D2）

| 项目 | 要求 | 条款 | 来源 |
|---|---|---|---|
| 最少出口 | 每层至少 1 个出口；effective height > 25 m 的 Class 2–8 建筑，每层至少 2 个出口（另加 horizontal exit） | D2D3(1)(2) | [S17] |
| 地下室 | 从某层疏散需要在楼内竖向上升超过 1.5 m 时，至少 2 个出口；除非该层面积 ≤ 50 m² 且到单一出口的距离 ≤ 20 m | D2D3(3) | [S17] |
| 不穿过别人的 SOU | 每个人都能不穿过其他 SOU 到达出口（需要 2 个出口时到达 2 个） | D2D3(7) | [S17] |
| 何时须用防火隔离楼梯（Class 2） | 作为必需出口的楼梯，连接、穿过或经过超过 3 个连续楼层时必须防火隔离；满足条件可多算一层（只停车或附属用途、全楼喷淋、或按规定 FRL 分隔） | D2D4(1) | [S17] |
| 何时须用防火隔离楼梯（Class 5–9） | 超过 2 个连续楼层必须防火隔离，条件同上可多一层 | D2D4(2) | [S17] |
| 疏散距离 Class 2/3 | SOU 入户门到出口（或到可向两个出口分头疏散的点）不超过 6 m；或到底层直通道路/空地的单一出口不超过 20 m；不在 SOU 内的房间，任一点到出口不超过 20 m | D2D5(1) | [S17] |
| 疏散距离 Class 5–9 | 任一点到出口不超过 20 m，或到可向两个出口分头疏散的点不超过 20 m 且到其中一个出口不超过 40 m；Class 5/6 在通往道路层的单一出口可放宽到 30 m | D2D5(3) | [S17] |
| 出口间距 | 互为替代的出口之间不少于 9 m；Class 2/3 不超过 45 m，其他一般不超过 60 m；两条疏散路线不能汇合到间距小于 6 m | D2D6 | [S17] |
| 其他 | 出口宽度 D2D8、门宽 D2D9、经防火出口的疏散 D2D12、出口排放 D2D15、人数计算 Table D2D18（例如混合用途小面积部分仍按实际用途计人数）| D2D7–D2D18 | [S17][S7] |

**高层 Class 2 的常见格局**：25 m 以上必须每层 2 部楼梯（D2D3），全部防火隔离（D2D4），且服务 25 m 以上楼层的楼梯要加压（E2D4）。很多布里斯班高层公寓为了提高得房率，用 Performance Solution 论证「单楼梯 + 其他补偿措施」或延长疏散距离——这类方案必须由 fire engineer 做 FER，并按昆州规定转介 QFR（见第 9 节和另一篇文件）。单楼梯方案在昆州是否有具体政策限制：待证实。

---

## 6. 无障碍（Part D4 + Premises Standards）

- **D4D2(4) Class 2 的要求（全国条文）**[S19]：
  - 从需要无障碍的人行入口，到至少 1 个有 SOU 的楼层，并到该层每个 SOU 的入户门；
  - 到达并进入每类公共用房中的至少 1 个（厨房、桑拿、健身房、泳池、公共洗衣房、游戏室、商铺、就餐区等）；
  - 如果装了符合 AS 1428.1 的坡道或客梯：要到达电梯/坡道所服务楼层上每个 SOU 的入户门，以及公共用房。
  - 「20 套以上须有 5% 无障碍单元」是 **SA 的州变体**，不适用于昆州 [S19]。
- D4D2(6)：Class 5、6 建筑——所有日常使用区域都要无障碍；D4D2(7)：Class 7a——到达并进入有无障碍车位的楼层 [S19]。
- D4D6：无障碍车位按 AS/NZS 2890.6；Class 5 等按每 100 个车位 1 个（不足 100 按 100 计），Class 6 在 1000 个车位以内按每 50 个 1 个 [S19]。Class 2 停车的无障碍车位数量：NCC 原文按「需要无障碍的建筑」处理，具体如何计算待证实。
- 其他：D4D7 标识、D4D8 助听系统、D4D9 触觉指示、D4D12 坡道、E3D7/E3D8 电梯无障碍功能 [S19][S15]。
- **Premises Standards**：Disability (Access to Premises — Buildings) Standards 2010 是联邦标准，NCC Part D4 与其一致；G7D2 的解释性说明明确提到 Class 2 的入户无障碍通道已由 Part D4 和 Premises Standards 处理 [S20]。Premises Standards 原文（legislation.gov.au）本轮无法访问，其适用范围（主要针对公共部分）的细节：待证实。
- **Livable housing（G7D2）**：Class 2 每个 SOU 都须符合 ABCB Standard for Livable Housing Design（第 1 部分除外）[S20]。昆州自 2023-10-01 起实施 Livable housing（见 `NCC现行版本与住宅要求.md`）；对 Class 2 是否有昆州特殊安排：待证实。

---

## 7. 能效（Section J）

| 项目 | 要求 | 条款 | 来源 |
|---|---|---|---|
| 性能要求 | J1P1 能源使用（Class 3、5–9 及 Class 2 公共区）；J1P2 Class 2 SOU 热性能；J1P3 Class 2 SOU 能源使用（暖通、热水、照明等 domestic services）；J1P4 可再生能源与电动车充电 | J1P1–J1P4 | [S21] |
| 验证方法 | J1V1 NABERS Energy、J1V2 Green Star、J1V3 参照建筑法、J1V4 气密性验证、J1V5 Class 2 SOU 参照建筑法 | J1V1–J1V5 | [S21] |
| **Class 2 公寓热性能（NatHERS）** | 全部 SOU **平均不低于 7 星**，且**每户不低于 6 星**，两者都要满足单独的供暖、制冷负荷限值；用 house energy rating software 和 ABCB Standard for NatHERS Heating and Cooling Load Limits 计算 | J3D3 | [S22] |
| Class 2 其他 DtS | 吊扇 J3D4、屋面/外墙热桥 J3D5/J3D6、楼板边保温 J3D10、气密 Part J5 | J3D4–J3D13 | [S22] |
| Class 2 全屋能源（Whole of Home） | SOU 的 net equivalent energy usage 不超过允许值（J3D14），或用 home energy rating software 计算（J3D15） | J3D14、J3D15 | [S22] |
| 非住宅部分 | Class 5/6/7a 和 Class 2 公共区按 Part J4（围护）、J5（气密）、J6（暖通与通风）、J7（照明与电源）、J8（热水）、J9（能源监测和分布式能源）| J4–J9 | [S6] |
| 昆州 | Class 2 能效同时受 QDC MP 4.1 约束 [S5]；昆州 7 星生效日期（2024-05-01）见 `NCC现行版本与住宅要求.md`，MP 4.1 对 Class 2 的具体内容待证实 | — | [S5] |

---

## 8. 隔声（Part F7）、防水（F1、F2）和冷凝（F8）

### 8.1 隔声——NCC 2022 是 Part F7（2019 版是 Part F5）[S23]
NCC 2022 中 Part F5 是「Room heights」，隔声是 **Part F7 Sound transmission and insulation**，原 2019 版编号为 F5.x [S6][S23]。
- F7D2：DtS 适用于 Class 2、3 和 Class 9c [S23]。
- **楼板（F7D5）**：分隔 SOU，或分隔 SOU 与机房、电梯井、楼梯、公共走廊、公共大堂或不同类别部分的楼板，Rw + Ctr（空气声）**不小于 50**，Ln,w（撞击声）**不大于 62** [S23]。
- **墙（F7D6）**：SOU 之间 Rw + Ctr 不小于 50；SOU 与机房、电梯井、楼梯、公共走廊等或不同类别之间 Rw 不小于 50；卫生间/洗衣房/厨房与相邻单元居室之间、SOU 与机房或电梯井之间的墙还要满足 F7D4(2)（撞击声的构造要求）；SOU 通向公共走廊的门组件 Rw 不小于 30；隔声墙要做到上层楼板底面或满足隔声要求的吊顶 [S23]。
- **管道（F7D7）**：穿过或服务多个 SOU 的风管、污废水管、给水管，与居室之间的构造 Rw + Ctr 不小于 40，与厨房或非居住房间之间不小于 25 [S23]。
- F7D8：水泵的隔振 [S23]。
- 昆州另有 QDC MP 4.4（交通噪声走廊建筑）：本轮未核对，待证实是否适用于 Class 2。

### 8.2 防水
- **F1D5 外部防水**：屋面、阳台、podium 或类似水平面必须设防水层，材料符合 AS 4654.1，设计和施工符合 AS 4654.2 [S24]。
- **F2D2 湿区**：Class 2、3 和 Class 4 部分的湿区构件须按 Specification 26 做到防水或耐水，并符合 AS 3740；Class 5–9 的浴室、淋浴间、洗衣房、卫生间等也按 Specification 26 [S25]。AS 3740 的版本（2010 或 2021）按 NCC 2022 Schedule 2 参考文件为准：待证实（见 `住宅相关澳大利亚标准清单.md`）。
- F1D6、F1D7：防潮和地面楼板防潮；地下室外防水本身 NCC DtS 规定很少，主要靠设计和 AS 等标准（见施工类文件）[S24]。

### 8.3 冷凝（Part F8）
- F8D2：DtS 只适用于 **Class 2 的 SOU** 和 Class 4 部分 [S26]。
- F8D3：外墙如用 pliable building membrane，须符合 AS 4200.1 并按 AS 4200.2 安装，放在主保温层外侧；对气候区 4、5 和 6–8 有透汽率下限（布里斯班属于气候区 2，透汽率下限条款不适用，但膜的位置要求仍适用）；不用透气膜时（单层砌体、单层混凝土除外），主防水层与怕水材料之间要有排水空腔 [S26]。布里斯班气候区为 2：据 ABCB 气候区地图，待证实具体地块。
- F8D4：厨房、浴室、卫生间、洗衣房排风量（浴室/卫生间 25 L/s，厨房/洗衣房 40 L/s），须直接或经竖井/风管排到室外；非连续运行且没有自然通风的浴室排风扇须与灯联动并延时 10 分钟 [S26]。
- F8D5：屋面空间通风 [S26]。

---

## 9. DtS、Performance Solution 与 fire engineering 流程

### 9.1 合规路线（Part A2）[S27]
- A2G1：满足 Performance Requirements 的路线有三种：Performance Solution、Deemed-to-Satisfy Solution、两者组合。Performance Requirements 是 NCC 中唯一必须满足的技术条款。
- **A2G2(1)**：Performance Solution 须证明 (a) 满足全部相关 Performance Requirements，或 (b) 至少等同于 DtS。
- **A2G2(2) 评估方法**：Part A5 的适用性证据；Verification Method（NCC 中的或经主管机关接受的其他方法）；Expert Judgement；与 DtS 比较。可组合使用。
- **A2G2(3)**：确定相关 Performance Requirements——本 Section/Part 的，以及其他 Section/Part 中受影响的。
- **A2G4**：DtS 与 Performance Solution 组合时，先找出被替代的 DtS 条款，再找出对应的 Performance Requirements，以及其他受影响的 Performance Requirements。

### 9.2 Performance Solution 的法定四步（A2G2(4)）[S27]
1. 与相关各方协商，编写 **performance-based design brief（PBDB）**；
2. 按 PBDB 进行分析；
3. 按 PBDB 中的验收标准评价分析结果；
4. 编写最终报告，内容包括：所有相关 Performance Requirements 和/或 DtS 条款、使用的评估方法、第 1–3 步的细节、确认满足 Performance Requirement 的结论、使用条件和限制。

### 9.3 Fire engineering 在高层项目中的实际做法（昆州）
- 消防方面的 Performance Solution 通常由 fire safety engineer 编写 fire engineering brief（即 PBDB）和 fire engineering report（FER）。昆州 fire safety engineer 须是 RPEQ（Professional Engineers Act 2002 (Qld)）：待证实具体要求。
- 涉及 special fire services，或消防系统采用按 NCC Volume One Performance Requirements 评估的方案时，建筑许可申请必须转介 Queensland Fire and Rescue（QFR，法规用名；业主所说的 QFD/原 QFES 体系）。按 Planning Regulation 2017 Schedule 9 Part 3 Division 3 Table 1，QFR 在此是 **advice agency（只能给建议）**，不是有约束力的 concurrence agency——详见 `高层建筑-规划审批与消防审查.md` 第 4 节。
- 常见消防 Performance Solution：延长疏散距离、减少出口数、外墙开口竖向分隔（C3D7）的替代、FRL 降低、取消部分防火门或防火卷帘等。每一项都会在 FER 中列明对应的 DtS 偏离、Performance Requirement（如 C1P1–C1P9、D1P4、E1P3、E2P2）和补偿措施。
- 竣工时，certifier 要确认 Performance Solution 的条件（例如维护要求）被纳入 fire safety installations 的维护制度（Building Fire Safety Regulation / Fire Safety Regulation 的 occupier 维护义务）：待证实细节。

---

## 10. 给 builder 的检查清单（看图时）

1. 先算 rise in storeys（C2D3）和 effective height（定义）：确认 Type A，以及是否超过 25 m、75 m。
2. 列出每层的类别，核对类别之间的分隔（C3D9、C3D10）和 FRL 表（S5C11a–g）。
3. 核对外墙所有构件是否不燃（C2D10），重点是保温、龙骨、防水透气膜、饰面板。
4. 核对楼梯数量和防火隔离（D2D3、D2D4）、疏散距离（D2D5、D2D6）、楼梯加压（E2D4）。
5. 核对消防设备：喷淋（E1D5）、消火栓（E1D2）、烟感（E2D5）、应急电梯（E3D5）、EWIS（E4D9）、消防控制中心（E1D15）。
6. 核对施工期消防（E1D16）：effective height 达到 12 m 后，消火栓/卷盘随楼层推进（最上 2 层除外）——这条直接影响施工进度和临时消防管的安排。
7. 核对隔声（F7D5–F7D7）、防水（F1D5、F2D2）、冷凝（F8D3、F8D4）、NatHERS（J3D3 平均 7 星、单户 6 星）。
8. 找出图纸中所有 Performance Solution，确认有 FER、QFR 建议和 certifier 的批准条件。

---

## 来源
- [S1] Business Queensland / Queensland Government，NCC 2025 在昆州的采用安排（见 `NCC现行版本与住宅要求.md` 来源 S1），https://www.business.qld.gov.au/industries/building-property-development/building-construction/laws-codes-standards ，日期见该文件，访问 2026-11-20。
- [S2] ABCB，NCC 2025 state and territory adoption information，https://ncc.abcb.gov.au/ncc-2025-state-and-territory-adoption-information ，日期未标明，访问 2026-11-20（昆州：2027-05-01）。
- [S3] Building Act 1975 (Qld) s36、s37，https://www.legislation.qld.gov.au/view/html/inforce/current/act-1975-011 ，现行版，访问 2026-11-20（核对见 `NCC现行版本与住宅要求.md`）。
- [S4] ABCB，NCC 2022 Volume One，Schedule 7 Queensland 目录，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/7-queensland ，访问 2026-11-20。
- [S5] ABCB，NCC 2022 Volume One，QLD Footnote: Other legislation affecting buildings，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/7-queensland/qld-footnote-other-legislation-affecting-buildings ，访问 2026-11-20。
- [S6] ABCB，NCC 2022 Volume One Online（目录），https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one ，访问 2026-11-20。
- [S7] NCC 2022 Volume One，Part A6 Building classification，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/a-governing-requirements/part-a6-building-classification ，访问 2026-11-20。
- [S8] NCC 2022 Volume One，Part C2 Fire resistance and stability，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/c-fire-resistance/part-c2-fire-resistance-and-stability ，访问 2026-11-20。
- [S9] NCC 2022 Volume One，Part C3 Compartmentation and separation，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/c-fire-resistance/part-c3-compartmentation-and-separation ，访问 2026-11-20（仅核对条款标题）。
- [S10] NCC 2022 Volume One，Specification 5 Fire-resisting construction，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/c-fire-resistance/5-fire-resisting-construction ，访问 2026-11-20。
- [S11] NCC 2022 Volume One，Specification 8 Performance of external walls in fire，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/c-fire-resistance/8-performance-external-walls-fire ，访问 2026-11-20（已下载，未逐条摘录）。
- [S12] NCC 2022 Volume One，Part A5 Documentation of design and construction，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/a-governing-requirements/part-a5-documentation-design-and-construction ，访问 2026-11-20（核对条款标题 A5G1–A5G9）。
- [S13] NCC 2022 Volume One，Schedule 1 Definitions – Glossary（Effective height、Open-deck carpark、Performance Solution、Rise in storeys），https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/1-definitions/glossary ，访问 2026-11-20。
- [S14] NCC 2022 Volume One，Part E1 Fire fighting equipment，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/e-services-and-equipment/part-e1-fire-fighting-equipment ，访问 2026-11-20。
- [S15] NCC 2022 Volume One，Part E3 Lift installations，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/e-services-and-equipment/part-e3-lift-installations ，访问 2026-11-20。
- [S16] NCC 2022 Volume One，Part E2 Smoke hazard management，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/e-services-and-equipment/part-e2-smoke-hazard-management ，访问 2026-11-20。
- [S17] NCC 2022 Volume One，Part D2 Provision for escape，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/d-access-and-egress/part-d2-provision-escape ，访问 2026-11-20。
- [S18] NCC 2022 Volume One，Part E4 Visibility in an emergency, exit signs and warning systems，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/e-services-and-equipment/part-e4-visibility-emergency-exit-signs-and-warning-systems ，访问 2026-11-20。
- [S19] NCC 2022 Volume One，Part D4 Access for people with a disability，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/d-access-and-egress/part-d4-access-people-disability ，访问 2026-11-20。
- [S20] NCC 2022 Volume One，Part G7 Livable housing design（含 G7D2 解释性说明提及 Premises Standards），https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/g-ancillary-provisions/part-g7-livable-housing-design ，访问 2026-11-20。
- [S21] NCC 2022 Volume One，Part J1 Energy efficiency performance requirements，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/j-energy-efficiency/part-j1-energy-efficiency-performance-requirements ，访问 2026-11-20。
- [S22] NCC 2022 Volume One，Part J3 Elemental provisions for a sole-occupancy unit of a Class 2 building or a Class 4 part of a building，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/j-energy-efficiency/part-j3-elemental-provisions-sole-occupancy-unit-class-2-building-or-class-4-part-building ，访问 2026-11-20。
- [S23] NCC 2022 Volume One，Part F7 Sound transmission and insulation，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/f-health-and-amenity/part-f7-sound-transmission-and-insulation ，访问 2026-11-20。
- [S24] NCC 2022 Volume One，Part F1 Surface water management, rising damp and external waterproofing，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/f-health-and-amenity/part-f1-surface-water-management-rising-damp-and-external-waterproofing ，访问 2026-11-20。
- [S25] NCC 2022 Volume One，Part F2 Wet areas and overflow protection，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/f-health-and-amenity/part-f2-wet-areas-and-overflow-protection ，访问 2026-11-20。
- [S26] NCC 2022 Volume One，Part F8 Condensation management，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/f-health-and-amenity/part-f8-condensation-management ，访问 2026-11-20。
- [S27] NCC 2022 Volume One，Part A2 Compliance with the NCC，https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-one/a-governing-requirements/part-a2-compliance-ncc ，访问 2026-11-20。

## 待证实清单（本文）
1. Class 5、6、7a、9 在 Part A6 中的具体条款号（A6G6–A6G10 的对应关系）。
2. Specification 8（外墙防火性能）的具体验收标准。
3. QDC MP 4.1 对 Class 2 能效的现行要求；QDC MP 4.4 是否适用于本项目。
4. Premises Standards 原文的适用范围细节；Class 2 附属停车的无障碍车位数量算法。
5. 昆州对 Class 2 Livable housing 有无特殊安排；昆州对单楼梯高层 Performance Solution 有无政策限制。
6. AS 3740 在 NCC 2022 Volume One 中引用的版本。
7. 昆州 fire safety engineer 的 RPEQ 要求；Performance Solution 维护条件如何纳入法定维护制度。
