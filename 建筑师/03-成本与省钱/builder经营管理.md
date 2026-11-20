# builder经营管理

## 摘要
本文从持证昆州 builder 的经营角度，整理开公司、接项目必须管好的几件事：要买哪些保险、怎样报价、怎样管现金流和 retention（保留金）、GST 怎么登记和开票、新住宅出售时买方代扣 GST 的规则、QLeave 培训/长期服务假/安全三项 levy、账簿要保存多少年，以及 QBCC 和 ASIC 资料里 builder 倒闭的常见原因。法定数字都按法律原文核对过，并标了条款号。业主也能用本文判断 builder 的经营是否健康：签约前查 QBCC 执照和财务类别，核对合同保险条款，付款时注意 retention 和进度款比例。查不到原文的内容（ATO 网页、WorkCover Queensland 网页、QLeave 网页、ASIC 统计 Excel、行业利润率）都标了「待证实」。

适用州：QLD（GST、记账为联邦规定，全国适用）｜资料核对日期：2026-11-21｜状态：部分待证实（法律原文、QBCC 网页和合同已核实；ATO、WorkCover Queensland、QLeave 网页及行业利润率未能打开或没有权威来源）

> **核对方式**：本文在 2026-11-21 直接打开以下原文核对：Federal Register of Legislation（GST Act、GST Regulations、Taxation Administration Act、Corporations Act 的现行汇编本）、Queensland Legislation（QBCC Act、Workers' Compensation and Rehabilitation Act、Portable Long Service Leave Act 及 Regulation）、QBCC 网页和 QBCC New Home Construction Contract PDF、ASIC 网页。**www.ato.gov.au（Akamai 返回 Access Denied）、www.qleave.qld.gov.au 和 www.worksafe.qld.gov.au（Cloudflare 人机验证）在本会话无法打开**，所以 ATO 的操作性说明（表格名、网上申报流程）只能依据法律条文，标「待证实」。

---

## 一、builder 要买的保险

| 险种 | 是否强制 | 依据与要点 | 状态 |
|---|---|---|---|
| **Workers' compensation（工伤保险）** | **强制**（雇用 worker 的雇主） | Workers' Compensation and Rehabilitation Act 2003 (Qld) s48(1)：每个雇主必须为其雇用的每个 worker 投保，并保持有效，承保雇主对工伤的**法定赔偿责任**和**损害赔偿责任**；s48(3)：必须通过自保执照（self-insurer）或 **WorkCover 保单**承保；s48(4)：WorkCover 对每个雇主只出一张保单 [S8] | ✅ 已核实（法律原文） |
| └ 谁算 worker | — | s11(1)(a)：按合同工作、并且就 PAYG withholding（TAA 1953 Sch 1 Part 2-5）而言属于「employee」的人，就是 worker [S8]。**所以有些以 ABN 干活的分包人，在法律上仍可能被认定为 worker**，builder 要逐个判断 | ✅ 已核实；具体判断标准（WorkCover 的 worker 判定工具）待证实 |
| └ 保费费率、申报时间 | — | WorkCover Queensland 网站（www.worksafe.qld.gov.au）本会话打不开 | **待证实** |
| **Contract works（工程一切险）** | 法律不强制；**QBCC 标准合同强制** | QBCC New Home Construction Contract（Version 3，2023-07）Condition 12.1(c)：builder 自费投保 contract works，保额**不低于合同价**，保到 Practical Completion 当日下午 4 点；保单须以业主和 builder 双方为被保险人 [S7] | ✅ 已核实（合同原文） |
| **Public liability（公众责任险）** | 法律不强制；**QBCC 标准合同强制** | 同 Condition 12.1(c)：公众责任险**不低于 1,000 万澳元**，保到 builder 履行完 Condition 29（缺陷整改）义务当日下午 4 点；12.2：须含交叉责任条款，保险人放弃对共同被保险人的代位求偿权；12.3：开工前或业主要求时，builder 须出示保单有效的书面证明 [S7] | ✅ 已核实（合同原文） |
| **Home warranty（QBCC 家庭保修保险）** | **强制**（住宅工程超过 $3,300） | 同 Condition 12.1(b)：保费由 builder 向业主收取，在签约后 10 个工作日内或开工前（取较早者）交给 QBCC [S7]。详见 `01-法规标准/QBCC家庭保修保险.md` | ✅ 已核实 |
| **Professional indemnity（职业责任险）** | 对 builder **一般不是执照条件**（待证实） | QBCC 网页只提到：某些行业的承包商如持有职业责任险，可豁免 Minimum Financial Requirements（MFR）；持有豁免类执照但 QBCC 没有其有效 PI 保单副本的，仍须满足 MFR [S12][S14]。哪些执照类别属于豁免类，以及设计施工一体（design & construct）的 builder 是否需要 PI，本次没有找到原文 | **待证实** |

