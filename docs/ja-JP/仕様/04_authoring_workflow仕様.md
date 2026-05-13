<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260513-000014Z-SVSA
lang: ja-JP
canonical_title: authoring workflow仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > authoring workflow仕様

# authoring workflow仕様

## 1. 目的

本仕様は、Studio AI における authoring workflow を定義する。

## 2. lifecycle

Studio AI は以下の lifecycle を扱う。

```text
input
  ↓
analysis
  ↓
decomposition
  ↓
multi-view generation
  ↓
review
  ↓
generation support
  ↓
validation
  ↓
distribution preparation
  ↓
export
```

## 3. input

入力候補:

- prompt
- single image
- multiple image sheet
- concept art
- sketch
- screenshot
- photo
- reference pack

## 4. analysis

analysis は以下を扱う。

- asset_type estimation
- visible structure detection
- segmentation candidate detection
- hidden area estimation
- material estimation
- copyright risk pre-check

## 5. decomposition

入力 asset を layer 単位へ分解する。

候補:

- base_structure
- outer_surface
- covering
- internal_mechanism
- accessory
- movable_part

## 6. multi-view generation

multi-view generation は以下を生成する。

- front
- back
- left
- right
- top
- detail

## 7. review

review は以下を扱う。

- user correction
- layer merge
- layer split
- prompt adjustment
- inferred layer confirmation
- policy confirmation

## 8. generation support

Studio AI は以下への generation support を提供する。

- 3D generation
- image generation
- video generation
- character sheet generation
- pose generation
- expression generation

## 9. validation

validation は以下を扱う。

- decomposition validation
- topology validation
- rigging validation
- integrity validation
- copyright risk assessment
- provenance validation

## 10. distribution preparation

distribution preparation は以下を扱う。

- export profile selection
- policy rewrite
- metadata filtering
- hidden mesh bake
- material merge
- irreversible export warning

## 11. export

export 候補:

- SansaVRM
- VRM
- glTF
- image pack
- video pack
- prompt pack
- report package

## 12. 禁止事項

- review を通さず inferred layer を正本扱いしない。
- policy rewrite 後の情報を validation なしに distribution state 化しない。
- irreversible export 後の情報を reversible asset として扱わない。

---

[目次](../目次.md) > 仕様 > authoring workflow仕様
