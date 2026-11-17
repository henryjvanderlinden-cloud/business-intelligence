# Third-party notices

This repository is dedicated to the public domain under CC0 1.0 Universal ([`LICENSE`](LICENSE)), except for the
material below, which is not the author's and keeps its own licence
([ADR-0041](docs/20_decisions/0041-cc0-public-domain-dedication.md)). The README's
[Third-party material](README.md#third-party-material) section says what it is and where it appears; this file carries
the notices and attributions those licences ask to be kept with copies. Every host an evidence file of kind
`web source` cites must be named in this file, and `tools/check_repo.py` checks that it is.

## Wide World Importers, Microsoft SQL Server sample code

The Wide World Importers sample database, its data-load simulation and the data it generates come from
[github.com/microsoft/sql-server-samples](https://github.com/microsoft/sql-server-samples), folder
`samples/databases/wide-world-importers`. One evidence file quotes its simulation procedures from
`raw.githubusercontent.com/microsoft/sql-server-samples`. The repository's `license.txt`, read on 2026-11-17, verbatim:

```text
Microsoft SQL Server Sample Code

Copyright (c) Microsoft Corporation

All rights reserved.

MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
```

## Microsoft Learn documentation

Fourteen evidence files under `analysis/wwi/` quote the Microsoft Learn page *What is Wide World Importers*
(`learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is`), each naming the page's title and URL. The
source of that documentation, [github.com/MicrosoftDocs/sql-docs](https://github.com/MicrosoftDocs/sql-docs), is
licensed under Creative Commons Attribution 4.0 International
([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), per its `LICENSE` file, read on 2026-11-17. The excerpts
are © Microsoft Corporation. They were returned by a summarising fetch and were not checked against the page by hand,
as each file's `tool` field says, so they may differ from the page's wording.

## Wikipedia

Two evidence files under `analysis/wwi/` hold lists of ISO 3166 codes read from the Wikipedia pages
*ISO 3166-1* and *ISO 3166-2:US* (`en.wikipedia.org`), each naming its page and URL. Wikipedia's text is licensed under
Creative Commons Attribution-ShareAlike 4.0 ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)), by its
contributors; that licence is stated from the model's knowledge of Wikipedia's terms and was not re-read on
2026-11-17. The lists hold the codes of the ISO 3166 standard and nothing of the pages' prose.