**经营建议（builder 视角）**
- 投标前把保险费计入 preliminaries（前期费用）。QBCC 合同要求的保额（contract works ≥ 合同价，public liability ≥ $10M）是**最低要求**，项目大或有邻近建筑风险时应向保险经纪确认是否加保。
- 分包合同里要求分包人出示自己的 public liability 和 workers' compensation（或个人意外险）证明，并在开工前存档。
- **业主核查要点**：开工前向 builder 要 contract works 和 public liability 保单的有效证明，这是 QBCC 合同 Condition 12.3 给业主的权利 [S7]。

---

## 二、报价与投标流程

### 1. 一般流程（行业通行做法，供参考）
1. **读招标文件**：图纸、规格书（specification）、合同条件、PC/PS 清单、工期要求。
2. **算量（quantity take-off）**：按构件逐项算量，见 `05-工具与模板/工程量计算表.xlsx` 和 `03-成本与省钱/成本估算方法.md`。
3. **询价**：向分包人和供应商发询价（每个主要工种通常询多家），比较报价时检查范围是否一致（包含项、不包含项、是否含 GST）。
4. **组成直接成本**：材料 + 人工 + 分包 + 设备。
5. **加 preliminaries（前期/现场管理费）**：现场管理人员、临时设施、围挡、保险、审批与认证费、清运等（项目清单见 `成本估算方法.md`）。
6. **加 overhead（公司管理费）和 margin（利润）**：见下文。
7. **加 GST**：住宅合同价通常含 GST（QBCC 合同进度款表头即写「all prices incl. GST」）[S7]。
8. **内部审核和风险评估**：价格、工期、合同风险、现金流（见第三节）。

### 2. margin 和 overhead 的构成
- **overhead（公司管理费）**：办公室租金、办公室人员工资、车辆、软件、会计和法律费、执照费、公司层面的保险等不能直接计入某个项目的费用。
- **margin（利润）**：在全部成本之上为承担风险和取得回报而加的部分。
- **比例**：在本次能访问的官方来源（QBCC、ABS、法律库）中**没有找到住宅 builder overhead 或 margin 的权威百分比**。网上常见的「x%–y%」说法多来自 builder 或咨询公司网站，不符合本知识库的来源要求——**待证实**。业主不要用某个「行业平均利润率」去压价，应该比较的是范围一致的完整报价。
- **QBCC 合同 PC/PS 超支加价**：PC/PS 超出部分 builder 可加收的比例按合同附表约定，是否有法定上限见 `03-成本与省钱/常见超支原因.md`（该文标为待确认）。

