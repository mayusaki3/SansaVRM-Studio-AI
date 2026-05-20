<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260516-000041Z-SVSA
lang: ja-JP
canonical_title: workflow graph execution仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > workflow graph execution仕様

# workflow graph execution仕様

## 1. 目的

本仕様は、SansaVRM Studio AI における workflow graph を executable semantic graph として扱うための実行モデルを定義する。

## 2. 基本方針

workflow graph は単なる表示用データではなく、以下を統合する workspace authority とする。

- workflow execution
- artifact dependency
- provenance tracking
- governance propagation
- diagnostics tracing
- workspace reconstruction

## 3. graph model

workflow graph は node と edge から構成する。

```json
{
  "nodes": [],
  "edges": [],
  "metadata": {}
}
```

## 4. node types

初期 node type は以下とする。

- workflow
- step
- artifact
- governance
- provenance
- diagnostics

## 5. edge types

初期 edge type は以下とする。

- dependency
- input
- output
- derived_from
- governed_by
- reviewed_by
- diagnostic_for

## 6. node lifecycle

node は以下の lifecycle state を持つ。

### 6.1 pending

未実行状態。

### 6.2 ready

依存関係が満たされ、実行可能な状態。

### 6.3 running

実行中。

### 6.4 completed

正常完了。

### 6.5 failed

実行失敗。diagnostics node を持つ。

### 6.6 blocked

governance restriction または dependency failure により実行できない状態。

## 7. execution model

実行順序:

```text
workflow graph
 ↓
dependency resolution
 ↓
execution planning
 ↓
step execution
 ↓
artifact generation
 ↓
governance update
 ↓
provenance update
 ↓
graph update
```

## 8. governance propagation

governance restriction は graph edge を通じて伝播する。

例:

```text
adult_only body
 ↓ assembly
assembled asset = adult_only
```

Studio AI は restriction を独自に緩和してはならない。

## 9. provenance propagation

artifact 生成時には provenance edge を追加する。

例:

```text
source image
 ↓ decomposition
component mesh
 ↓ assembly
assembled SansaVRM
```

## 10. diagnostics tracing

failure / blocked の理由は diagnostics node として graph に保持する。

例:

```text
export denied
 ↑ governed_by
redistribution restricted component
 ↑ derived_from
source SansaVRM_B
```

## 11. graph query

初期 query 候補:

- find_provenance_chain
- find_restriction_source
- find_derived_artifacts
- find_workflow_dependencies
- find_blocked_nodes
- find_diagnostics_for_node

## 12. UI 表示

UI は graph を以下の用途で使用する。

- workflow execution viewer
- provenance viewer
- governance debugger
- artifact lineage viewer
- diagnostics viewer

## 13. 保存

workflow graph は project state の一部として保存する。

候補ファイル:

```text
workflow_graph.json
```

## 14. 禁止事項

- workflow graph を表示専用キャッシュとして扱ってはならない。
- artifact 生成時に provenance edge を記録しないで進めてはならない。
- governance restriction を graph に反映せず workflow を進めてはならない。
- blocked / failed の原因を diagnostics として記録せずに失敗扱いしてはならない。

## 15. 次アクション

- workflow graph model PoC を実装する。
- graph query PoC を実装する。
- workflow engine と graph update を接続する。
- UI graph viewer と接続する。

---

[目次](../目次.md) > 仕様 > workflow graph execution仕様
