# 高层-工地管理与WHS

适用州：QLD（布里斯班）｜资料核对日期：2026-11-20｜状态：部分待证实

## 摘要
本文从 principal contractor（总包）的角度，整理在布里斯班盖一栋 20 层 Class 2 公寓时的工地管理与安全法定要求：WHS Regulation 2011 (Qld) 中的 construction project、principal contractor、WHS management plan、高风险建筑工作与 SWMS；塔吊和施工电梯的高风险作业执照（HRWL）与 plant 注册；脚手架、模板、防坠落与防坠物（昆州特有的 hoarding/gantry 规则）；工地厕所等设施最低数量；布里斯班的围挡、占道、道路封闭和施工时间（Environmental Protection Act 1994 (Qld) s440R：周一至周六 6:30–18:30）。法规条文均直接核对 legislation.qld.gov.au 和 brisbane.qld.gov.au 原文；worksafe.qld.gov.au 对本会话返回 Cloudflare 拦截，codes of practice 只核对了官方批准清单（名称和生效日期），未读 code 正文。最后给出文件体系（日报、ITP、NCR、RFI、variation、进度会议）。安全不能省钱：合法的节省来自工序安排（如外防护屏随楼层周期爬升）和提前办许可，不是减少防护。

> 住宅线 WHS 见 `工地安全WHS规定.md`；可填写的模板见 `../05-工具与模板/高层-工地管理计划模板.md`。

---

## 一、Principal contractor 与 construction project

### 1. 定义（WHS Regulation 2011 (Qld) Chapter 6）[S1]
- **Construction project**：construction work 造价 **$250,000 或以上** 的项目（s292）[S1]。20 层公寓必然属于。
- **Principal contractor**（s293）：委托 construction project 的 PCBU 默认是 principal contractor；如果它另聘一个 PCBU 担任 principal contractor 并授权其管理控制工地、履行 principal contractor 职责，则被聘者是 principal contractor。一个项目**同一时间只能有一个** principal contractor [S1]。
- 开发商必须把其掌握的工地及周边危险信息交给 principal contractor（s296）[S1]。
- **Large construction project**：造价 **$7.5m 或以上**；small construction project 为 $7.5m 以下（Sch 5A 定义，用于厕所数量）[S1]。

### 2. Principal contractor 的主要法定职责（Part 6.4）[S1]
| 条款 | 职责 | 最高罚则 |
|---|---|---|
| s308 | 设置标牌：principal contractor 名称、电话（含下班后电话）、工地办公室位置，须从工地外清楚可见 | 36 penalty units |
| s309 | 开工前编写书面 **WHS management plan** | 60 penalty units |
| s310 | 让每个施工人员在开工前知道 WHS management plan 的内容及查阅权 | — |
| s311 | 审查并按需修订 WHS management plan，并告知修订 | 36 penalty units |
| s312 | 在高风险建筑工作开始前采取一切合理步骤取得 SWMS 副本 | 36 penalty units |
| s313 | 保存 WHS management plan 至项目完成；发生 notifiable incident 时至少保存 2 年；施工人员可随时查阅 | — |
| s314 | 安排确保遵守 Part 3.2 多个 division（一般工作环境、设施、急救、应急计划等）和 Part 4.4（坠落）等 | 60 penalty units |
| s315 | 管理以下风险：材料和垃圾的存放、搬运、处置；闲置 plant 的存放；受施工影响的周边交通；工地上的 essential services | — |
| s315A + Sch 5A | 工地设施（厕所等）——见下文第六节 | 20–60 penalty units |
| s315B–315M | 防坠物（falling objects）——见下文第五节 | 60 penalty units |

（penalty unit 的金额会按年调整，本文不写金额，以 Penalties and Sentences Regulation 现行值为准，待证实。）

### 3. WHS management plan 必须包含（s309(2)）[S1]
1. 工地上负有特定健康安全职责人员的姓名、职位和职责；
2. 工地上各 PCBU 之间的协商、合作和活动协调安排；
3. WHS 事故管理安排；
4. 工地特定的安全规则，以及让所有人知悉这些规则的安排；
5. SWMS 的收集、评估、监督和审查安排。

