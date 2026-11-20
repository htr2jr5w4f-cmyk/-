# 施工工法要点-builder视角

## 摘要
本文按工序整理 builder 在布里斯班建独立住宅（Class 1a，混凝土板 + 框架）时的技术要点：放线（set-out）、开挖与填土、楼板（防潮膜、钢筋保护层、混凝土、白蚁防护）、框架（AS 1684 / NASH、支撑与抗拔）、屋面（AS 1562.1、泛水）、湿区防水（Housing Provisions Part 10.2 / AS 3740）、外墙泛水与防潮层、门窗安装。每项写「依据的 NCC 条款或标准」「关键检查点」「常见错误」。依据以免费的 NCC 2022 Volume Two（H 部分 Deemed-to-Satisfy 条款）和 ABCB Housing Provisions 原文为主，辅以 QBCC 的 Standards and Tolerances Guide 和缺陷通报；付费澳洲标准里的具体数值不写，标「见 AS xxxx，付费」。对省钱的意义：屋面泛水和湿区防水是 QBCC 统计里最常见、整改最贵的缺陷（QBCC 称 2024–25 财年每宗浴室保修理赔平均整改费接近 $25,000），一次做对是最省钱的做法。

适用州：QLD｜资料核对日期：2026-11-21｜状态：部分待证实（NCC / Housing Provisions 条文已在 ncc.abcb.gov.au 原文核对；付费标准内容未写数值）

> **版本说明**：本文引用的是 **NCC 2022** 和 **ABCB Housing Provisions（2022 版）**。本库 `01-法规标准/NCC现行版本与住宅要求.md` 记载昆州目前仍执行 NCC 2022、NCC 2025 推迟到 2027-05-01 实施（该日期以那篇文件的核对结果为准）。NCC 2025 对防水有改动（QBCC 提到：水平面须有坡度防积水、防水膜须直接做在结构基层上而不是找平层上）[S20]，换版前需重新核对。
>
> **Deemed-to-Satisfy（DTS）的意思**：NCC 规定，按所列标准或 Housing Provisions 的做法施工即视为满足性能要求；Housing Provisions 的很多章节有适用范围限制（例如风级不超过 N3、场地类别 A/S/M），超出范围就要按相应的澳洲标准或工程师设计做。下面每项都写了这些限制。

---

## 0. 通用：builder 的检查方法
- QBCC 建议在结构阶段完成时（footing、slab、frame、final）以及重要非结构阶段开始前（油漆前、钉板前、外墙钉挂前）、交房前做详细检查 [S17]。
- QBCC 的 supervisor's checklist 按 Foundation / Structure / Drainage / Internal finishes 列出逐项检查内容 [S17]，本文各节的「关键检查点」与其对应。
- QBCC 的 **Standards and Tolerances Guide（Queensland, December 2023）** 是判断缺陷的基准，例如：放线偏离正确位置超过 50 mm 且影响安全使用或合理舒适性的，属缺陷；墙框垂直度在任意 2 m 高度内偏差超过 4 mm 属缺陷 [S18]。下文引用的容差都来自该指南。
- QBCC 对屋面缺陷的建议同样适用于各工序：保留合同和规格、批准文件、安装前和各阶段照片、完工证据、厂家规格和安装说明、施工期间天气记录（用于工期顺延）、与分包和业主的书面沟通 [S19]。

---

## 1. 放线（set-out）

**依据**
- 放线须符合批准图纸、地块产权证（Certificate of Title）、规划/开发批准、相关规划叠加图层和建筑法规；否则属缺陷 [S18]。
- 法定 frame 检查前，独立住宅的**退界（boundary clearance）**一项若由 competent person 协助检查，必须是 **cadastral surveyor**（地籍测量师）[S21]。

**关键检查点**
- 地块描述和边界核实；退界与批准文件一致；建筑轮廓与批准文件和合同文件一致 [S17]。
- 建筑平台标高正确；完成楼面标高（FFL）满足地方政府最低标高（例如洪水、地表漫流）[S17]。布里斯班的洪水标高要求见 `01-法规标准/布里斯班规划与地块限制.md`。

**容差（QBCC 指南，完工后 12 个月内）** [S18]
- 位置偏离超过 50 mm 且影响安全使用或合理舒适性：缺陷。
- 外部尺寸偏差超过 L/200（L 为墙总长）或 5 mm（取大者）：缺陷。
- FFL 偏离设计超过 40 mm：缺陷。

**常见错误**
- 只凭围栏或邻居的旧桩放线，不请测量师复核边界（行业通行做法，建议由注册测量师放线并出具放线图；待证实是否为法定要求，法定要求以 certifier 的批准条件为准）。
- 放线时没有核对排水坡度和楼板高出地面的要求，导致后面楼板高度不够（见第 3 节）。