### 3. 报价必须守住的财务红线：QBCC MFR
QBCC Minimum Financial Requirements（MFR）是执照条件，必须**随时**满足 [S12]：
- **Current ratio（流动比率）≥ 1:1**：每 $1 流动负债至少要有 $1 流动资产；营业额超过 $800,000 的，须由认可的独立会计师在 MFR 报告中计算该比率，并显示报告期末日（例如 6 月 30 日）达标 [S13][S15]。（「不得四舍五入凑到 1:1」的说法只见于搜索摘要，本次打开的页面未见原句——待证实。）
- **Net tangible assets（净有形资产，NTA）≥ $0** [S15]。
- **NTA 要足以支撑营业额**：执照按「maximum revenue（最高年营业额）」分财务类别。QBCC 页面列出：SC1 最高营业额 $200,000、NTA 至少 $12,000（**builder 类执照不能选 SC1**）；SC2 最高营业额 $800,000、NTA 至少 $46,000；Categories 1–3 最高营业额 $30,000,000；Categories 4–7 为 $30,000,001 以上 [S14]。QBCC 示例：NTA $250,000 可支持超过 $5.6 百万的营业额；只想要 $3,000,000 营业额时，会计师可在报告中写 NTA「至少 $156,000」[S14]。
- **触发报告的事件**：营业额超过上次核定 maximum revenue **10% 以上**；NTA 比上次核定值下降超过 **30%**（SC1、SC2 和 Categories 1–3）或超过 **20%**（Categories 4–7）；业务结构或董事变更等 [S14][S15]。
- **年度报告**：多数 Category 1–7 执照人在每年 **12 月 31 日**前提交；SC1、SC2 公司执照人在每年 **3 月 31 日**前提交；SC1、SC2 个人执照人的年度报告要求已于 2025 年 3 月取消 [S15]。
- MFR 还要求编制**季度管理报表**（quarterly management accounts），QBCC 说明这是检查利润率、确认合同仍然盈利、及时付款给分包和供应商的工具 [S15]。

> 对报价的含义：接一个大合同前，先算这个合同会不会让年营业额超出执照 maximum revenue 的 10% 以上，以及前期垫资会不会让 current ratio 低于 1:1。

---

## 三、现金流管理

### 1. 收款端：业主付给 builder
- QBCC 新建住宅合同 Option A 进度款（含 GST）：定金 5%，Base 15%，Frame 20%，Enclosed 25%，Fixing 20%，Practical Completion 15% [S7]。
- **比例必须与进度相称**：合同对 builder 的警告写明，QBCC Act 要求进度款与现场工程进度直接相关、与工程价值成比例；例如在现场完成的工程超过 50% 之前，已付定金加进度款总额不得超过合同价的 50%；违者重罚 [S7]。
- 业主须在收到进度款请求后 **5 个工作日内**核对并支付有效请款（合同业主检查清单，GC 19.1）[S7]。

### 2. 付款端：builder 付给分包人
- **分包合同受 QBCC Act Part 4A 管辖**：Part 4A 的「building contract」不包括 domestic building contract（s67AAA）[S9]；但 Schedule 1B s3(2)(a) 规定，building contractor 与 subcontractor 之间的合同**不是** domestic building contract [S9]。因此住宅项目的分包合同也适用 Part 4A。
- **最长付款期**：subcontract（或 construction management trade contract）里约定在付款请求提交后**超过 25 个工作日**才付进度款的条款无效（s67U）；commercial building contract 的上限为 **15 个工作日**（s67W）。计算工作日时不算周六日、公众假期和**每年 12 月 22 日至次年 1 月 10 日** [S9]。

### 3. 时间差与资金缺口（builder 经营要点）
- 收款按阶段（例如 Frame 阶段完成才能请款 20%），而材料、人工和分包费在阶段内持续发生，builder 通常要先垫付一个阶段的成本。QBCC 合同 5 个工作日的业主付款期与分包合同最长 25 个工作日的付款期之间，形成可以利用的时间差，但**不得因此拖欠分包人到期款项**。
- 做法：每个项目做**现金流预测表**（按周列收入、支出、累计余额），每次请款前检查应付分包款；不要用新项目的定金填补旧项目的亏空（这是 ASIC 资料里「现金流不足」类倒闭的典型路径，见第七节）。
- 项目信托账户（project trust）和 retention trust 的门槛与豁免见 `01-法规标准/` 付款与信托文件 `付款与信托账户规定.md`（少于 3 个居住单元的住宅工程豁免）。