### 4. General construction induction（White Card）[S1]
- PCBU 必须确保从事 construction work 的工人完成 general construction induction training；如果完成培训已超过 2 年且过去 2 年没做过 construction work，须重新培训（s316、s317）[S1]。
- 工地准入流程应核查 White Card，并另做**工地专项入场培训**（site induction）。

---

## 二、高风险建筑工作与 SWMS（WHS Regulation 2011 (Qld) s291、s299–s303）[S1]

### 1. 高风险建筑工作（s291）——20 层公寓几乎每一项都会碰到
| s291 项 | 内容 | 本项目中的典型工序 |
|---|---|---|
| (a) | 有坠落超过 **2 m** 风险 | 楼板边、核心筒、立面安装、电梯井 |
| (b) | 在通信塔上工作 | 一般不涉及 |
| (c) | 拆除承重或与结构完整性有关的构件 | 场地原有建筑拆除 |
| (d) | 涉及或可能涉及扰动石棉 | 旧建筑拆除 |
| (e) | 需要临时支撑以防倒塌的结构改动或维修 | 回顶（back-propping）、转换层 |
| (f) | 在受限空间内或附近 | 集水坑、水箱、管井 |
| (g) | 在开挖深度超过 **1.5 m** 的竖井或沟槽内或附近；隧道 | 基坑、地下室、桩基 |
| (h) | 使用炸药 | 岩石爆破（如有） |
| (i) | 在加压燃气管附近 | 接驳 |
| (j) | 在化学品、燃料或制冷剂管线附近 | 机电 |
| (k) | 在带电电气装置或设施附近 | 临电、Energex 接驳 |
| (l) | 可能有污染或易燃气体的区域 | 地下室、受污染土 |
| (m) | **tilt-up 或预制混凝土** | 预制外墙板、预制楼梯 |
| (n) | 在使用中的道路、铁路等交通走廊上或旁边 | 临街施工、占道 |
| (o) | 有移动式动力设备移动的区域 | 挖掘机、混凝土泵车、叉车 |
| (p) | 人为极端温度区域 | 一般不涉及 |
| (q) | 有溺水风险的水或液体附近 | 降水井、积水基坑 |
| (r) | 潜水作业 | 一般不涉及 |

### 2. SWMS 要求 [S1]
- 高风险建筑工作开始前必须准备 SWMS（s299(1)）；SWMS 必须识别哪项是高风险建筑工作、说明危险和风险、控制措施及其实施、监督和审查方法（s299(2)）。
- 如果是 construction project，SWMS 须考虑该工地的 **WHS management plan**（s299(3)）。
- 坠落超过 2 m 的 SWMS 如果只用行政控制或个人防护装备（PPE），必须写出曾考虑过的所有控制措施（含 s79(3) 的一般要求）（s299(4)）[S1]。
- 工作必须按 SWMS 进行；不按 SWMS 时必须立即（或安全时）停工，直到按 SWMS 进行（s300，60 penalty units）[S1]。
- 分包商须在开工前把 SWMS 副本交给 principal contractor（s301）；控制措施修订时须审查 SWMS（s302）；SWMS 保存至该工作完成（s303）[S1]。

---

## 三、塔吊、施工电梯和混凝土泵：执照与注册