---

## 2. 开挖与填土

**依据**
- NCC Volume Two **H1D3(1)**：按 Housing Provisions **Part 3.2** 做土方工程即满足要求，前提是场地按 4.2.2 划为 A、S、M、H 或 E 类且为「normal」场地条件；挡土结构按 **AS 4678** [S2]。
- 场地分类按 **AS 2870**（Housing Provisions 4.2.2）。H、E、P 类须直接按 AS 2870 设计（付费）；M-D 也超出 Housing Provisions 范围 [S4]。

**关键检查点（Housing Provisions 4.2.3、4.2.4）** [S4]
- 基础开挖尽可能垂直切边；坑底平地基本水平（为排水最多 1:40 坡度），坡地不陡于 1:10；坑内无松土、树根、泥浆、杂物；表土和草根清除。
- 松散砂地或易受风/水侵蚀的场地，基础底面在完成地面以下不少于 300 mm。
- 板下填土须为 controlled fill 或 rolled fill：
  - controlled fill：砂填最深 800 mm，每层不超过 300 mm，用振动平板或振动压路机压实；黏土填最深 400 mm，每层不超过 150 mm，机械碾压。
  - rolled fill：砂填最深 600 mm、黏土填最深 300 mm，用挖掘机等反复碾压，每层厚度同上限。
  - 砂填不得含砾石级颗粒，用 AS 1289.6.3.3 方法测得每 300 mm 不少于 7 击；黏土压实时须湿润。
  - 填土顶面铺不少于 20 mm 的干净采石砂（可用符合 Part 3.4 的碎石白蚁防护系统代替）。
- 法定 **excavation** 检查：开挖到地基土之后、浇基础或楼板混凝土之前 [S16]。

**常见错误**
- 填土厚度超出 Housing Provisions 范围仍按 DTS 做，没有工程师设计和压实证明。QBCC 指南写明，因填土或压实不足造成的基础移动，即使有 Level 1 compaction certificate，也属缺陷 [S18]。
- 坑底积水、泥浆没清理就浇筑。

---

## 3. 楼板（slab-on-ground）

**依据**
- NCC Volume Two **H1D4(1)**：footings 和 slabs 按 **AS 2870**、**AS 3600**，或（在 H1D4(2) 的限制内）Housing Provisions **Section 4** [S2]。
- H1D4(2) 限制（节选）：场地为 A、S 或 M 类且承载力均匀；板长宽不超过 18 m；无永久缝（施工缝除外）；只有外直角（几何形状），最多一个内凹角；非侵蚀性土；不超过两层可通行楼面；墙高不超过 8 m（不含山墙）；normal 场地；非高山区；AS 1170.4 附录 A 无特殊抗震要求 [S2]。超出就要工程师按 AS 2870 设计——布里斯班很多黏土地块是 H 类，这时 Housing Provisions 的楼板做法**不能**直接用（场地类别以土工报告为准）。

**3.1 防潮膜（vapour barrier）**——Housing Provisions **4.2.8**（适用于 QLD 的全国文本）[S4]
- Class 1 建筑（以及与之连成一体的 Class 10 楼板）的板下必须铺 vapour barrier。
- 材料：**0.2 mm** 名义厚度聚乙烯膜，**中等抗冲击（medium impact resistant）**，按 AS 2870 第 5.3.3.3 条的标准判定；膜上须连续印有「AS 2870 Concrete underlay, 0.2 mm Medium impact resistance」。
- 安装：所有接缝搭接**不少于 200 mm**；管线穿透处用胶带或紧贴套管密封；破损处（管线穿透以外）用同种膜加胶带完全封补；膜须覆盖整个板底，并延伸到内外梁下方、收头到地面。
- ⚠ 州差异：NSW 等州的变体要求更高等级的 damp-proofing membrane（高抗冲击）；本文只写 QLD 适用的全国文本 [S4]。

**3.2 钢筋与保护层**——Housing Provisions **4.2.11** [S4]
- 钢筋须符合 AS 2870，可用焊接钢筋网、trench mesh 或钢筋；有内凹角的板须在角部加斜向钢筋（如 3-N12，长不少于 2 m，45° 放置，中点在内角处）。
- **保护层**（钢筋最外缘，包括箍筋、扎丝，到混凝土表面）不少于：
  - **40 mm**：到无保护的土；
  - **30 mm**：到与土接触的防潮膜；
  - **20 mm**：到室内表面；
  - **40 mm**：到室外暴露面。
