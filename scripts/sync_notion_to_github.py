#!/usr/bin/env python3
"""
Sincroniza as páginas da base "Biblioteca de Conhecimento" (Notion)
para arquivos Markdown dentro deste repositório.

Organização gerada:
    estudos/<categoria>/<titulo>.md

Cada arquivo tem um front-matter com as propriedades da página e,
em seguida, o conteúdo convertido para Markdown.

Variáveis de ambiente esperadas:
    NOTION_TOKEN        -> token da integração interna do Notion
    NOTION_DATABASE_ID  -> ID da base "Biblioteca de Conhecimento"
    OUTPUT_DIR          -> pasta de saída (padrão: "estudos")

Uso local:
    NOTION_TOKEN=xxx NOTION_DATABASE_ID=yyy python sync_notion_to_github.py
"""

import os
import re
import sys
import unicodedata
import requests

NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"


def slugify(text: str) -> str:
    text = text or "sem-titulo"
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "sem-titulo"


def notion_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def query_all_pages(database_id: str, headers: dict) -> list:
    """Busca todas as páginas da base, seguindo a paginação."""
    pages = []
    payload = {"page_size": 100}
    while True:
        resp = requests.post(
            f"{API_BASE}/databases/{database_id}/query",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        pages.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        payload["start_cursor"] = data["next_cursor"]
    return pages


def get_children_blocks(block_id: str, headers: dict) -> list:
    """Busca todos os blocos filhos de um bloco/página, seguindo a paginação."""
    blocks = []
    params = {"page_size": 100}
    while True:
        resp = requests.get(
            f"{API_BASE}/blocks/{block_id}/children",
            headers=headers,
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        blocks.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        params["start_cursor"] = data["next_cursor"]
    return blocks


def rich_text_to_md(rich_text: list) -> str:
    parts = []
    for rt in rich_text or []:
        text = rt.get("plain_text", "")
        ann = rt.get("annotations", {})
        if ann.get("code"):
            text = f"`{text}`"
        if ann.get("bold"):
            text = f"**{text}**"
        if ann.get("italic"):
            text = f"*{text}*"
        if ann.get("strikethrough"):
            text = f"~~{text}~~"
        href = rt.get("href")
        if href:
            text = f"[{text}]({href})"
        parts.append(text)
    return "".join(parts)


def block_to_md_line(block: dict, depth: int) -> str:
    btype = block.get("type")
    data = block.get(btype, {}) or {}
    indent = "  " * depth
    text = rich_text_to_md(data.get("rich_text", [])) if "rich_text" in data else ""

    if btype == "heading_1":
        return f"# {text}"
    if btype == "heading_2":
        return f"## {text}"
    if btype == "heading_3":
        return f"### {text}"
    if btype == "paragraph":
        return text
    if btype == "bulleted_list_item":
        return f"{indent}- {text}"
    if btype == "numbered_list_item":
        return f"{indent}1. {text}"
    if btype == "to_do":
        checked = "x" if data.get("checked") else " "
        return f"{indent}- [{checked}] {text}"
    if btype == "quote":
        return f"> {text}"
    if btype == "callout":
        icon = data.get("icon") or {}
        emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
        return f"> {emoji} {text}".strip()
    if btype == "divider":
        return "---"
    if btype == "code":
        lang = data.get("language", "")
        return f"```{lang}\n{text}\n```"
    # tipos não tratados explicitamente: cai para o texto simples (se houver)
    return text


def render_blocks(block_id: str, headers: dict, depth: int = 0) -> list:
    lines = []
    for block in get_children_blocks(block_id, headers):
        line = block_to_md_line(block, depth)
        if line is not None:
            lines.append(line)
        if block.get("has_children"):
            lines.extend(render_blocks(block["id"], headers, depth + 1))
    return lines


def prop_plain_text(prop: dict) -> str:
    if not prop:
        return ""
    ptype = prop.get("type")
    if ptype == "title":
        return "".join(rt.get("plain_text", "") for rt in prop.get("title", []))
    if ptype == "rich_text":
        return "".join(rt.get("plain_text", "") for rt in prop.get("rich_text", []))
    if ptype == "select":
        sel = prop.get("select")
        return sel.get("name", "") if sel else ""
    if ptype == "status":
        st = prop.get("status")
        return st.get("name", "") if st else ""
    if ptype == "multi_select":
        return ", ".join(o.get("name", "") for o in prop.get("multi_select", []))
    if ptype == "url":
        return prop.get("url") or ""
    if ptype == "date":
        d = prop.get("date")
        return d.get("start", "") if d else ""
    return ""


def yaml_escape(value: str) -> str:
    value = value.replace('"', '\\"')
    return f'"{value}"'


def main():
    token = os.environ.get("NOTION_TOKEN")
    database_id = os.environ.get("NOTION_DATABASE_ID")
    output_dir = os.environ.get("OUTPUT_DIR", "estudos")

    if not token or not database_id:
        print("Defina NOTION_TOKEN e NOTION_DATABASE_ID antes de rodar.", file=sys.stderr)
        sys.exit(1)

    headers = notion_headers(token)
    pages = query_all_pages(database_id, headers)
    print(f"Encontradas {len(pages)} páginas na base.")

    written = []
    for page in pages:
        props = page.get("properties", {})
        titulo = prop_plain_text(props.get("Título")) or "Sem título"
        categoria = prop_plain_text(props.get("Categoria")) or "sem-categoria"
        subcategoria = prop_plain_text(props.get("Subcategoria"))
        nivel = prop_plain_text(props.get("Nível"))
        status = prop_plain_text(props.get("Status"))
        fonte = prop_plain_text(props.get("Fonte"))
        atualizado_em = page.get("last_edited_time", "")

        pasta = os.path.join(output_dir, slugify(categoria))
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, f"{slugify(titulo)}.md")

        corpo = render_blocks(page["id"], headers)

        front_matter = [
            "---",
            f"titulo: {yaml_escape(titulo)}",
            f"categoria: {yaml_escape(categoria)}",
        ]
        if subcategoria:
            front_matter.append(f"subcategoria: {yaml_escape(subcategoria)}")
        if nivel:
            front_matter.append(f"nivel: {yaml_escape(nivel)}")
        if status:
            front_matter.append(f"status: {yaml_escape(status)}")
        if fonte:
            front_matter.append(f"fonte: {yaml_escape(fonte)}")
        front_matter.append(f"atualizado_em: {yaml_escape(atualizado_em)}")
        front_matter.append("---")
        front_matter.append("")
        front_matter.append(f"# {titulo}")
        front_matter.append("")

        with open(caminho, "w", encoding="utf-8") as f:
            f.write("\n".join(front_matter) + "\n\n" + "\n\n".join(corpo) + "\n")

        written.append(caminho)
        print(f"  -> {caminho}")

    print(f"Concluído. {len(written)} arquivo(s) atualizado(s).")


if __name__ == "__main__":
    main()