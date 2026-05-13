<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260513-000017Z-SVSA
lang: ja-JP
canonical_title: decomposition schemaテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > decomposition schemaテスト仕様

# decomposition schemaテスト仕様

## 1. 目的

本テスト仕様は decomposition schema の validation を確認する。

## 2. テストケース

### TC-DEC-001

目的:

asset_type が humanoid_character の場合に validation が通ることを確認する。

入力:

```json
{
  "asset_type": "humanoid_character"
}
```

期待結果:

- validation success

---

### TC-DEC-002

目的:

未知の asset_type を rejection できることを確認する。

入力:

```json
{
  "asset_type": "unknown_asset_type"
}
```

期待結果:

- validation error

---

### TC-DEC-003

目的:

source=inferred を許可できることを確認する。

入力:

```json
{
  "source": "inferred"
}
```

期待結果:

- validation success

---

### TC-DEC-004

目的:

duplicated layer_id を rejection できることを確認する。

入力:

```json
{
  "layers": [
    {
      "layer_id": "body"
    },
    {
      "layer_id": "body"
    }
  ]
}
```

期待結果:

- validation error

---

### TC-DEC-005

目的:

material_region=fur を許可できることを確認する。

入力:

```json
{
  "material_region": "fur"
}
```

期待結果:

- validation success

---

## 3. カバレッジ観点

- asset_type
- layer_type
- source
- material_region
- duplicated layer_id
- inferred layer

---

[目次](../目次.md) > テスト > decomposition schemaテスト仕様