- 钢筋无浮锈、泥、油漆和油；绑扎牢固；用钢丝、混凝土或塑料马凳架离地面或模板；钢筋网下马凳间距不超过 **800 mm**；软地基或塑料膜上的钢丝马凳须带平底座。
- 搭接：直径不超过 12 mm 的钢筋搭接不少于 500 mm；12–16 mm 的不少于 700 mm；L 形转角处一根外侧钢筋须弯折并延伸不少于 500 mm（Table 4.2.11b）。

**3.3 混凝土**——Housing Provisions **4.2.10**（适用于 QLD 的全国文本）[S4]
- 按 AS 3600 生产；28 天强度不低于 20 MPa（N20）；最大骨料 20 mm；名义坍落度 100 mm；**不得加水**提高坍落度；按良好施工做法浇筑、振捣和养护。
- 说明部分建议：搅拌加水后 1.5 小时内卸完（除非用了缓凝剂）；振捣排除气泡但不要过振 [S4]。
- （⚠ 州差异：SA 的变体另有 7 天湿养护、32°C 以上不浇筑等规定，不适用于 QLD；QLD 的养护按工程师规格和 AS 3600，付费。）

**3.4 楼板高度与周边排水**——Housing Provisions **3.3.3**（NCC H2D2 引用 Part 3.3）[S3][S5]
- 楼板面高出室外完成面：低降雨强度地区或排水良好的砂地 **100 mm**；向外找坡的硬化地面 **50 mm**；**其他情况 150 mm**。
- 楼板周边地面须向外找坡：第一米内至少 **50 mm**（低降雨地区的硬化面等特定情况可为 25 mm）。

**3.5 白蚁防护**（QLD 有专门变体）
- NCC **QLD H1P3**：Class 1 建筑的白蚁防护措施设计寿命至少 **50 年**；否则必须便于补充或更换（例如板下化学喷淋管网系统）。说明部分明确举例：在直接落地的混凝土板下**人工喷洒化学药剂**，若药剂设计寿命不到 50 年，可能不满足要求 [S6]。
- **QLD H1D3(3)**：按 Housing Provisions Part 3.4 做即满足 H1P1 和 QLD H1P3 [S6]。
- Housing Provisions **QLD 3.4.2**：系统须按 QLD Table 3.4.2 选择，并符合 **AS 3660.1**（受 3.4.1(4)–(6) 限制）或通过 AS 3660.3 第 5 节测试；化学药剂须在主管机关（APVMA）的农药登记册上 [S7][S8]。
  - 符合 AS 2870 的板：板边外露（slab edge exposure）可作为周边防护；穿管和控制缝可用不锈钢网、碎石作部件或全系统，化学方式只能作为板下全系统（受 50 年/可补充规定限制）[S7]。
- **QLD 3.4.1(6)**：周边用化学防护的，须开沟、处理沟槽并用处理过的土回填，上面再做**不少于 50 mm 厚、300 mm 宽**（从外墙量起）的混凝土盖板 [S7]。
- 3.4.3：在电表箱等显眼位置固定**耐久标牌**，写明系统类型、安装日期、化学药剂的寿命（如适用）、今后检查的范围和频率建议 [S8]。
- 关键检查点：slab 检查时白蚁系统已就位 [S17]；final 检查要收集白蚁防护证书 [S16]；做白蚁防护的分包须持 QBCC termite management 执照（chemical 类不论金额都要执照）[S22]。
- 常见错误：完工后业主或景观工把花坛、覆盖物堆高，跨过防护层（NCC 说明部分举的「bridged or breached」例子）[S6]；穿管处没有做防护部件。

**3.6 法定检查**
- **footings** 检查：模板和钢筋就位、浇筑前；**slab** 检查：模板和钢筋就位、浇筑前 [S16]。独立住宅的基础钢筋、楼板模板与钢筋若由 competent person 协助检查，须是 **registered professional engineer** [S21]。

**常见错误**
- 马凳不够或被踩倒，钢筋贴在防潮膜上，保护层不足（这是 slab 检查最常见的不通过原因之一，行业经验，待证实）。
- 防潮膜被踩破、管线穿透处没封、搭接不足 200 mm。
- 现场加水提高坍落度（明文禁止）[S4]。
- 楼板高度不够 150 mm，后期室外地面又被抬高。

---

## 4. 框架（timber / steel framing）

