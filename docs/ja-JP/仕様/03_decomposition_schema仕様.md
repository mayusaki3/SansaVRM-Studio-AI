<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260513-000013Z-SVSA
lang: ja-JP
canonical_title: decomposition schema仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > decomposition schema仕様

# decomposition schema仕様

## 1. 目的

本仕様は、Studio AI の AI 前処理において使用する decomposition schema を定義する。

本 schema は、人型キャラクター専用ではなく、汎用 asset decomposition を目的とする。

## 2. 前提

- decomposition は 3D 生成前処理を目的とする。
- decomposition は image / video generation にも利用する。
- decomposition は SansaVRM layered asset structure 候補へ接続する。
- decomposition 結果は Core semantic identity そのものではない。
- decomposition は AI 推定を含む場合がある。

## 3. asset_type

以下を標準 asset_type 候補とする。

- humanoid_character
- non_humanoid_character
- animal
- creature
- robot
- mech
- vehicle
- furniture
- building
- prop
- environment_asset

## 4. layer schema

## 4.1 layer

各 layer は以下を持つ。

```json
{
  "layer_id": "outer_armor",
  "layer_type": "outer_surface",
  "source": "visible",
  "confidence": 0.92,
  "editable": true
}
```

## 4.2 layer_type

標準 layer_type 候補:

- base_structure
- outer_surface
- covering
- appendage
- accessory
- internal_mechanism
- movable_part
- hidden_part
- material_region
- effect_region

## 4.3 source

source は layer の由来を表す。

標準 source 候補:

- visible
- hidden
- inferred
- generated
- author_verified

## 5. material_region

material_region は表面材質を表す。

候補:

- skin
- fur
- feather
- scale
- shell
- armor
- metal_panel
- fabric
- leather
- glass
- emission_part

## 6. multi-view

multi-view は以下を持つ。

- front
- back
- left
- right
- top
- bottom
- detail

asset_type に応じて必要 view を切り替える。

## 7. downstream generation

decomposition 出力は以下へ利用できる。

- 3D generation
- image generation
- video generation
- pose variation generation
- expression variation generation
- clothing variation generation
- material reference generation

## 8. provenance

decomposition 由来情報は provenance として保持する。

例:

```json
{
  "decomposition": {
    "model": "Qwen2.5-VL",
    "segmentation": "SAM2",
    "generated_at": "2026-05-13T00:00:00Z"
  }
}
```

## 9. Validation

decomposition schema は以下を validation する。

- asset_type validity
- layer_type validity
- source validity
- confidence range
- duplicated layer_id
- unsupported layer mapping

## 10. 次アクション

- authoring workflow を定義する。
- local AI runtime を定義する。
- segmentation PoC を作成する。

---

[目次](../目次.md) > 仕様 > decomposition schema仕様