### 1. 高风险作业执照（HRWL）类别（WHS Regulation Sch 3, Table 3.1）[S1]
| 类别 | 内容（原文摘要） | 本项目用途 |
|---|---|---|
| Basic scaffolding | 模块化/预制脚手架、≤500 kg 悬挑物料提升机、绳、gin wheel、安全网和静态绳、支架式脚手架（含模板支架） | 外脚手架、核心筒脚手架 |
| Intermediate scaffolding | 含 Basic；另含悬挑卸料平台（cantilevered crane loading platforms）、悬挑脚手架、spur scaffolds、坡道、**与外围安全屏（perimeter safety screens and shutters）相关的脚手架**、**mast climbing work platforms**、扣件式脚手架 | 卸料平台、外防护屏、爬架式平台 |
| Advanced scaffolding | 含 Intermediate；另含悬挑提升机、吊挂脚手架、悬吊脚手架 | 吊篮 / 悬吊平台 |
| Dogging | 指挥吊装（dogging work） | 塔吊吊装指挥 |
| Basic rigging | 含 dogging；结构钢安装、提升机、预制混凝土构件、安全网和静态绳、mast climbing work platforms、外围安全屏、悬挑卸料平台 | 预制件安装、外防护屏 |
| Intermediate rigging | 含 Basic；带臂提升机和自爬升提升机、**起重机**、输送机、挖掘机、tilt 板、拆除、双机抬吊 | 塔吊安装、爬升（以 code 和厂商要求为准） |
| Advanced rigging | 含 Intermediate；gin poles、缆索、guyed derricks、悬吊和吊挂脚手架 | 特殊吊装 |
| **Tower crane** | 操作塔吊 | 塔吊司机 |
| Self-erecting tower crane | 操作自立式塔吊 | — |
| Slewing mobile crane（按吨位分级） | 操作汽车吊/履带吊 | 塔吊安装拆除用的汽车吊 |
| **Materials hoist** | 操作物料提升机 | — |
| **Personnel and materials hoist** | 操作人货两用施工电梯（含物料提升机） | 施工电梯 |
| **Concrete placing boom** | 操作混凝土布料杆 | 布料杆 / 泵车 |
| Boom-type elevating work platform | 操作臂式高空作业平台（臂长 11 m 及以上） | 立面、地下室顶板 |

- 申请、培训和考核流程由 WorkSafe Queensland 管理（worksafe.qld.gov.au 本轮无法访问，流程细节待证实）。

### 2. Plant 注册（WHS Regulation Sch 5）[S1]
| 类别 | Part 1 设计注册（design registration） | Part 2 单台注册（item registration） |
|---|---|---|
| 塔吊（含自立式） | 是（1.3） | **是（3.3）** |
| 电梯、扶梯、自动步道 | 是（1.4） | 是（3.4）——**Class 2 建筑里供一个单元内部多层使用的户内电梯除外** |
| 平台行程超过规定值的提升机（施工电梯等） | 是（1.6） | 否（不在 Part 2） |
| 吊笼（work boxes 挂在起重机上） | 是（1.7） | 否 |
| 混凝土布料杆 | 是（1.9） | 否 |
| 预制脚手架 | 是（1.10） | 否 |
| 臂式高空作业平台 | 是（1.11） | 否 |
| Mast climbing work platforms | 是（1.14） | 否 |
| 汽车吊（超过规定额定起重量） | 是（1.15） | 见 Part 2 原文 |
| 建筑维护设备（building maintenance units，屋顶吊篮机） | 是（1.5） | 是（3.5） |

- 登记的塔吊和汽车吊须由 competent person 进行 **major inspection**（s235）[S1]；具体周期以原文和 Tower Crane Code of Practice 2017 为准（待证实）。
- 永久电梯（3.4）和屋顶 BMU（3.5）在竣工前要完成注册，纳入交付清单。