**依据**
- NCC Volume Two **H1D6(4)**（QLD 变体）：木框架按以下标准之一（视情况）：**AS 1720.1**（木结构设计）、**AS 1720.5**（钉板桁架设计）、**AS 1684.2**（非气旋区）、**AS 1684.3**（气旋区）、**AS 1684.4**（非气旋区简化版）、**AS 1860.2**（刨花板地板安装）。另外，QLD 要求结构用木材的树种须列于昆州政府「Construction timbers in Queensland」（2017 年 12 月版）Book 2 的 Schedule A、B 或 C 中 [S2]。
- **H1D6(3)**：钢框架按 NASH Standard「Residential and Low-Rise Steel Framing」Part 1（设计）/ Part 2（设计方案）、AS 4100 或 AS/NZS 4600 [S2]。
- Housing Provisions Section 6 本身只含 subfloor ventilation（6.2）和 structural steel members（6.3）；木框架和钢框架的 DTS 直接引用上述标准 [S9]。
- 以上 AS 1684、AS 1720、NASH 均为付费标准。

**AS 1684 span tables 怎么用（方法，不含数值）**
1. 先确定**风级**（N1–N6 / C1–C4）：按 AS 4055（付费）或由工程师/设计文件给出；布里斯班大部分地块属非气旋区，但具体风级取决于地形、遮挡和高度（具体值见 AS 4055，付费；以批准图纸为准）。
2. 确定木材的**应力等级**（如 MGP10、F17 等）和尺寸，以及是否为 seasoned。
3. 在 AS 1684.2 的 span tables（补充资料 Supplement 中的表格，付费）里，按构件（椽、梁、托梁、过梁、墙骨、地梁等）、荷载情况（屋面质量、楼面荷载、承载宽度/面积）和间距查最大跨度。
4. 按风级和建筑尺寸计算所需**支撑（bracing）**：确定各方向的迎风面积和风压，求出所需支撑力，再按 AS 1684 选用支撑墙板类型和数量、布置位置（见 AS 1684.2，付费）。
5. 按风级和构件位置确定**抗拔连接（tie-down）**：从屋面到基础形成连续传力路径，选用连接件和螺栓规格（见 AS 1684.2，付费）。
6. 桁架由厂家按 AS 1720.5 设计，按厂家的桁架布置图和连接要求安装。
- 实务上，多数项目的框架尺寸、支撑和抗拔由结构工程师或桁架/框架供应商出图，builder 的责任是**按图施工并核对**。

**关键检查点**（QBCC checklist 和容差指南）
- 法定 **frame** 检查已通过 [S16][S17]；框架定位和尺寸与批准文件一致；所有结构构件和抗风支撑与批准文件一致；层高和门宽符合合同和法定最低要求；墙架和天花架垂直、方正 [S17]。
- 容差（完工后 12 个月内）：墙框/立柱在任意 2 m 高度内偏离垂直超过 **4 mm** 属缺陷；钉板前用 1.8 m 直尺检查，90% 面积偏差不超过 3 mm、其余不超过 4 mm；钢框架墙不得偏离垂直超过 H/600 [S18]。
- 木材收缩：未干燥木材收缩超过 10%、干燥木材超过 3% 属缺陷 [S18]。

**常见错误**（行业经验，结合 QBCC 指南）
- 支撑墙板钉距、数量不足，或位置与图纸不符；水电工开孔削弱支撑板或墙骨（待证实：具体开孔限制见 AS 1684，付费）。
- 抗拔连接漏装或用错规格，尤其是屋面到墙顶的连接。
- 过梁上方未留缝，门窗承受结构荷载（见第 7 节）。

---

## 5. 屋面（metal sheet roofing）

**依据**
- NCC Volume Two **H1D7(2)**：金属屋面按 **AS 1562.1**；或在风级不超过 **N3** 的地区按 Housing Provisions **Part 7.2**。瓦屋面按 AS 2050，或在 N3 以内、瓦符合 AS 2049、坡度 15°–35° 时按 Part 7.3 [S2]。
- 雨水槽和落水管：**H2D6** 按 AS/NZS 3500.3，或 Housing Provisions Part 7.4（须接到合规的雨水系统，且不含 box gutter）[S3]。
- QBCC 推荐的参考：AS 1562.1 和 **SA HB 39**（Metal roof and wall cladding installation），以及厂家的安装说明 [S10]（两者付费）。

