---
title: A轴生成脊柱·跨仓同步回执 v1
module: source-receipt
layer: sources
type: governance-receipt
status: proposed
observed_at: "2026-08-07"
---

# A 轴生成脊柱 · 跨仓同步回执 v1

## 1. 目的

记录 `yuanli-trilogy-max` 本轮公共叙事更新究竟消费了哪个上游候选、哪些内容已写入、哪些事实仍未建立，防止公共叙事仓反向成为正典源。

## 2. 上游 Soul 堆叠 PR

截至 2026-08-07，本轮上游仍是 **Draft / unmerged**：

| 顺序 | Soul PR | 作用 | 状态 |
|---|---|---|---|
| PR-1 | `moonstachain/yuanli-strategy-soul#459` | 冻结 A 轴正典：母体第一因、资产终态、四个第一性问题、四个教学动作 | Draft / unmerged |
| PR-2 | `moonstachain/yuanli-strategy-soul#460` | A1-A4 contracts / Schema / golden queries / drift CI | Draft / unmerged |
| PR-3 | `moonstachain/yuanli-strategy-soul#461` | 教材、Teaching-ready、投影准备与 B4 四权漂移净化 | Draft / unmerged |

因此本仓当前只能宣称：

> **已完成对上游候选正典的公共叙事蒸馏提案。**

不得宣称：

> Soul 已正式合并或发布本轮新正典。

## 3. 本仓实际同步文件

```text
README.md
00-canon/06-十二模块总图.md
10-yuanli-asset/10-卷首-原力资产.md
10-yuanli-asset/11-A1-发现母体.md
10-yuanli-asset/12-A2-回到母体.md
10-yuanli-asset/13-A3-获得原力.md
10-yuanli-asset/14-A4-显化原力.md
20-yuanli-venture/24-B4-壁垒锁定.md
50-spine/53-自诊-你卡在哪一关.md
80-governance/83-术语表.md
```

没有新增平行 A1-A4 文件，55 篇主结构不因本轮同步扩容。

## 4. 本轮冻结的公共表达

```text
A1 发现母体 · 找源
什么持续生成我的不同？

A2 回到母体 · 归源
哪些东西真正属于我，哪些只是外界塑造？

A3 获得原力 · 炼源
如何把潜在生成结构训练成真实能力？

A4 显化原力 · 证源
这种原力进入真实世界后，是否真正创造价值？
```

层级：

```text
原力母体 = 生成第一因
原力资产 = 第一部终态
找源/归源/炼源/证源 = 教学动作
发现母体/回到母体/获得原力/显化原力 = 正典模块名
```

## 5. B4 同步净化

本轮公共仓同时清理了高可见度旧“六层壁垒”表达。

唯一有效的壁垒分类：

```text
虚壁垒 = 心智控制权
实壁垒 = 交付控制权
入壁垒 = 入口控制权
出壁垒 = 留存控制权
```

```text
飞轮 = 四权相互强化机制
母体 = 四权差异生成源头
```

二者不得作为第五、第六类壁垒。

## 6. 诚实状态

```yaml
upstream_soul_pr_459: DRAFT_UNMERGED
upstream_soul_pr_460: DRAFT_UNMERGED
upstream_soul_pr_461: DRAFT_UNMERGED
public_narrative_files: UPDATED_ON_BRANCH
public_canon_authority: NONE
live_reader_validation: NOT_ESTABLISHED
market_outcome: NOT_ESTABLISHED
feishu_projection: NOT_RUN
compounding: NOT_PROVEN
publication_readiness: BLOCKED_PENDING_UPSTREAM_MERGE_AND_REVIEW
```

## 7. 合并门

本 PR 合并前至少确认：

1. Soul #459/#460/#461 的最终合并内容没有改变四个第一性问题与层级边界；
2. 若 Soul 合并 SHA 与本回执观察的候选不同，先更新本仓来源说明再合并；
3. 公共仓不得把 `candidate` 语言改成“已冻结为 Soul Canon”，除非上游确已 merge；
4. 不因公共文章完成，提升任何 A1-A4 live validation / Outcome；
5. B4 继续保持四大控制权，不恢复六类并列表达。
