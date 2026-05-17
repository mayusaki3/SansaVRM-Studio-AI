<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260516-000039Z-SVSA
lang: ja-JP
canonical_title: assembly workspaceテスト仕様
canonical_document: true
document_type: testspec
transport: [download, ui_copy]
-->

[目次](../目次.md) > テスト > assembly workspaceテスト仕様

# assembly workspaceテスト仕様

## 1. 目的

assembly workspace の component selection / provenance graph / governance validation / conflict diagnostics を検証する。

## 2. テストケース

### ASM-001

目的:

assembly allowed component が選択できること。

期待結果:

- selected_components に追加される。
- provenance graph に追加される。

### ASM-002

目的:

assembly denied component が選択できないこと。

期待結果:

- selection が拒否される。
- diagnostics が出力される。

### ASM-003

目的:

provenance graph が source SansaVRM を保持すること。

期待結果:

- provenance graph に source_sansavrm が出力される。

### ASM-004

目的:

assembly conflict diagnostics が保持されること。

期待結果:

- conflicts に conflict entry が追加される。

### ASM-005

目的:

selection API が current selection state を更新すること。

期待結果:

- selected component state が更新される。
- preview API に反映される。

---

[目次](../目次.md) > テスト > assembly workspaceテスト仕様