**Housing Provisions Part 7.2 要点（N3 以内）** [S11]
- 坡度：按 Figure 7.2.3 满足各板型的最小坡度（具体数值见原文图表）。
- 紧固：穿透式（crest fastening）或隐藏式；Table 7.2.5：波纹板端跨每两个波峰加搭边、内跨每三个波峰加搭边；梯形板每个波峰；隐藏式每个波峰。紧固件金属须与屋面相容；夹扣与穿透式混用时，侧搭接要有防毛细作用构造。
- 铺设：尽量整张从檐口铺到屋脊；需要端搭接的，每一列从下往上铺完再铺下一列；端搭接坡度大于 15° 时不少于 **150 mm**，5°–15° 时不少于 **200 mm**；屋脊处每张板的波谷向上折 60°（stop end）。
- 泛水和盖板（7.2.7）：须为**专门制作、机器折弯**的金属件，材料与上下游屋面材料相容；接头搭接不少于 **75 mm**，顺水流方向搭接（原文另写有「fastened at intervals not more than 40 mm」）；砌体墙上的墙泛水和阶梯泛水用镀锌或锌铝楔块固定，每段两端及中间间距不超过 500 mm，顺流搭接不少于 75 mm；**铅泛水不得与预涂钢板或锌铝钢板一起用，也不得用于饮用水集水屋面**；防毛细折边：平面 10 mm/30°，其他面 10 mm/90° 或 135°。
- 穿透处：collar flashing 须让上方区域完全排水；安装后加设 trimmer 和支撑恢复屋面结构强度。
- 说明部分建议：侧搭接尽量背向主导风向；不要过度拧紧紧固件 [S11]。

**关键检查点**（QBCC checklist）[S17]
- 紧固件到位且与风级相符；sarking 搭接和铺设正确；泛水到位且材料相容；板材最小坡度和搭接正确；雨水槽和落水管位置符合批准文件。

**常见错误**（QBCC 缺陷通报）[S10][S19]
- 泛水和盖板缺失或安装不良，包括 scribing（裁切贴合）不正确。
- 屋面板端部没有做 weathering（板端折起）和防毛细构造。
- 紧固件类型、间距错误，侧搭接错位，密封不足。
- 穿透处密封草率。
- 材料不相容（尤其沿海地区）；不按厂家规格安装。
- 墙体空腔泛水装在防潮层外侧、阳台/露台 apron flashing 与墙体泛水衔接错误，导致水流进室内（QBCC 列为前十大缺陷之一）[S10]。
- 过度依赖密封胶而不是靠构造挡水（QBCC 强调「机械方式」防水）[S10]。

---

## 6. 湿区防水（wet areas）

**依据**
- NCC Volume Two **H4D2**：按 **AS 3740** 或 Housing Provisions **Part 10.2**，但湿区须按 10.2.1–10.2.6 和 10.2.12 保护 [S12]。
- **H4D3**：材料和安装满足 10.2.1–10.2.6 的防水/防潮分区要求，并且：符合 AS 3740 加 10.2.12，或符合 10.2.7–10.2.32 [S12]。
- AS 3740 为付费标准；Housing Provisions Part 10.2 免费。

**分区要求（Housing Provisions 10.2.2–10.2.5）** [S13]
| 部位 | 要求 |
|---|---|
| 淋浴区地面（含挡水坎、下沉） | waterproof |
| 淋浴区墙面 | waterproof，从楼面基层起**不低于 1800 mm** |
| 淋浴区墙角/接缝 | waterproof，接缝两侧各**不少于 40 mm** |
| 淋浴区墙地交接、穿透 | waterproof |
| 淋浴区以外地面 | 混凝土/纤维水泥板地面：water resistant；木质地面（含刨花板、胶合板）：waterproof |
| 淋浴区以外墙地交接 | waterproof；用泛水的，水平边不少于 40 mm |
| 非独立浴缸周边墙面 | 浴缸距墙 75 mm 以内的，浴缸以上不低于 150 mm 为 water resistant |
| 嵌入式浴缸 | 台面 waterproof 并在缸沿下设 waterstop；墙面缸沿以上不低于 150 mm waterproof |
| 洗手盆、水槽、洗衣槽靠墙 | 距墙 75 mm 以内的，以上 150 mm 为 water resistant；固定在墙上的墙缝 waterproof |
| 洗衣房、WC | 地面和墙地交接 water resistant |
| 设手持式妇洗器喷头的 WC | 地面 waterproof；墙面按 900 mm 半径分区（详见原文） |
- 淋浴在浴缸上方的，按淋浴要求处理 [S13]。

**材料（10.2.8–10.2.10）** [S13]
- waterproof：不锈钢；带防水接缝的柔性防水卷材地面；符合 **AS/NZS 4858** 的防水膜；防水密封胶。
- water resistant 基层：墙面——符合 AS 3600 并做防潮处理的混凝土、做防潮处理的水泥砂浆、符合 AS/NZS 2908.2 的纤维水泥板、防潮石膏板、符合 AS 3700 并做防潮处理的砌体；地面——符合 AS 3600 或 AS 2870 的混凝土、铺在结构楼面上的纤维水泥板。