### 3. 适用的 codes of practice（昆州批准清单）[S2]
Work Health and Safety (Codes of Practice) Notice 2022（current as at 1 September 2026）Schedule 1 中与高层施工直接相关的：
| Code | 生效日期 |
|---|---|
| **Formwork Code of Practice 2016** | 2016-03-31 |
| **Tower Crane Code of Practice 2017** | 2017-07-01 |
| **Scaffolding Code of Practice 2021** | 2021-07-01 |
| Mobile Crane Code of Practice 2024 | 2024-09-23 |
| Concrete Pumping Code of Practice 2019 | 2019-12-02 |
| Tilt-up and Pre-cast Construction Industry Code of Practice 2003 | 2003-06-01 |
| Steel Construction Advisory Standard 2004 | 2004-09-10 |
| Traffic Management for Construction or Maintenance Work Code of Practice（2008-09-01 生效；Notice 中标题换行，全称待核） | 2008-09-01 |
| Managing the Risk of Falls at Workplaces（2021） | 2021-03-01 |
| Demolition Work Code of Practice 2021；Excavation Work Code of Practice 2021；Confined Spaces Code of Practice 2021 | 2021-03-01 |
| Managing respirable crystalline silica dust exposure in construction and manufacturing of construction elements（2022） | 2023-05-01 |
| Safe Design of Structures Code of Practice 2021；How to Manage Work Health and Safety Risks（2021）；Managing Noise and Preventing Hearing Loss at Work（2021）；Hazardous Manual Tasks（2021）；First Aid in the Workplace（2021）；Managing Risks of Plant in the Workplace（2021） | 2021-03-01 |
| Managing the risk of psychosocial hazards at work（2022/2023） | 2023-04-01 |

- 以上只核对了名称和生效日期；**code 正文（例如模板支撑检查、塔吊基础设计、脚手架检查间隔细节）本轮未能打开 worksafe.qld.gov.au，待证实**。

---

## 四、脚手架、模板与防坠落

### 1. 脚手架（WHS Regulation s225、s306P–306Q）[S1]
- 适用于悬吊、悬挑、spur、吊挂脚手架，以及**任何人或物可能坠落超过 4 m 的脚手架**（s225(1)）。
- 管理控制人在收到 competent person 书面确认脚手架搭设完成前，不得使用（s225(2)）。
- 检查：使用前；发生可能影响稳定的事故后；维修后；**至少每 30 天**一次（s225(3)）[S1]。
- s306P、s306Q 规定搭设和拆除脚手架时的具体防坠要求（昆州特有条款）[S1]，细节以原文为准。
- 搭设超过 4 m 的脚手架须持相应 scaffolding HRWL（Sch 3），类别按脚手架类型（见第三节）。

### 2. 模板（Formwork Code of Practice 2016）[S2]
- 昆州批准 code，2016-03-31 生效 [S2]。code 内容（设计、搭设、浇筑前检查、拆模和回顶）本轮未读原文，待证实。
- 法规层面：模板搭设和拆除时的防坠物要求见 s315H（下文第五节）；模板内部坠落的 fall arresting platform 有例外（s306D(5)）[S1]。
- 工地实践（通用做法，非法规原文）：模板和支撑须有临时工程设计（temporary works design）和浇筑前检查记录（列入 ITP 的 hold point）。

### 3. 防坠落：临边、开口（WHS Regulation s78–80、s306D–306H）[S1]
- **非住宅类 construction work 坠落高度 ≥ 2 m**（住宅类为 ≥ 3 m）或屋面坡度 > 26° 时，开工前必须采取控制措施：首先**防止坠落**（临边防护、开口盖板、行动限制系统 travel restraint）；不可行时才用**坠落制动**（fall arresting platform、安全带系统、安全网）（s306D(1)–(3)）[S1]。20 层公寓适用 **2 m** 门槛：s306A 把 housing construction work 限定为「不位于另一住宅或建筑其他部分之上或之下（私人车库除外）」的独立屋、以防火墙分隔的联排屋，以及 ≤300 m² 的寄宿类建筑及其附属建筑 [S1]；上下叠置的公寓不属于 housing construction work。
- 临边防护须按厂商说明或工程师 / competent person 的要求搭设；须能承受人员冲撞；顶部栏杆高度要求：基础面宽度 ≥ 1,200 mm 时，栏杆顶至少高出该面 900 mm（s306E）[S1]，其余情况见原文。
- 电梯井、管井、楼板洞口：用固定盖板或临边防护；每层浇筑后立即恢复。
- 楼层边缘的外防护屏（perimeter screens）兼具防坠落和防坠物功能，搭设、爬升须由持 Intermediate scaffolding / Basic rigging 及以上执照的人员进行（Sch 3）[S1]。

---