### 4. Retention（保留金）与 security（担保）——QBCC Act Part 4A
| 规则 | 内容 | 条款 |
|---|---|---|
| 实际完工前上限（业主/SPV 对总包） | 保留金加担保合计**不超过合同价 5%**；但书面合同经解释、明确排除并由双方草签时可不受此限 | s67K [S9] |
| 实际完工前上限（分包） | 保留金加担保合计**不超过分包合同价 5%** | s67L [S9] |
| 每期扣留上限 | 每次付款扣留的保留金**不超过该次应付款的 10%** | s67M [S9] |
| 实际完工后上限 | 保留金加担保合计**不超过合同价 2.5%**（只限于用于整改缺陷责任期内发现的缺陷） | s67N [S9] |
| 法定缺陷责任期 | 合同没有约定释放期限的，保留金或担保须在**实际完工之日起 12 个月**届满时释放 | s67NA [S9] |
| 不按时释放的处罚 | 无合理理由不按合同释放保留金或担保，最高 **200 penalty units 或 1 年监禁** | s67NB [S9] |
| 动用保留金抵债 | 须书面通知对方拟动用的金额；通知须在知道或应当知道有权追讨后 **28 天内**发出 | s67J [S9] |
| 以担保换回现金保留金 | 被扣方可提交等值政府债券或认可担保机构的担保，换回现金保留金 | s67T [S9] |

> 注意：Part 4A 不适用于 builder 与业主之间的 domestic building contract（s67AAA）[S9]；住宅业主合同一般不扣 retention，而是按阶段付款加 12 个月缺陷责任期（见 `CLAUDE.md` 关键结论）。

---

## 四、GST

### 1. 登记门槛
- 经营企业（carrying on an enterprise）且 **GST turnover 达到登记门槛**的，必须登记 GST（GST Act s23-5）[S1]。
- 门槛：GST Act s23-15(1) 规定为 $50,000「或法规规定的更高金额」[S1]；**A New Tax System (Goods and Services Tax) Regulations 2019 s23-15.01 规定为 $75,000**（非营利机构 $150,000，s23-15.02）[S3]。
- 必须在**成为应登记之日起 21 天内**申请登记（GST Act s25-1）[S1]。
- 营业额未达门槛的也可以自愿登记（s23-10）[S1]。

### 2. 进度款开票与 GST 归属期
- **一般规则（非现金制）**：一项应税供应的 GST 归属到**先发生者**所在的申报期：收到任何价款，或在收款之前开出发票（s29-5(1)）[S1]。
- **现金制**：只按实际收到的价款归属（s29-5(2)）；能否选现金制见 s29-40（小企业实体等）[S1]。
- **分期/进度供应**：按进度或分期提供、价款也按进度或分期支付的应税供应，**每一期视为一项单独供应**来确定 GST 归属（s156-5）[S2]。所以每次进度款请款单都要单独作为 tax invoice 处理。
- builder 实务：按非现金制的 builder，**开出进度款发票的那个申报期就要交这部分 GST**，即使业主还没付款——这是现金流压力的来源之一。tax invoice 的格式要求见 ATO 页面——**待证实**（ATO 网站本会话无法打开）。

### 3. 新住宅销售的 GST withholding（买方代扣）
适用于 builder 自建自售（spec home）或开发商卖楼花/现房：
- **义务人是买方**：买方取得「new residential premises」（不是经 substantial renovations 形成的、也不是 commercial residential premises）或特定 potential residential land 的应税供应时，须向 ATO 支付一笔款项（Taxation Administration Act 1953 Sch 1 s14-250(1)–(2)）[S4]。
- **金额**（s14-250(6)–(8)）[S4]：
  - 采用 margin scheme 的：部长另有规定的百分比（只能在 7% 以上、不超过 9%）；**没有规定的为合同价的 7%**；
  - 其他情况：**合同价的 1/11**；
  - 与关联方之间无对价或低于含 GST 市值的：GST-exclusive 市值的 10%（s14-250(9)）。
  - 部长是否已按 s14-250(8) 规定高于 7% 的比例：本次没有查到——**待证实**（需查 ATO 页面或 legislation.gov.au 上的相关 determination）。
- **付款时间**：在首次支付价款（**不含定金**）之日或之前，通常即交割日（s14-250(4)）[S4]。
- **卖方（builder/开发商）的书面通知义务**：卖方在出售任何 residential premises 或 potential residential land 之前，必须书面通知买方是否需要代扣；需要代扣的，要写明负责交 GST 的实体名称和 ABN、代扣金额、支付时间等（s14-255(1)）；**不通知是严格责任罪**（s14-255(4)）；但卖方没通知不影响买方的代扣义务（s14-255(3)）[S4]。
- ATO 的申报表格（俗称 Form one / Form two）和网上操作流程——**待证实**（ATO 网站无法打开）。