**构造（10.2.12–10.2.19）** [S13]
- 地面找坡：有地漏的，连续坡度**不小于 1:80、不大于 1:50**。
- 淋浴区须有地漏并采用下沉、挡水坎或无门槛三种之一：
  - 下沉式：淋浴区最高完成面比外面低**不少于 25 mm**；
  - 挡水坎：用砌体、混凝土、加气混凝土或挤塑聚氨酯泡沫，**不得用木材**；坎体缝隙抹平、固定在地面并与墙密封后再刷防水膜；
  - 有门的无门槛淋浴：在淋浴区边缘设 waterstop，装淋浴屏的，waterstop 竖边高出完成面不少于 5 mm；
  - 开放式（无门）淋浴：waterstop 距花洒水平距离不少于 **1500 mm**，竖边与完成面齐平；或整个湿区地面做防水并排向地漏。
- 预制淋浴底盘：须有上翻边，墙面材料须插入翻边内侧，并有支撑防止变形开裂。

**关键检查点**
- 防水由持 QBCC **waterproofing** 执照的分包施工（QBCC 执照清单中有此类别）[S22]；final 检查要收集湿区防水证书 [S16]。
- 防水完成后、贴砖前拍照记录（带尺寸），检查墙面高度、转角加强、穿透处、waterstop 位置和收头 [S14][S20]。

**常见错误**（QBCC 检查发现最多的）[S20]
- 防水膜施工不正确（厚度、层数、养护不按厂家要求）；
- 龙头穿墙处未密封；
- waterstop 位置和收头错误；
- 转角和接缝未加强。

---

## 7. 外墙防潮层与门窗泛水

**7.1 砖饰面（masonry veneer）**——NCC **H2D4(2)** 按 AS 3700、AS 4773.1/.2 或 Housing Provisions **Part 5.7**；Part 5.2 砖饰面结构做法限风级 N3 以内、场地 A/S/M 类 [S2][S3]。Housing Provisions Part 5.7 要点 [S15]：
- 空腔净宽：砖饰面与框架外侧之间 **25–75 mm**（25 mm 要扣除墙膜、支撑板和管线后仍保持）；外叶砖挑出楼板边缘不超过 **15 mm**；楼板上的空腔须排水到室外。
- 防潮层/泛水材料：符合 AS/NZS 2904 等（见原文清单）。
- 位置：楼板上墙体底部一圈连续设置；屋面与砖墙交接处；门窗底部和顶部（顶部有宽度超过门窗以上砖墙高度 3 倍的屋檐遮挡的除外）；须贯通墙体并从外面可见。
- 防潮层高度：高出相邻地面不少于 **150 mm**；高出向外找坡的硬化或景观地面不少于 **75 mm**；有车棚、走廊遮挡且符合 3.3.3(b) 的，不少于 50 mm（低降雨地区另有规定）。
- 窗台和窗顶泛水：两侧各伸出洞口边**不少于 150 mm**；窗台泛水不低于窗台砖下一皮，窗顶泛水不高于洞口以上 300 mm；在空腔内上翻不少于 150 mm；嵌入外叶砖不少于 30 mm；固定在窗框或墙架上。
- 排水孔（weepholes）：紧贴泛水上方一皮砖开竖缝，高不少于 **50 mm**，间距不超过 **1.2 m**；宽度小于 1.2 m 的门窗顶、窗台下方等可不设。
- 检查点（QBCC checklist）：伸缩缝和控制缝位置正确；空腔清理干净；排水孔通畅且位置正确；防潮层到位；砖墙垂直 [S17]。

**7.2 板材外墙（timber / composite / sheet cladding）**——NCC **H1D7(4)** 按 Housing Provisions **Part 7.5** [S2]。要点 [S23]：
- 外露洞口的泛水（7.5.6）：材料符合 AS/NZS 2904；洞口**底部、顶部和两侧**都要做；尽可能伸出洞口边**不少于 110 mm**；固定在窗框和墙架上；顶部和底部泛水排到墙外侧；接头顺流搭接不少于 75 mm 并在搭接处打密封胶；泛水压入外墙板下不少于 25 mm；有宽度超过洞口以上墙高 3 倍的屋檐遮挡时，顶部可不做。
- 外墙板底部与完成地面的距离（7.5.7）：一般 **150 mm**；低降雨或排水良好砂地 100 mm；向外找坡的硬化地面 50 mm；架空楼面的外墙板须延伸到地梁以下不少于 50 mm。

**常见错误**（QBCC 缺陷通报）[S10]
- 空腔泛水装在防潮层外面，或钉在木框上再翻到砖墙外侧，水直接流进室内。
- 窗台泛水两端没有上翻或伸出不够，水从窗角渗入（行业经验，待证实）。

---