## 五、防坠物：hoarding、gantry、catch platform（昆州特有，s315B–315M）[S1]
对非 civil construction、非 housing construction work（即高层公寓）：
1. principal contractor 须让相关人员确定围挡线（proposed line），并测量「工作最高点」到「围挡线上最近地面点」连线与水平面的夹角（s315F(2)）。
2. 按夹角确定围挡（s315F(3)）[S1]：

| 测得角度 | 最低要求 |
|---|---|
| ≤ 15° | ≥ 900 mm 的围栏或 hoarding |
| > 15° 且 ≤ 30° | ≥ 1,800 mm 的 hoarding |
| > 30° 且 < 75° | ≥ 1,800 mm、**全封闭板材**（木、胶合板、金属或坚固合成板）的 hoarding |
| ≥ 75° | ≥ 1,800 mm 全封闭 hoarding（不属于 gantry），或按 s315G(3)(a) 搭设 gantry |

3. 全封闭 hoarding 须能承受：顶部在两柱中间 1 m² 上施加 500 N/m² 水平力不发生永久变形；在 1,500 mm² 上施加 950 N 不被完全穿透（s315F(7)）[S1]。
4. 角度 ≥ 75° 时（拆除和模板作业除外），开工前还须至少采用一种：沿可能坠物的各边搭 **gantry**；按 s315M **封闭相邻区域**；或在可能坠物楼层下方不超过 1 m 处设 **catch platform + perimeter containment screening**（s315G）[S1]。模板搭拆和拆除作业另见 s315H。
5. 用作防坠物的网须满足：钢丝直径 ≥ 2.5 mm、抗拉强度 ≥ 380 MPa，孔径限值见 s315D [S1]。
- 实务：临街 20 层楼几乎都会达到 ≥ 75°，所以临街一侧通常要 gantry（需同时向 BCC 申请 hoarding/gantry 许可，见第七节）或用外防护屏 + catch platform。

---

## 六、工地设施（WHS Regulation s315A、Schedule 5A）[S1]
- principal contractor 必须让每名施工人员都能合理使用符合要求的厕所（Sch 5A s2A）。
- **最少厕所数量**：每 15 人（不足 15 按 15 计）至少 1 个；**large construction project（≥ $7.5m）** 另需每 100 人（不足 100 按 100 计）至少 1 个**女性专用厕所**（Sch 5A s2B）。原文示例：large project 有 120 人时，至少 8 个厕所 + 2 个女性专用厕所 [S1]。
- 设施须保持卫生、安全、可用，建立检查和清洁制度；有女性卫生用品处理设施的须妥善处置（s315A(2)）[S1]。
- 高层项目实务：随楼层上升在中间楼层设临时厕所，减少往返（「合理可用」须结合距离判断，原文以单层建筑 100 m 内为例）[S1]。

---

## 七、场地布置与布里斯班许可

### 1. 围挡、占道（footpath）[S3]
BCC「Footpath works and permits」原文：
- 以下工作须事先获得批准：临时在人行道（footway）上堆放建筑设备和材料；**临时在工地周围设围挡**；开挖人行道或道路等 [S3]。
- 以下还需要**批准 + 许可（permit）**：临时使用人行道；在人行道上堆放设备或材料；**设置 hoarding 和 gantry** [S3]。
- 在 CBD（City Plan 的 PC1 principal centre (city centre) zone）以外、非 state-controlled road 上，占用人行道少于 48 小时可免批，但须保留通行宽度：住宅区 1.2 m，CBD 或商业区 1.8 m [S3]。
- 收费按区（Zone A：PC1；Zone B：PC2、MC、DC2、HDR、MU；Zone C：其他）[S3]。高层公寓常在 HDR、MU 或 PC1/PC2 区内。
- 处理时间：**预留 20 天**出结果 [S3]。须提交场地草图（工作位置、临时结构尺寸、开挖、行人如何绕行），可附交通管理计划；可能被要求补交行人管理计划 [S3]。

