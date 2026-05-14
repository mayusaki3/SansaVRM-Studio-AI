<!--
HLDocS:LLM-MANAGED
doc_id: doc-20260514-000028Z-SVSA
lang: ja-JP
canonical_title: local server仕様
canonical_document: true
document_type: spec
transport: [download, ui_copy]
-->

[目次](../目次.md) > 仕様 > local server仕様

# local server仕様

## 1. 目的

本仕様は、SansaVRM Studio AI のブラウザ UI および外部連携のための local server を定義する。

## 2. 前提

- local server は project workspace を操作する API を提供する。
- 初期状態では localhost のみで待ち受ける。
- LAN 公開は明示設定がある場合のみ許可する。
- local server は AI 実行環境がなくても起動できる。
- 初期 PoC は FastAPI による実装を許容する。

## 3. 動作モード

### 3.1 local mode

- bind address は 127.0.0.1 または localhost とする。
- 既定モードとする。

### 3.2 lan mode

- 利用者が明示指定した場合のみ有効にする。
- bind address と port を設定可能とする。

### 3.3 restricted mode

- 認証またはアクセス制御を有効にしたモードとする。
- 初期 PoC では仕様定義のみとする。

## 4. API

### 4.1 health

```text
GET /api/health
```

目的:

- server が起動していることを確認する。

### 4.2 project summary

```text
GET /api/project
```

目的:

- 現在開いている project の概要を返す。

### 4.3 artifacts

```text
GET /api/artifacts
```

目的:

- artifact registry の一覧を返す。

### 4.4 workflow runs

```text
GET /api/workflow-runs
```

目的:

- workflow run の一覧を返す。

### 4.5 workflow dependency graph

```text
GET /api/workflow-graph
```

目的:

- artifact dependency graph を返す。

## 5. 禁止事項

- local mode で外部ネットワークへ公開してはならない。
- project workspace なしで project API を成功扱いしてはならない。
- 制限付き素材を API 応答で無制限に返してはならない。
- external service opt-in なしに外部 AI サービスへ接続してはならない。

## 6. 次アクション

- FastAPI PoC を実装する。
- health / project / artifact / workflow API のテストを作成する。
- Web UI の最小構成を検討する。

---

[目次](../目次.md) > 仕様 > local server仕様
