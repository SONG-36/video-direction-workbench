# TRACK B KP0 CONTEXT

## Project Path

`/Volumes/server-data/projects/andy/0803/video-direction-workbench`

## Current Task

K-P0 Knowledge Catalog.

## Four Catalogs

- K01 Operational Research Lens Catalog
- K02 Platform & Content Rules Library
- K03 Creative Operator Library
- K04 Success / Failure Case Library

## knowledge_ref Format

```text
knowledge_ref = "<knowledge_type>:<knowledge_id>@<version>"
```

Example: `research_lens:problem_amplification@v0.1`

## Allowed Scope

- Design knowledge item fields.
- Design knowledge_ref format.
- Design minimal YAML / Markdown file structure.
- Design tag taxonomy.
- Design version rules.
- Design human approval rules.

## Forbidden

- Database
- UI
- Automatic learning
- Automatic overwrite of official catalog
- Automatic script generation
- Replacing ProductBrief fact boundary
- Modifying N02A code

## Relationship With N02A/SIG-P0/N18

- N02A references K-P0 through `ResearchBasis.knowledge_refs`.
- SIG-P0 may read K-P0 tags for simple classification but must not modify K-P0.
- N18 controls official catalog updates.

## Minimal Verification Direction

Create minimal K01/K02 entries with stable IDs and verify their knowledge_refs can be referenced by a ResearchBasis example.

## Do Not Modify

Do not modify N02A code in this track.