### 2. 道路封闭、construction works zone [S4][S5]
- 自 **2025-07-01** 起，BCC 的临时道路封闭、自行车道封闭和 **construction works zone** 统一通过 **Road Corridor Permit System（RCPS）** 申请 [S4]。
- **Temporary Lane/Road Closure Assessment and Certificate**：适用于工地周边封车道、**塔吊和设备进出场**、在道路上放置路障、开挖等；Council 批准后还须向 **Queensland Police Service** 申请许可 [S5]。
- 申请须在拟封闭日期前至少 **20 个完整工作日**提交（资料齐全起算）；证书最长有效 **1 个月**，每次最多 5 条邻近街道，长期需续期 [S5]。
- 必交文件：交通管理计划（traffic management plan）和 traffic guidance scheme；如与 DA 有关须附 DA 批准 [S5]。
- **Construction works zone**：占用工地旁一段路边用于装卸货的许可，由 Council 设标牌并注明时段，不得用于一般停车 [S5]。
- 如道路封闭用于 6:30–18:00 以外的施工，申请前须先取得 Environmental Protection Act 1994 方面的批准（BCC 原文写的是 6.30am–6pm，与 EP Act s440R 的 6:30pm 不同，以 out-of-hours 审批为准）[S5]。
- 设置 works zone、使用起重机或在人行道放路障可能需要另外的批准 [S5]。
- 官方名称说明：BCC 网站没有名为「Permit to occupy footpath/road」的单一许可；对应的是 footpath works approval/permit、hoarding and gantry permit、Temporary Lane/Road Closure Certificate、construction works zone（经 RCPS）[S3][S4][S5]。

### 3. 施工噪音时间（Environmental Protection Act 1994 (Qld) s440R）[S6]
- **原文**：不得以产生 audible noise 的方式进行 building work——**business day 或周六 6:30 a.m. 之前或 6:30 p.m. 之后；其他日子（周日、公众假期）任何时间**（s440R(1)）[S6]。
- 「audible noise」指受影响建筑内的占用人能清楚听到（s440L）[S6]。违反 noise standard：故意为最高 1,665 penalty units，否则 600 penalty units（s440Q）[S6]。
- BCC 页面说明：周六公众假期按周六处理（允许 6:30–18:30）；周日或公众假期（不含周六公众假期）任何时间不得有清晰可闻噪音；**如 development approval 授权在上述时间之外施工，按 DA 条件执行** [S7]。
- **Out of hours construction approval（BCC）**：只有 DA 条件要求就非工作时间施工通知或取得 Council 批准时才可申请；须证明因公共安全、交通管理、公用设施中断等正当理由不能在规定时间内进行（商业便利或排期问题不被接受）；须附非工作时间施工噪音管理计划和给受影响住户的通知信；**公众假期不发批**；高噪音作业（拆除、爆破、打桩、混凝土/沥青切割、金属切割、破碎岩石）**22:00–6:30 不允许** [S8]。
- 实务：大体积混凝土浇筑（筏板、转换层）常需早于 6:30 开始，必须在 DA 阶段就争取相关条件并提前申请 out-of-hours approval。

### 4. 场地布置清单（通用工地实践）
- 塔吊位置（覆盖范围、与邻楼和电线的距离、基础、拆除路线、Council 和航空限高——布里斯班机场航空限制面待证实）。
- 施工电梯位置（与外防护屏和立面安装的衔接）。
- 混凝土泵车 / 固定泵和布料杆位置。
- 材料堆放、钢筋加工区、垃圾分类箱。
- 工地办公室、休息室、厕所（按 Sch 5A 计算数量）、急救室。
- 出入口、洗车台、沉淀池（防止泥沙进入雨水系统——属 EP Act 一般环境责任）。
- 围挡、hoarding、gantry、行人通道。
- 临电（Energex 接驳）、临水、消防临时设施。
- principal contractor 标牌（s308）。

---