---

## 五、QLeave 缴费（Building and Construction Industry (Portable Long Service Leave) Act 1991 (Qld)）

| 项目 | 内容 | 依据 |
|---|---|---|
| 三项 levy | 建筑业培训 levy、长期服务假 levy、工作健康安全 levy | Act s66 [S10] |
| 费率 | 培训 levy **0.1%**、长期服务假 levy **0.35%**、WHS levy **0.125%**（合计 0.575%）按工程造价计 | Regulation 2024 s8 [S11] |
| 门槛 | 工程造价**低于 $150,000** 不须交 levy；造价不含 GST | Regulation 2024 s7(1)；Act s73(1)（见 Regulation 注释）[S11] |
| 谁交 | 需要 development permit 的：**申请人**；需要管道排水许可的：申请人；其他：**委托工程的人**（政府、联邦工程另有规定） | Act s74 [S10] |
| 什么时候交 | 在 building/plumbing/operational work 的 development permit 发出**之前**；不需要许可的，在**开工前**；QLeave 可书面批准延后，或按 s82 分期 | Act s75 [S10] |
| 申报 | 须向 QLeave 或其代理提交指定表格（时间同上）；实际造价比申报额高出 **$50,000 以上**的，须在完工后 **30 天内**通知并补交 | Act s67 [S10] |

- 实务上 certifier 在发 building approval 前通常要看到 QLeave 缴费收据（这是 s75「permit 发出之前交」的结果）。业主自建住宅超过 $150,000 时，如果业主是申请人，levy 由业主交——签合同时要写清楚由谁交、是否已含在合同价里。
- 引用的 Regulation 为 2024 年版本（Queensland Legislation 显示「Current as at 23 August 2024」），之后有无修订**待证实**；QLeave 网站本会话无法打开，网上缴费流程和计算器**待证实**。

---

## 六、记账和文件保存年限

| 记录 | 保存期限 | 依据 |
|---|---|---|
| 与 GST 相关的交易记录（应税供应、可抵扣采购等） | 交易完成后 **5 年**，或税务评估复审期（如更长）；评估被修改的，按刷新的 4 年复审期 | Taxation Administration Act 1953 Sch 1 s382-5(1) [S5] |
| 公司财务记录 | 交易完成后 **7 年** | Corporations Act 2001 s286(2)（适用于公司）[S6] |
| 所得税记录（个人和企业） | 通常 5 年（ITAA 1936 s262A）——本次未打开该条原文 | **待证实** |
| 工资和雇员记录 | Fair Work 规定通常 7 年——本次未核对 | **待证实** |
| QBCC 执照人的项目文件（合同、变更、检查证书等） | 法定保存年限本次未查到；建议至少覆盖结构缺陷保修期（6 年 6 个月，见 `CLAUDE.md`）和诉讼时效 | **待证实** |

建议的项目文件包：合同及附表、所有 variation 书面文件（Form 5）、进度款请款和付款记录、检查证书、分包合同和保险证明、QLeave 收据、home warranty 证明、现场日报和照片、缺陷通知与整改记录。

---

## 七、常见的经营失败原因（QBCC 和 ASIC 资料）

### 1. ASIC 资料
- ASIC 2023 年发布的 2022-23 财年统计（registered liquidators 提交的报告）：**建筑业报告数量最多，占 28%**；每份报告平均列出 3–4 个失败原因；最常见的是**现金流不足或现金消耗过高（52% 的报告）**、「其他」（50%）和**经营亏损（trading losses，49%）**；昆州占报告的 18% [S16]。
- 同一来源：83% 的报告涉及资产 $100,000 以下的公司，82% 员工少于 20 人；96% 的债权人每元只收回 0–11 分 [S16]。对分包人和业主的含义是：小型 builder 倒闭时，债权人基本拿不回钱。
- 按行业细分的失败原因（Series 3.1 Excel，2024-25 财年已发布）放在 download.asic.gov.au，本会话被代理拒绝——**待证实**。

