<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260516-000040Z-SVSA
lang: ja-JP
canonical_title: assembly REST API仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > assembly REST API仕様

# assembly REST API仕様

## 1. 目的

assembly workspace を UI / workflow / external integration から利用可能にするため、REST API を提供する。

## 2. 基本方針

- governance-aware selection を行う。
- assembly deny component は API レベルで拒否する。
- provenance graph を API から取得可能にする。
- assembly preview を API から取得可能にする。
- diagnostics を API から取得可能にする。

## 3. API一覧

### GET /api/assembly/components

assembly 対象 component 一覧取得。

### POST /api/assembly/select-component

assembly slot に component を選択する。

### GET /api/assembly/selected-components

現在の selection state を取得する。

### GET /api/assembly/preview

assembly preview を取得する。

### GET /api/assembly/provenance-graph

provenance graph を取得する。

### GET /api/assembly/conflicts

assembly conflict diagnostics を取得する。

## 4. selection request

```json
{
  "slot_name": "body",
  "component_id": "body-001"
}
```

## 5. selection validation

selection 時に以下を評価する。

- governance rule
- assembly permission
- component restriction
- conflict detection
- provenance consistency

## 6. deny behavior

assembly deny component の場合:

- HTTP 400 を返す。
- governance diagnostics を追加する。
- selection state を変更しない。

## 7. preview response

```json
{
  "selected_components": {},
  "provenance_graph": {},
  "conflicts": []
}
```

## 8. provenance graph

例:

```text
assembled asset
 ├ body -> SansaVRM_A
 ├ hair -> SansaVRM_B
 └ clothing -> SansaVRM_C
```

## 9. conflict diagnostics

候補:

- commercial conflict
- redistribution conflict
- age rating conflict
- ai training conflict
- assembly restriction conflict

## 10. 次アクション

- local_server.py に REST API を追加する。
- UI selection state と接続する。
- provenance graph visualization と接続する。
- assembly artifact generation に接続する。

---

[目次](../目次.md) > 仕様 > assembly REST API仕様