## 八、文件体系（工地实践；法定部分已标注）
| 文件 | 用途 | 法定或惯例 |
|---|---|---|
| WHS management plan | 见第一节 | **法定**（s309） |
| SWMS 登记册 | 收集、审查分包 SWMS | **法定**（s301、s309(2)(e)、s312） |
| 现场日报（site diary） | 天气、人数（按分包）、设备、完成工作、检查、事故、来访、延误原因 | 惯例；对 EOT 和 variation 举证极其重要 |
| ITP（Inspection and Test Plan，检验与试验计划） | 按工序列出检查点、hold point（未经签字不得继续）和 witness point、验收标准、记录 | 惯例；常为合同要求 |
| NCR（Non-Conformance Report，不合格报告） | 记录不合格、原因、整改、关闭 | 惯例 |
| RFI（Request for Information） | 向设计方澄清图纸 | 惯例；记录日期用于延误分析 |
| Variation（变更）登记 | 指令、报价、批准、金额 | 合同要求（AS 4000 等）；住宅合同另有 QBCC Act 法定要求 |
| EOT（工期延长）申请登记 | 按合同期限通知 | 合同要求（逾期可能失权） |
| Payment claim 登记 | 按 Building Industry Fairness (Security of Payment) Act 2017 (Qld) 申请和回复进度款 | 法定程序（时限待证实，本文未核对） |
| 检测报告 | 混凝土试块、钢筋、PT 张拉记录、防水淋水试验、消防系统调试 | 规范和合同要求 |
| 进度会议纪要 | 见模板文件 | 惯例 |
| 事故和 notifiable incident 记录 | 须向 WorkSafe 报告的事故 | **法定**（WHS Act，本文未核对条款） |

---

## 核对记录
- 2026-11-20 新建。WHS Regulation 2011 (Qld)、EP Act 1994 (Qld) 直接从 legislation.qld.gov.au 现行版本核对；BCC 页面直接核对。
- worksafe.qld.gov.au 对本会话返回 Cloudflare 拦截（403），codes of practice 正文、HRWL 申请流程未核对。Codes 清单依据 Work Health and Safety (Codes of Practice) Notice 2022（current as at 1 September 2026）PDF。

## 来源
- [S1] Work Health and Safety Regulation 2011 (Qld)（现行版本）, ss 78–80, 225, 235, 291–317, 306A–306Q, 315A–315M, Sch 3, Sch 5, Sch 5A. https://www.legislation.qld.gov.au/view/whole/html/inforce/current/sl-2011-0240 ；访问 2026-11-20（原文）
- [S2] Work Health and Safety (Codes of Practice) Notice 2022, Schedule 1, current as at 1 September 2026. Queensland Legislation（legislation.qld.gov.au，PDF；具体 URL 本轮未记录）；访问 2026-11-20（原文）
- [S3] Brisbane City Council, "Footpath works and permits". https://www.brisbane.qld.gov.au/transport-and-parking/traffic-management-and-safety/footpath-works-and-permits ；日期未标明；访问 2026-11-20（原文）
- [S4] Brisbane City Council, "Road Corridor Permit System". https://www.brisbane.qld.gov.au/transport-and-parking/traffic-management-and-safety/road-corridor-permit-system ；日期未标明（系统 2025-07-01 启用）；访问 2026-11-20（原文）
- [S5] Brisbane City Council, "Road closure permits". https://www.brisbane.qld.gov.au/transport-and-parking/traffic-management-and-safety/road-closure-permits ；日期未标明；访问 2026-11-20（原文）
- [S6] Environmental Protection Act 1994 (Qld)（现行版本）, ss 440L, 440Q, 440R. https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1994-062 ；访问 2026-11-20（原文）
- [S7] Brisbane City Council, "Noise restrictions and complaints". https://www.brisbane.qld.gov.au/laws-and-permits/complaints/noise-restrictions-and-complaints ；日期未标明；访问 2026-11-20（原文）
- [S8] Brisbane City Council, "Out of hours construction approval". https://www.brisbane.qld.gov.au/building-and-planning/additional-approvals/out-of-hours-construction-approval ；日期未标明；访问 2026-11-20（原文）