### 2. QBCC 资料
- QBCC 说明：未满足 MFR 的执照人**资不抵债的风险更高**，会给债权人和消费者造成损失 [S12]。
- QBCC 评估执照人风险时使用：年度财务报告；征信机构信息（付款违约、征信查询、ASIC 数据、法院诉讼、供应商账户状态）；QBCC 内部数据（欠款投诉、未完工索赔、缺陷投诉）；举报 [S15]。这些也就是 builder 走向失败前的**预警信号**。
- 公司无力偿还到期债务时，董事依法须委任管理人；个体经营者须进入破产或债务协议；QBCC 无法阻止破产程序，但会对参与过破产事件的执照人、申请人等实施禁止（exclusion）[S12]。

### 3. 归纳（builder 自查清单）
| 失败原因 | 典型表现 | 对策 |
|---|---|---|
| 现金流不足 | 用新项目定金付旧项目欠款；拖欠分包 | 每个项目单独做现金流预测；严格按进度请款 |
| 报价过低、经营亏损 | 漏项、没计 preliminaries/overhead；固定总价合同里材料涨价 | 完整算量；合同写清价格调整条款（如适用）和 PC/PS |
| 超出财务能力扩张 | 营业额超出 MFR 核定额；NTA 下降 | 接单前对照 MFR；按季做管理报表 [S15] |
| 管理不善 | 变更没书面化导致收不到钱；记录缺失 | variation 先书面后施工（QBCC Act Sch 1B s40）；按第六节保存记录 |

---

## 八、对业主（省钱与防风险）的用途
1. 签约前在 QBCC 执照查询中看 builder 的执照类别和财务类别，确认合同价没有超出其 maximum revenue（见第二节第 3 点）。
2. 合同保险条款至少要达到 QBCC 标准合同 Condition 12 的水平，开工前索取保单证明 [S7]。
3. 进度款严格按阶段支付，不要提前付款；「工程不到 50% 时累计付款不超过 50%」是法律要求，不是 builder 的让步 [S7]。
4. 如果是买 builder 的新建现房（spec home），交割前确认卖方已发出 GST withholding 书面通知，并由律师或产权转让人办理代扣 [S4]。

---

