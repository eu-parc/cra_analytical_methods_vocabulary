# CRA Analytical Methods Vocabulary

A controlled vocabulary of analytical methods used in chemical risk assessment, developed within the [PARC project](https://www.eu-parc.eu/). Terms are published as nanopublications under the shared `https://w3id.org/chemical-exposome/terms/` namespace.

This vocabulary is part of the [chemical-exposome](https://w3id.org/chemical-exposome/) semantic infrastructure and is referenced via `sosa:usedProcedure` in the [chemicals-outdoor metadata schema](https://w3id.org/chemical-exposome/schema/chemicals-outdoor) and the PEH data model.

---

## Proposing a new analytical method term

1. Add one or more `*.yaml` files to the `dropbox/` folder following this structure. This is a minimal example:

```yaml
$schema: "https://w3id.org/chemical-exposome/schema/dropbox-analytical-method.schema.json"

analytical_methods:
  - id: FlameAAS
    name: Flame Atomic Absorption Spectroscopy
    abbreviation: Flame AAS
    description: >-
      Sample solution is nebulised into a flame for atomisation.
      Suitable for major and minor element concentrations (ppm range).
    parent_method: AtomicAbsorptionSpectroscopy
```

Notes:
- `id` is a local identifier — full URIs are minted automatically by the pipeline under `https://w3id.org/chemical-exposome/terms/`
- `name` is the full preferred label (skos:prefLabel)
- `abbreviation` is the standard acronym (skos:altLabel)
- `parent_method` references the local `id` or full URI of the parent method
- Set `top_concept: true` and omit `parent_method` for top-level concepts

See `schema/dropbox-analytical-method.schema.json` for the full field reference.

2. Open a PR with your `*.yaml` files added to `dropbox/`

---

## Under the hood

1. New YAML vocab files are dropped into `dropbox/`.
2. Processing converts them into RDF assertions in `unpublished/`.
3. Processed source YAML files move to `archive/` with a ULID suffix to avoid overwriting earlier submissions.
4. Publishing creates nanopublications from `unpublished/`.
5. Publishing also writes a timestamped term-to-nanopub redirect mapping into `redirect/`.
6. Successfully published assertion files move to `published/`.

---

## Folder semantics

- `dropbox/`: incoming YAML vocabulary files
- `archive/`: processed YAML files moved out of dropbox with ULID-labeled filenames
- `unpublished/`: generated RDF term assertions waiting for publish
- `redirect/`: timestamped term-to-nanopub identifier mappings produced during publishing
- `published/`: assertions already published as nanopublications
- `build/`: transient build artifacts
- `schema/`: vocabulary schema files

---

## Local usage

Install dependencies:

```bash
uv sync
```

Process incoming YAML from `dropbox/`:

```bash
make pipeline
```

Dry-run publish (no move to `published/`):

```bash
make publish-pipeline DRY=--dry-run
```

Real publish (requires nanopub credentials in environment):

```bash
export NANOPUB_PRIVATE_KEY=...
export NANOPUB_PUBLIC_KEY=...
export INTRO_NANOPUB_URI=...
make publish-pipeline
```

Each publish run writes a uniquely named redirect mapping file such as
`redirect/term-to-nanopub_20260424T120102Z.tsv`.

End-to-end local smoke test:

```bash
make test-flow
```

---

## GitHub Workflows

- `serialize.yaml`: on push to `main` with `dropbox/**` changes, runs `make pipeline` and commits `archive/` + `unpublished/` updates.
- `test-serialize.yaml`: on PR with `dropbox/**` changes, validates processing behaviour.
- `publish.yaml`: publishes nanopublications on:
  - release publish (real publish)
  - tag push (dry-run)
  - manual `workflow_dispatch` ("Publish mode" input: `dry-run` or `publish`)

In manual real publish mode (`workflow_dispatch` with `publish`), published assertion files are moved from `unpublished/` to `published/`, the new redirect mapping file is committed from `redirect/`, and both changes are pushed.

---

## Schema

- `schema/analytical-methods-vocabulary.schema.yaml` — LinkML schema defining the vocabulary model and its alignment to SKOS, OWL, and SOSA
- `schema/dropbox-analytical-method.schema.json` — JSON Schema for validating dropbox YAML submissions

---

## Namespace

| Purpose | URI |
|---------|-----|
| Term URIs | `https://w3id.org/chemical-exposome/terms/` |
| Schema | `https://w3id.org/chemical-exposome/schema/analytical-methods-vocabulary` |
| Dropbox schema | `https://w3id.org/chemical-exposome/schema/dropbox-analytical-method.schema.json` |

---

## Related resources

- [PARC project](https://www.eu-parc.eu/)
- [Chemical-exposome namespace](https://w3id.org/chemical-exposome/)
- [Chemicals-outdoor metadata schema](https://w3id.org/chemical-exposome/schema/chemicals-outdoor)
- [PEH data model](https://w3id.org/peh/)
- [Nanopublications](https://nanopub.net/)