## 8. 门窗安装

**依据**
- NCC Volume Two **H1D8(1)**：外墙玻璃组件（窗、有框推拉门和平开门、百叶、一体框窗墙）按 **AS 2047** 设计制造，并按 AS 2047 安装；在 AS 4055 第 1.2 条的几何限制内且风级不超过 N3 的，也可按 Housing Provisions **Part 8.2** 安装 [S2]。H2D7 规定门窗防水同样按 H1D8(1) [S3]。人体冲击区玻璃按 AS 1288（Part 8.4）（付费）。

**Housing Provisions 8.2.2 要点** [S24]
- 结构荷载**不得**传给窗组件。
- 窗组件顶部与承重框架或砌体之间至少留 **10 mm** 缝隙；宽洞口可加大，以容纳框架沉降。
- 垫块（如使用）放在两侧和底部，固定牢靠使窗框两侧和底边保持平直，且**不得压在泛水上**。
- 说明部分建议：窗要垂直、方正（对角线相等）；铝窗台接触砂浆的，用沥青膜或含铬酸锌的涂料/密封胶隔离 [S24]。

**关键检查点**（QBCC checklist）[S17]
- 外门窗的风荷载等级正确；门窗泛水到位；人体冲击区使用正确的玻璃；取得安装和玻璃证书（final 检查需要玻璃证书 [S16]）。
- 容差和缺陷判断见 QBCC Standards and Tolerances Guide 第 9 节（门窗）[S18]。

**常见错误**
- 窗顶没有留缝，框架沉降后窗框变形、推拉不畅、密封失效（Housing Provisions 说明部分所述的风险）[S24]。
- 门窗风级低于设计风级（采购时只看尺寸，不核对 AS 2047 等级标签；行业经验，待证实）。

---

## 9. 省钱要点（合法）
1. **场地分类决定楼板做法和成本**：先做土工报告，A/S/M 类且平面规整的，可以用 Housing Provisions 的 DTS 做法；平面设计成规整矩形、只有一个内凹角，能留在 DTS 范围内（H1D4(2)）[S2]。
2. **屋面和湿区一次做对**：这两项是 QBCC 最常见、整改最贵的缺陷 [S19][S20]；在贴砖前、封板前留出自检和拍照时间，成本很低。
3. **用免费的 Housing Provisions 做检查清单**：泛水尺寸、防潮膜搭接、保护层、找坡等数值都在免费原文中，可以直接做成现场检查表（见 `05-工具与模板/`）。
4. **白蚁系统选型要看 50 年寿命或可补充**：选错（例如寿命不足的人工喷洒）可能在 final 检查时不通过，返工更贵 [S6]。

---

## 待证实 / 待确认清单
- 布里斯班常见地块的风级和场地类别分布：未查到官方汇总，以每块地的设计文件和土工报告为准（待证实）。
- 支撑、抗拔、开孔限制的具体数值：见 AS 1684.2 / AS 4055，付费，本文不写。
- 屋面泛水「fastened at intervals not more than 40 mm」原文如此，建议对照 AS 1562.1 / HB 39 确认含义（待确认）。
- 混凝土养护时间（QLD）：Housing Provisions 全国文本未规定天数，按工程师规格和 AS 3600（付费），待证实。
- NCC 2025 在昆州实施后的防水、楼板等变化：待 2027 年换版前重新核对。
- 由测量师放线是否为法定要求：待证实（法定的是退界检查须由 cadastral surveyor 协助时）。