## 来源
- [S1] A New Tax System (Goods and Services Tax) Act 1999（Compilation No. 96，汇编日 2026-01-01）s23-5、s23-10、s23-15、s25-1、s29-5、s29-40 — Federal Register of Legislation — https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html — 2026-01-01 — 访问 2026-11-21（已打开原文）
- [S2] 同上 Act 第二部分 s156-5 — https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html — 2026-01-01 — 访问 2026-11-21（已打开原文）
- [S3] A New Tax System (Goods and Services Tax) Regulations 2019（F2019L00417，汇编日 2025-11-01）s23-15.01、s23-15.02 — Federal Register of Legislation — https://www.legislation.gov.au/F2019L00417/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html — 2025-11-01 — 访问 2026-11-21（已打开原文）
- [S4] Taxation Administration Act 1953 Schedule 1 s14-250、s14-255（汇编日 2026-10-01）— Federal Register of Legislation — https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html — 2026-10-01 — 访问 2026-11-21（已打开原文）
- [S5] Taxation Administration Act 1953 Schedule 1 s382-5（汇编日 2026-10-01）— https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html — 2026-10-01 — 访问 2026-11-21（已打开原文）
- [S6] Corporations Act 2001 s286（汇编日 2026-09-19）— Federal Register of Legislation — https://www.legislation.gov.au/C2004A00818/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_2/document_2.html — 2026-09-19 — 访问 2026-11-21（已打开原文）
- [S7] QBCC New Home Construction Contract（PDF，Version 3 – effective from July 2023）Condition 12、业主检查清单（GC 19.1）、Schedule Item 8A — QBCC — https://www.qbcc.qld.gov.au/sites/default/files/documents/template-contract-new-home-construction.pdf — 2023-07 — 访问 2026-11-21（已打开原文）
- [S8] Workers' Compensation and Rehabilitation Act 2003 (Qld) s11、s48 — Queensland Legislation — https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-2003-027 — 现行版本（页面版本日期未标明）— 访问 2026-11-21（已打开原文）
- [S9] Queensland Building and Construction Commission Act 1991 Part 4A（s67AAA、s67J、s67K、s67L、s67M、s67N、s67NA、s67NB、s67T、s67U、s67W）及 Schedule 1B s3 — Queensland Legislation — https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1991-098 — 现行版本（页面版本日期未标明）— 访问 2026-11-21（已打开原文）
- [S10] Building and Construction Industry (Portable Long Service Leave) Act 1991 (Qld) s66、s67、s74、s75 — Queensland Legislation — https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1991-090 — 现行版本 — 访问 2026-11-21（已打开原文）
- [S11] Building and Construction Industry (Portable Long Service Leave) Regulation 2024 s7、s8、s9（PDF，Current as at 23 August 2024）— Queensland Legislation — https://www.legislation.qld.gov.au/view/pdf/2024-08-23/sl-2024-0162 — 2024-08-23 — 访问 2026-11-21（已打开原文；之后是否修订待证实）
- [S12] What are minimum financial requirements? — QBCC — https://www.qbcc.qld.gov.au/running-your-business/financial-requirements/what-are-minimum-financial-requirements — Last published 2021-10-18 — 访问 2026-11-21（已打开原页）
- [S13] Current ratio requirements — QBCC — https://www.qbcc.qld.gov.au/running-your-business/financial-requirements/current-ratio-requirements — Last published 2021-10-18 — 访问 2026-11-21（已打开原页）
- [S14] MFR report or declaration — QBCC — https://www.qbcc.qld.gov.au/running-your-business/financial-requirements/financial-reporting-obligations-contractor-licensees-0 — Last published 2025-03-27 — 访问 2026-11-21（已打开原页）
- [S15] Regulatory Guide for Minimum Financial Requirements and Annual Reporting（PDF，March 2026）— QBCC — https://www.qbcc.qld.gov.au/sites/default/files/documents/regulatory-guide-mfr-annual-reporting.pdf — 2026-03 — 访问 2026-11-21（已打开原文）
- [S16] 23-346MR ASIC's annual corporate insolvency statistics shows COVID-19 impact on small business — ASIC — https://www.asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-346mr-asic-s-annual-corporate-insolvency-statistics-shows-covid-19-impact-on-small-business — 2023（具体日期页面未标明；数据期 2022-07-01 至 2023-06-30）— 访问 2026-11-21（已打开原页）
- [S17] Insolvency statistics（Series 3 外部管理人报告下载页）— ASIC — https://www.asic.gov.au/about-asic/corporate-publications/statistics/insolvency-statistics — 日期未标明 — 访问 2026-11-21（页面已打开；Excel 文件在 download.asic.gov.au，被代理拒绝，未读取）
- 未能打开（待证实项的出处）：ATO Registering for GST、GST property withholding、How long to keep your records 等页面（www.ato.gov.au 返回 Access Denied）；WorkCover Queensland / WorkSafe（www.worksafe.qld.gov.au，Cloudflare 验证）；QLeave（www.qleave.qld.gov.au，Cloudflare 验证）— 访问尝试 2026-11-21

## 核对记录
- 2026-11-21 新建。所有带条款号的数字均直接核对法律原文或 QBCC 原文。
- 原计划从 ATO 网站核对 GST 门槛、withholding 和记录保存，ATO 网站无法访问，改用 GST Act、GST Regulations 和 Taxation Administration Act 原文；ATO 操作性内容（表格、流程）保留「待证实」。
- WorkCover Queensland 和 QLeave 网站无法访问，改用 Workers' Compensation and Rehabilitation Act 2003 和 PLSL Act/Regulation 原文；保费费率、缴费流程保留「待证实」。
- 注意：QBCC Act Part 4A 不适用于 domestic building contract，但适用于住宅项目的分包合同（Sch 1B s3(2)(a)），这一点容易被误解。
