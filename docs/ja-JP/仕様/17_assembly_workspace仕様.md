<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260516-000038Z-SVSA
lang: ja-JP
canonical_title: assembly workspace仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > assembly workspace仕様

# assembly workspace仕様

## 1. 目的

assembly workspace は、SansaVRM component を interactive に選択し、governance-aware assembly を行うための workspace state を提供する。

## 2. 基本方針

- component 単位で governance を評価する。
- assembly deny component は選択不可にする。
- provenance graph を保持する。
- conflict diagnostics を保持する。
- assembly 前に governance merge validation を行う。

## 3. 管理対象

- selected components
- provenance graph
- assembly conflicts
- governance diagnostics
- assembly preview
- merged restriction state

## 4. selection state

slot 単位で selected component を保持する。

例:

```json
{
  "body": "body-001",
  "hair": "hair-001",
  "clothing": "clothing-001"
}
```

## 5. provenance graph

assembly provenance を graph 化する。

例:

```text
assembled asset
 ├ body -> SansaVRM_A
 ├ hair -> SansaVRM_B
 └ clothing -> SansaVRM_C
```

## 6. governance validation

selection 時に governance evaluation を行う。

禁止対象:

- decomposition denied component
- assembly denied component
- export denied component
- redistribution denied component

## 7. conflict diagnostics

候補:

- commercial conflict
- redistribution conflict
- ai_training conflict
- age_rating conflict
- distribution_state conflict

## 8. UI

UI は以下を表示する。

- component list
- source SansaVRM
- governance state
- selection state
- denied reason
- provenance graph
- conflict diagnostics

## 9. 次アクション

- UI selection state 接続
- provenance graph visualization
- assembly artifact generation
- merged governance preview

---

[目次](../目次.md) > 仕様 > assembly workspace仕様