## 来源
- [S1] NCC 2022 Volume Two（总入口）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-two ｜NCC 2022｜访问 2026-11-21
- [S2] NCC 2022 Volume Two, Part H1 Structure（H1D3、H1D4、H1D5、H1D6 含 QLD 变体、H1D7、H1D8）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-two/h-class-1-and-10-buildings/part-h1-structure ｜NCC 2022｜访问 2026-11-21
- [S3] NCC 2022 Volume Two, Part H2 Damp and weatherproofing（H2D2、H2D4、H2D6、H2D7、H2D8）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-two/h-class-1-and-10-buildings/part-h2-damp-and-weatherproofing ｜NCC 2022｜访问 2026-11-21
- [S4] ABCB Housing Provisions, Part 4.2 Footings, slabs and associated elements（4.2.2、4.2.3、4.2.4、4.2.8、4.2.10、4.2.11）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/4-footings-and-slabs/part-42-footings-slabs-and-associated-elements ｜2022 版｜访问 2026-11-21
- [S5] ABCB Housing Provisions, Part 3.3 Drainage（3.3.3）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/3-site-preparation/part-33-drainage ｜2022 版｜访问 2026-11-21
- [S6] NCC 2022 Volume Two, Queensland variations – Part H1 Structure（QLD H1P3、QLD H1D3）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-two/7-queensland/h1-structure ｜NCC 2022｜访问 2026-11-21
- [S7] ABCB Housing Provisions, Queensland variations – 3.4 Termite risk management（QLD 3.4.1、QLD 3.4.2、QLD Table 3.4.2）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/7-queensland/34-termite-risk-management ｜2022 版｜访问 2026-11-21
- [S8] ABCB Housing Provisions, Part 3.4 Termite risk management（3.4.1、3.4.3）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/3-site-preparation/part-34-termite-risk-management ｜2022 版｜访问 2026-11-21
- [S9] ABCB Housing Provisions, Part 6.1 Scope and application of Section 6. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/6-framing/part-61-scope-and-application-section-6 ｜2022 版｜访问 2026-11-21
- [S10] Roof flashings. QBCC. https://www.qbcc.qld.gov.au/news/roof-flashings ｜Last reviewed 2021-01-11｜访问 2026-11-21
- [S11] ABCB Housing Provisions, Part 7.2 Sheet roofing（7.2.3、7.2.5、7.2.6、7.2.7）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/7-roof-and-wall-cladding/part-72-sheet-roofing ｜2022 版｜访问 2026-11-21
- [S12] NCC 2022 Volume Two, Part H4 Health and amenity（H4D2、H4D3）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/volume-two/h-class-1-and-10-buildings/part-h4-health-and-amenity ｜NCC 2022｜访问 2026-11-21
- [S13] ABCB Housing Provisions, Part 10.2 Wet area waterproofing（10.2.2–10.2.19）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-102-wet-area-waterproofing ｜2022 版｜访问 2026-11-21
- [S14] Clearer accountability for defective work—refined DTR process（隐蔽前拍照建议）. QBCC. https://www.qbcc.qld.gov.au/news/clearer-accountability-defective-work-refined-dtr-process ｜2026-03-27｜访问 2026-11-21
- [S15] ABCB Housing Provisions, Part 5.7 Weatherproofing of masonry（5.7.2–5.7.5）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/5-masonry/part-57-weatherproofing-masonry ｜2022 版｜访问 2026-11-21
- [S16] Stages of a building inspection. Business Queensland. https://www.business.qld.gov.au/industries/building-property-development/building-construction/approvals-inspections/stages ｜Last reviewed 2022-07-26｜访问 2026-11-21
- [S17] Supervision and quality control（Supervisor's checklist for domestic building work）. QBCC. https://www.qbcc.qld.gov.au/worksite-building-practice/site-responsibilities/supervision-quality-control ｜Last reviewed 2023-06-11｜访问 2026-11-21
- [S18] Standards and Tolerances Guide (Queensland, December 2023). QBCC. https://www.qbcc.qld.gov.au/sites/default/files/documents/guide-standards-tolerances.pdf ｜2023-12｜访问 2026-11-21
- [S19] Roof cladding defects: Helping licensees deliver quality and prevent common issues. QBCC. https://www.qbcc.qld.gov.au/news/roof-cladding-defects-helping-licensees-deliver-quality-prevent-common-issues ｜Last reviewed 2026-03-24｜访问 2026-11-21
- [S20] Waterproofing done right: what you need to know in 2025. QBCC. https://www.qbcc.qld.gov.au/news/waterproofing-done-right-what-you-need-know-2025 ｜Last reviewed 2025-08-11｜访问 2026-11-21
- [S21] Building inspections by competent persons and cadets. Business Queensland. https://www.business.qld.gov.au/industries/building-property-development/building-construction/approvals-inspections/competent-persons-cadets ｜Last reviewed 2022-06-30｜访问 2026-11-21
- [S22] Technical qualifications（执照类别清单，含 Waterproofing、Termite management—chemical/physical）. QBCC. https://www.qbcc.qld.gov.au/licences/apply-licence/eligibility-requirements/technical-qualifications ｜Last reviewed 2024-07-01｜访问 2026-11-21；「不论金额都需执照」见 Advertising 页 https://www.qbcc.qld.gov.au/running-your-business/advertising （Last reviewed 2021-08-30）
- [S23] ABCB Housing Provisions, Part 7.5 Timber and composite wall cladding（7.5.6、7.5.7）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/7-roof-and-wall-cladding/part-75-timber-and-composite-wall-cladding ｜2022 版｜访问 2026-11-21
- [S24] ABCB Housing Provisions, Part 8.2 Windows and external glazed doors（8.2.2）. ABCB. https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/8-glazing/part-82-windows-and-external-glazed-doors ｜2022 版｜访问 2026-11-21
