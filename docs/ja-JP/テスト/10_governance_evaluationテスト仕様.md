<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260515-000037Z-SVSA
lang: ja-JP
canonical_title: governance evaluationテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > governance evaluationテスト仕様

# governance evaluationテスト仕様

## 1. 目的

governance evaluation の workflow / UI / assembly / conversion 制御を検証する。

## 2. テストケース

### GOV-001

目的:

decomposition denied asset の component extraction が拒否されること。

入力:

```text
asset:
  decomposition=deny
```

期待結果:

- component extraction workflow が拒否される。
- extract button が disabled になる。
- diagnostics が出力される。

### GOV-002

目的:

assembly denied component が assembly source に選択できないこと。

入力:

```text
component:
  assembly=deny
```

期待結果:

- component selection UI が disabled になる。
- assembly workflow が失敗する。

### GOV-003

目的:

conversion denied export target が拒否されること。

入力:

```text
policy:
  export_fbx=deny
```

期待結果:

- FBX export button が disabled になる。
- conversion workflow が失敗する。

### GOV-004

目的:

複数 source asset の restriction conflict が検出されること。

入力:

```text
asset A:
  commercial=allow

asset B:
  commercial=deny
```

期待結果:

- conflict diagnostics が出力される。
- assembly governance result が restrictive priority になる。

### GOV-005

目的:

分解不可 asset の component が個別 export されないこと。

期待結果:

- component export workflow が拒否される。
- diagnostics が出力される。

## 3. 次アクション

- governance evaluation PoC 実装。
- UI button disable 連携。
- workflow diagnostics 連携。

---

[目次](../目次.md) > テスト > governance evaluationテスト仕様
